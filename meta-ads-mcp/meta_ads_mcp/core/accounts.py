"""Account-related functionality for Meta Ads API."""

import json
import re
import httpx
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any
from urllib.parse import urlparse, parse_qs
from .api import meta_api_tool, make_api_request
from .server import mcp_server


@mcp_server.tool()
@meta_api_tool
async def get_ad_accounts(access_token: Optional[str] = None, user_id: str = "me") -> str:
    """
    Get ad accounts accessible by a user. Fetches ALL accounts with pagination.
    
    Args:
        access_token: Meta API access token (optional - will use cached token if not provided)
        user_id: Meta user ID or "me" for the current user
    """
    all_accounts = []
    endpoint = f"{user_id}/adaccounts"
    params = {
        "fields": "id,name,account_status,currency",
        "limit": 200
    }
    
    data = await make_api_request(endpoint, access_token, params)
    
    if "data" in data:
        all_accounts.extend(data["data"])
        
        # Follow pagination to get ALL accounts
        while "paging" in data and "next" in data.get("paging", {}):
            next_url = data["paging"]["next"]
            match = re.search(r'graph\.facebook\.com/v[\d.]+/(.+)', next_url)
            if not match:
                break
            next_path = match.group(1).split("?")[0]
            parsed = urlparse(next_url)
            query_params = {k: v[0] for k, v in parse_qs(parsed.query).items()}
            query_params.pop("access_token", None)
            
            data = await make_api_request(next_path, access_token, query_params)
            if "data" in data:
                all_accounts.extend(data["data"])
            else:
                break
    
    return json.dumps({"data": all_accounts, "total_accounts": len(all_accounts)}, indent=2)


@mcp_server.tool()
@meta_api_tool
async def get_account_info(account_id: str, access_token: Optional[str] = None) -> str:
    """
    Get detailed information about a specific ad account.
    
    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        access_token: Meta API access token (optional - will use cached token if not provided)
    """
    if not account_id:
        return {
            "error": {
                "message": "Account ID is required",
                "details": "Please specify an account_id parameter",
                "example": "Use account_id='act_123456789' or account_id='123456789'"
            }
        }
    
    # Ensure account_id has the 'act_' prefix for API compatibility
    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"
    
    # Try to get the account info directly first
    endpoint = f"{account_id}"
    params = {
        "fields": "id,name,account_id,account_status,amount_spent,balance,currency,age,business_city,business_country_code,timezone_name"
    }
    
    data = await make_api_request(endpoint, access_token, params)
    
    # Check if the API request returned an error
    if "error" in data:
        # If access was denied, provide helpful error message with accessible accounts
        if "access" in str(data.get("error", {})).lower() or "permission" in str(data.get("error", {})).lower():
            # Get list of accessible accounts for helpful error message
            accessible_endpoint = "me/adaccounts"
            accessible_params = {
                "fields": "id,name,account_id,account_status,amount_spent,balance,currency,age,business_city,business_country_code",
                "limit": 50
            }
            accessible_accounts_data = await make_api_request(accessible_endpoint, access_token, accessible_params)
            
            if "data" in accessible_accounts_data:
                accessible_accounts = [
                    {"id": acc["id"], "name": acc["name"]} 
                    for acc in accessible_accounts_data["data"][:10]  # Show first 10
                ]
                return {
                    "error": {
                        "message": f"Account {account_id} is not accessible to your user account",
                        "details": "This account either doesn't exist or you don't have permission to access it",
                        "accessible_accounts": accessible_accounts,
                        "total_accessible_accounts": len(accessible_accounts_data["data"]),
                        "suggestion": "Try using one of the accessible account IDs listed above"
                    }
                }
        
        # Return the original error for non-permission related issues
        return data
    
    # Add DSA requirement detection
    if "business_country_code" in data:
        european_countries = ["DE", "FR", "IT", "ES", "NL", "BE", "AT", "IE", "DK", "SE", "FI", "NO"]
        if data["business_country_code"] in european_countries:
            data["dsa_required"] = True
            data["dsa_compliance_note"] = "This account is subject to European DSA (Digital Services Act) requirements"
        else:
            data["dsa_required"] = False
            data["dsa_compliance_note"] = "This account is not subject to European DSA requirements"
    
    return data


@mcp_server.tool()
@meta_api_tool
async def get_pixels(account_id: str, access_token: Optional[str] = None) -> str:
    """
    Get pixels (datasets) associated with a Meta Ads account.
    Use this to find pixel IDs needed for website custom audiences and conversion tracking.
    
    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        access_token: Meta API access token (optional - will use cached token if not provided)
    
    Returns:
        JSON response with pixels associated with the account, including id, name, and status
    """
    if not account_id:
        return json.dumps({"error": "No account ID provided"}, indent=2)
    
    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"
    
    endpoint = f"{account_id}/adspixels"
    params = {
        "fields": "id,name,creation_time,last_fired_time,is_unavailable,data_use_setting,code"
    }
    
    data = await make_api_request(endpoint, access_token, params)
    
    return json.dumps(data, indent=2)


@mcp_server.tool()
@meta_api_tool
async def get_account_videos(
    account_id: str,
    instagram_account_id: Optional[str] = None,
    media_type: str = "VIDEO",
    access_token: Optional[str] = None,
) -> str:
    """
    Get videos from all sources: Instagram posts, Instagram carousels, and Facebook Page.
    Use this to find video IDs needed for creating video custom audiences.
    Automatically paginates up to 500 posts and filters by last 365 days.

    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        instagram_account_id: Optional Instagram Business Account ID to fetch media from directly.
            If not provided, the tool will discover IG accounts and return the list for you to choose.
        media_type: Filter by media type. Options: "VIDEO" (default), "ALL", "IMAGE", "CAROUSEL_ALBUM"
        access_token: Meta API access token (optional - will use cached token if not provided)

    Returns:
        JSON with videos from Instagram and Facebook Page including id, title, source, and timestamps
    """
    if not account_id:
        return json.dumps({"error": "No account ID provided"}, indent=2)

    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"

    # If a specific IG account was provided, fetch media directly
    if instagram_account_id:
        return await _fetch_ig_media(instagram_account_id, media_type, access_token, account_id=account_id)

    # Step 1: Discover Instagram accounts
    ig_accounts = []

    ig_endpoint = f"{account_id}/instagram_accounts"
    ig_params = {"fields": "id,username,profile_pic,followers_count"}
    ig_data = await make_api_request(ig_endpoint, access_token, ig_params)
    ig_accounts = ig_data.get("data", [])

    if not ig_accounts:
        ig_endpoint2 = f"{account_id}/connected_instagram_accounts"
        ig_data2 = await make_api_request(ig_endpoint2, access_token, ig_params)
        ig_accounts = ig_data2.get("data", [])

    # Fallback: find IG accounts via Pages
    if not ig_accounts:
        try:
            pages_data = await make_api_request("me/accounts", access_token, {
                "fields": "id,name,instagram_business_account{id,username,followers_count}",
                "limit": 100
            })
            seen_ig_ids = set()
            for page in pages_data.get("data", []):
                ig_biz = page.get("instagram_business_account")
                if ig_biz and ig_biz.get("id") not in seen_ig_ids:
                    seen_ig_ids.add(ig_biz["id"])
                    ig_accounts.append({
                        "id": ig_biz["id"],
                        "username": ig_biz.get("username", ""),
                        "followers_count": ig_biz.get("followers_count", 0),
                        "page_name": page.get("name", ""),
                    })
        except Exception:
            pass

    if not ig_accounts:
        return json.dumps({
            "error": "No Instagram accounts found",
            "suggestion": "Make sure your Instagram Business/Creator account is connected to this ad account in Meta Business Suite"
        }, indent=2)

    # If only 1 IG account, fetch media directly
    if len(ig_accounts) == 1:
        return await _fetch_ig_media(ig_accounts[0]["id"], media_type, access_token, ig_accounts[0].get("username"), account_id=account_id)

    # Multiple IG accounts: return the list so the AI can ask the user which one
    return json.dumps({
        "multiple_accounts_found": True,
        "message": "Multiple Instagram accounts found. Ask the user which one to use, then call this tool again with instagram_account_id.",
        "instagram_accounts": [
            {"id": a.get("id"), "username": a.get("username", ""), "followers": a.get("followers_count", 0), "page_name": a.get("page_name", "")}
            for a in ig_accounts
        ],
    }, indent=2)


async def _fetch_ig_media(ig_id: str, media_type: str, access_token: Optional[str], username: str = "", account_id: str = "") -> str:
    """Internal helper to fetch media from a specific Instagram account and its linked Facebook Page.
    Paginates up to 500 posts to cover ~365 days of content."""
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=365)

    # --- Instagram videos (including videos inside carousels) ---
    ig_all = await _paginate_media(ig_id, "id,caption,media_type,permalink,timestamp,children{id,media_type}", cutoff_date, access_token)
    ig_all = _filter_by_date(ig_all, cutoff_date)

    ig_videos = []
    for item in ig_all:
        if item.get("media_type") == "VIDEO":
            item["source"] = "instagram"
            item["instagram_account_id"] = ig_id
            if username:
                item["instagram_username"] = username
            item.pop("children", None)
            ig_videos.append(item)
        elif item.get("media_type") == "CAROUSEL_ALBUM":
            children = item.get("children", {}).get("data", [])
            for child in children:
                if child.get("media_type") == "VIDEO":
                    ig_videos.append({
                        "id": child["id"],
                        "media_type": "VIDEO",
                        "source": "instagram_carousel",
                        "carousel_id": item["id"],
                        "caption": item.get("caption"),
                        "permalink": item.get("permalink"),
                        "timestamp": item.get("timestamp"),
                        "instagram_account_id": ig_id,
                        **({"instagram_username": username} if username else {}),
                    })

    if media_type != "ALL" and media_type != "VIDEO":
        ig_videos = [m for m in ig_all if m.get("media_type") == media_type]
        for item in ig_videos:
            item["source"] = "instagram"
            item["instagram_account_id"] = ig_id
            if username:
                item["instagram_username"] = username

    # --- Facebook Page videos ---
    fb_videos = []
    page_name = ""
    try:
        pages_data = await make_api_request("me/accounts", access_token, {
            "fields": "id,name,access_token,instagram_business_account{id}",
            "limit": 100
        })
        for page in pages_data.get("data", []):
            ig_biz = page.get("instagram_business_account", {})
            if ig_biz.get("id") == ig_id:
                page_id = page["id"]
                page_token = page.get("access_token", "")
                page_name = page.get("name", "")
                if page_token:
                    fb_data = await _paginate_media(
                        page_id, "id,title,description,created_time,length",
                        cutoff_date, access_token, endpoint_suffix="videos",
                        token_override=page_token
                    )
                    fb_data = _filter_by_date(fb_data, cutoff_date, date_field="created_time")
                    for item in fb_data:
                        item["source"] = "facebook"
                        item["page_id"] = page_id
                        item["page_name"] = page_name
                        item["media_type"] = "VIDEO"
                    fb_videos = fb_data
                break
    except Exception:
        pass

    return json.dumps({
        "instagram_account": {"id": ig_id, "username": username},
        "facebook_page": {"name": page_name} if page_name else None,
        "instagram_videos": len(ig_videos),
        "facebook_videos": len(fb_videos),
        "total_videos": len(ig_videos) + len(fb_videos),
        "media_type_filter": media_type,
        "media": ig_videos + fb_videos,
    }, indent=2)


async def _paginate_media(
    source_id: str, fields: str, cutoff_date: datetime,
    access_token: Optional[str], endpoint_suffix: str = "media",
    token_override: Optional[str] = None
) -> list:
    """Paginate through media/videos endpoint up to 500 items or 365-day cutoff."""
    all_items = []
    max_posts = 500
    endpoint = f"{source_id}/{endpoint_suffix}"
    params = {"fields": fields, "limit": 200}

    if token_override:
        params["access_token"] = token_override
        # Direct call with page token
        async with httpx.AsyncClient() as client:
            url = f"https://graph.facebook.com/v25.0/{endpoint}"
            r = await client.get(url, params=params, timeout=30.0)
            data = r.json()
        all_items.extend(data.get("data", []))

        while len(all_items) < max_posts and "paging" in data and "next" in data.get("paging", {}):
            last = all_items[-1] if all_items else None
            ts = last.get("timestamp") or last.get("created_time") if last else None
            if ts:
                try:
                    last_ts = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                    if last_ts < cutoff_date:
                        break
                except (ValueError, TypeError):
                    pass
            async with httpx.AsyncClient() as client:
                r = await client.get(data["paging"]["next"], timeout=30.0)
                data = r.json()
            all_items.extend(data.get("data", []))
    else:
        data = await make_api_request(endpoint, access_token, params)
        all_items.extend(data.get("data", []))

        while len(all_items) < max_posts and "paging" in data and "next" in data.get("paging", {}):
            last = all_items[-1] if all_items else None
            ts = last.get("timestamp") or last.get("created_time") if last else None
            if ts:
                try:
                    last_ts = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                    if last_ts < cutoff_date:
                        break
                except (ValueError, TypeError):
                    pass
            next_url = data["paging"]["next"]
            m = re.search(r'graph\.facebook\.com/v[\d.]+/(.+)', next_url)
            if not m:
                break
            next_path = m.group(1).split("?")[0]
            parsed_url = urlparse(next_url)
            qp = {k: v[0] for k, v in parse_qs(parsed_url.query).items()}
            qp.pop("access_token", None)
            data = await make_api_request(next_path, access_token, qp)
            all_items.extend(data.get("data", []))

    return all_items


def _filter_by_date(items: list, cutoff_date: datetime, date_field: str = "timestamp") -> list:
    """Filter out items older than cutoff_date."""
    filtered = []
    for m in items:
        ts = m.get(date_field)
        if ts:
            try:
                item_date = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                if item_date < cutoff_date:
                    continue
            except (ValueError, TypeError):
                pass
        filtered.append(m)
    return filtered


@mcp_server.tool()
@meta_api_tool
async def create_pixel(
    account_id: str,
    name: str,
    access_token: Optional[str] = None,
) -> str:
    """
    Create a new Meta Pixel (dataset) for an ad account.

    A pixel is a piece of JavaScript code that tracks visitor activity on your website.
    Use pixels for conversion tracking, audience building, and ad optimization.

    Important notes:
    - Each ad account can have a maximum of 100 pixels.
    - Once created, a pixel CANNOT be deleted via the API. You can only archive it
      in the Ads Manager UI, so choose names carefully.
    - Use get_pixels to check existing pixels before creating a new one.

    Args:
        account_id: Ad account ID (format: act_XXXXXXXXX)
        name: Name for the pixel (e.g., "My Website Pixel"). Must be unique within the account.
        access_token: Meta API access token (optional)

    Returns:
        JSON string with the created pixel ID.

    Example:
        create_pixel("act_123456789012345", "Landing Page Pixel")
    """
    if not account_id:
        return json.dumps({"error": "account_id is required"}, indent=2)
    if not name:
        return json.dumps({"error": "name is required"}, indent=2)

    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"

    endpoint = f"{account_id}/adspixels"
    params = {"name": name}

    data = await make_api_request(endpoint, access_token, params, method="POST")

    # If pixel was created, fetch the JS code snippet
    pixel_id = data.get("id")
    if pixel_id and "error" not in data:
        pixel_details = await make_api_request(
            pixel_id, access_token, {"fields": "id,name,code"}
        )
        if "code" in pixel_details:
            data["code"] = pixel_details["code"]
            data["note"] = "Install this JavaScript code in your website <head> tag to start tracking events."

    return json.dumps(data, indent=2)