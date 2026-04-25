"""Custom Audience creation tools for Meta Ads API.

Supports creating Custom Audiences from:
- Website (Pixel) visitors
- Video engagement
- Facebook Page engagement
- Instagram account engagement
- Lead form engagement
"""

import json
from typing import Optional, List, Dict
from .api import meta_api_tool, make_api_request
from .server import mcp_server


@mcp_server.tool()
@meta_api_tool
async def create_website_custom_audience(
    account_id: str,
    name: str,
    pixel_id: str,
    retention_days: int = 30,
    rule_type: str = "all_visitors",
    url_contains: Optional[str] = None,
    url_equals: Optional[str] = None,
    description: Optional[str] = None,
    access_token: Optional[str] = None,
) -> str:
    """
    Create a Custom Audience based on website visitors tracked by a Meta Pixel.

    Args:
        account_id: Ad account ID (format: act_XXXXXXXXX)
        name: Name for the custom audience
        pixel_id: The Meta Pixel ID to use as data source
        retention_days: Number of days to retain users in the audience (1-180, default: 30)
        rule_type: Type of website rule. Options:
            - "all_visitors" (default): Everyone who visited your website
            - "specific_pages": People who visited specific pages (use url_contains or url_equals)
            - "time_spent": Top 25% of visitors by time spent
            - "event": People who triggered a specific pixel event (use url_contains for the event name:
              Purchase, AddToCart, InitiateCheckout, CompleteRegistration, AddPaymentInfo,
              ViewContent, Search, AddToWishlist, Lead, Subscribe, StartTrial, Contact)
        url_contains: For specific_pages rule: URL must contain this string (e.g., "/products").
                      For event rule: the pixel event name (e.g., "Purchase")
        url_equals: For specific_pages rule: URL must exactly match this string
        description: Optional description for the audience
        access_token: Meta API access token (optional)

    Returns:
        JSON string with the created audience ID and details
    """
    if not account_id or not name or not pixel_id:
        return json.dumps({"error": "account_id, name, and pixel_id are required"}, indent=2)

    retention_days = max(1, min(180, retention_days))
    retention_seconds = retention_days * 86400

    # Build the rule in v24.0 format with inclusions wrapper (per Meta docs)
    if rule_type == "event" and url_contains:
        filters = [{"field": "event", "operator": "eq", "value": url_contains}]
    elif rule_type == "specific_pages" and (url_contains or url_equals):
        url_value = url_equals or url_contains
        filters = [{"field": "url", "operator": "i_contains", "value": url_value}]
    elif rule_type == "time_spent":
        filters = [{"field": "time_spent", "operator": "top", "value": 25}]
    else:
        # all_visitors — use empty url filter to match all pages
        filters = [{"field": "url", "operator": "i_contains", "value": ""}]

    rule = {
        "inclusions": {
            "operator": "or",
            "rules": [
                {
                    "event_sources": [{"id": pixel_id, "type": "pixel"}],
                    "retention_seconds": retention_seconds,
                    "filter": {"operator": "and", "filters": filters},
                }
            ],
        }
    }

    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"

    params = {
        "name": name,
        "rule": json.dumps(rule),
        "prefill": True,
    }
    if retention_days:
        params["retention_days"] = retention_days
    if description:
        params["description"] = description

    endpoint = f"{account_id}/customaudiences"
    data = await make_api_request(endpoint, access_token, params, method="POST", use_multipart=True, api_version="v25.0")

    if "error" in data:
        return json.dumps({"error": "Failed to create website custom audience", "details": data.get("error")}, indent=2)

    return json.dumps({
        "success": True,
        "audience_id": data.get("id"),
        "name": name,
        "subtype": "WEBSITE",
        "pixel_id": pixel_id,
        "rule_type": rule_type,
        "retention_days": retention_days,
    }, indent=2)


@mcp_server.tool()
@meta_api_tool
async def create_video_custom_audience(
    account_id: str,
    name: str,
    video_ids: List[str],
    engagement_type: str = "video_watched",
    retention_days: int = 365,
    description: Optional[str] = None,
    access_token: Optional[str] = None,
) -> str:
    """
    Create a Custom Audience based on people who engaged with your videos on Facebook or Instagram.
    Use video IDs from Instagram posts (/{ig_id}/media) or Facebook Page posts (/{page_id}/videos).

    Args:
        account_id: Ad account ID (format: act_XXXXXXXXX)
        name: Name for the custom audience
        video_ids: List of video IDs from Instagram media or Facebook Page videos
        engagement_type: Type of video engagement. Options:
            - "video_watched" (default): People who watched at least 3 seconds
            - "video_completed": People who watched 95% or more
            - "video_view_10s": People who watched at least 10 seconds
            - "video_view_15s": People who watched at least 15 seconds
            - "video_view_25_percent": People who watched at least 25%
            - "video_view_50_percent": People who watched at least 50%
            - "video_view_75_percent": People who watched at least 75%
        retention_days: Days to retain users (1-365, default: 365)
        description: Optional description for the audience
        access_token: Meta API access token (optional)

    Returns:
        JSON string with the created audience ID and details
    """
    if not account_id or not name or not video_ids:
        return json.dumps({"error": "account_id, name, and video_ids are required"}, indent=2)

    retention_days = max(1, min(365, retention_days))

    valid_events = {
        "video_watched", "video_completed",
        "video_view_10s", "video_view_15s",
        "video_view_25_percent", "video_view_50_percent", "video_view_75_percent",
    }
    event_name = engagement_type if engagement_type in valid_events else "video_watched"

    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"

    rule = [{"object_id": vid, "event_name": event_name} for vid in video_ids]

    params = {
        "name": name,
        "subtype": "ENGAGEMENT",
        "rule": json.dumps(rule),
        "retention_days": retention_days,
        "prefill": True,
    }
    if description:
        params["description"] = description

    endpoint = f"{account_id}/customaudiences"
    data = await make_api_request(endpoint, access_token, params, method="POST", use_multipart=True, api_version="v25.0")

    if "error" in data:
        return json.dumps({"error": "Failed to create video custom audience", "details": data.get("error")}, indent=2)

    return json.dumps({
        "success": True,
        "audience_id": data.get("id"),
        "name": name,
        "subtype": "ENGAGEMENT",
        "engagement_type": event_name,
        "video_ids": video_ids,
        "retention_days": retention_days,
    }, indent=2)


@mcp_server.tool()
@meta_api_tool
async def create_page_custom_audience(
    account_id: str,
    name: str,
    page_id: str,
    engagement_type: str = "page_engaged",
    retention_days: int = 365,
    description: Optional[str] = None,
    access_token: Optional[str] = None,
) -> str:
    """
    Create a Custom Audience based on people who engaged with your Facebook Page.

    Args:
        account_id: Ad account ID (format: act_XXXXXXXXX)
        name: Name for the custom audience
        page_id: Facebook Page ID to use as source
        engagement_type: Type of page engagement. Options:
            - "page_engaged" (default): Everyone who engaged with the page
            - "page_visited": People who visited the page
            - "page_messaged": People who sent a message to the page
            - "page_cta_clicked": People who clicked any CTA button
            - "page_liked": People who currently like or follow the page
        retention_days: Days to retain users (1-365, default: 365)
        description: Optional description for the audience
        access_token: Meta API access token (optional)

    Returns:
        JSON string with the created audience ID and details
    """
    if not account_id or not name or not page_id:
        return json.dumps({"error": "account_id, name, and page_id are required"}, indent=2)

    retention_days = max(1, min(365, retention_days))

    # Map engagement_type to Meta API filter
    action_map = {
        "page_engaged": "page_engaged",
        "page_visited": "page_visited",
        "page_messaged": "page_messaged",
        "page_cta_clicked": "page_cta_clicked",
        "page_liked": "page_liked",
    }
    action = action_map.get(engagement_type, "page_engaged")

    # page_liked (current followers) does not support retention_seconds
    rule_entry: dict = {
        "event_sources": [{"id": page_id, "type": "page"}],
        "filter": {
            "operator": "and",
            "filters": [{"field": "event", "operator": "eq", "value": action}],
        },
    }
    if action != "page_liked":
        rule_entry["retention_seconds"] = retention_days * 86400

    rule = {
        "inclusions": {
            "operator": "or",
            "rules": [rule_entry],
        }
    }

    params = {
        "name": name,
        "rule": json.dumps(rule),
        "prefill": True,
    }
    if description:
        params["description"] = description

    endpoint = f"{account_id}/customaudiences"
    data = await make_api_request(endpoint, access_token, params, method="POST", use_multipart=True, api_version="v25.0")

    if "error" in data:
        return json.dumps({"error": "Failed to create page custom audience", "details": data.get("error")}, indent=2)

    return json.dumps({
        "success": True,
        "audience_id": data.get("id"),
        "name": name,
        "subtype": "ENGAGEMENT",
        "page_id": page_id,
        "engagement_type": engagement_type,
        "retention_days": None if action == "page_liked" else retention_days,
    }, indent=2)


@mcp_server.tool()
@meta_api_tool
async def create_instagram_custom_audience(
    account_id: str,
    name: str,
    instagram_account_id: str,
    engagement_type: str = "ig_business_profile_all",
    retention_days: int = 365,
    description: Optional[str] = None,
    access_token: Optional[str] = None,
) -> str:
    """
    Create a Custom Audience based on people who engaged with your Instagram professional account.

    Args:
        account_id: Ad account ID (format: act_XXXXXXXXX)
        name: Name for the custom audience
        instagram_account_id: Instagram professional account ID (or Facebook Page ID — will auto-resolve)
        engagement_type: Type of Instagram engagement. Options:
            - "ig_business_profile_all" (default): Everyone who engaged with the profile (most inclusive)
            - "ig_business_profile_engaged": People who engaged with content or ads
            - "ig_business_profile_visit": People who visited the profile
            - "ig_user_messaged_business": People who sent a message
            - "ig_business_profile_ad_saved": People who saved a post or ad
            - "ig_business_profile_follow": Current followers (no retention, real-time)
        retention_days: Days to retain users (1-730, default: 365)
        description: Optional description for the audience
        access_token: Meta API access token (optional)

    Returns:
        JSON string with the created audience ID and details
    """
    if not account_id or not name or not instagram_account_id:
        return json.dumps({"error": "account_id, name, and instagram_account_id are required"}, indent=2)

    retention_days = max(1, min(730, retention_days))

    # Auto-resolve: if a Page ID was passed instead of IG Business Profile ID,
    # try to get the instagram_business_account from the Page
    try:
        page_data = await make_api_request(
            instagram_account_id, access_token,
            {"fields": "instagram_business_account"}, method="GET"
        )
        if "instagram_business_account" in page_data:
            ig_business_id = page_data["instagram_business_account"]["id"]
        else:
            ig_business_id = instagram_account_id
    except Exception:
        ig_business_id = instagram_account_id

    action_map = {
        "ig_business_profile_all": "ig_business_profile_all",
        "ig_business_profile_engaged": "ig_business_profile_engaged",
        "ig_business_profile_visit": "ig_business_profile_visit",
        "ig_user_messaged_business": "ig_user_messaged_business",
        "ig_business_profile_ad_saved": "ig_business_profile_ad_saved",
        "ig_business_profile_follow": "ig_business_profile_follow",
    }
    action = action_map.get(engagement_type, "ig_business_profile_all")

    # ig_business_profile_follow (current followers) does not support retention_seconds
    rule_entry: dict = {
        "event_sources": [{"id": ig_business_id, "type": "ig_business"}],
        "filter": {
            "operator": "and",
            "filters": [{"field": "event", "operator": "eq", "value": action}],
        },
    }
    if action != "ig_business_profile_follow":
        rule_entry["retention_seconds"] = retention_days * 86400

    rule = {
        "inclusions": {
            "operator": "or",
            "rules": [rule_entry],
        }
    }

    params = {
        "name": name,
        "rule": json.dumps(rule),
        "prefill": True,
    }
    if description:
        params["description"] = description

    endpoint = f"{account_id}/customaudiences"
    data = await make_api_request(endpoint, access_token, params, method="POST", use_multipart=True, api_version="v25.0")

    if "error" in data:
        return json.dumps({"error": "Failed to create Instagram custom audience", "details": data.get("error")}, indent=2)

    return json.dumps({
        "success": True,
        "audience_id": data.get("id"),
        "name": name,
        "subtype": "IG_BUSINESS" if action == "ig_business_profile_follow" else "ENGAGEMENT",
        "instagram_account_id": instagram_account_id,
        "engagement_type": engagement_type,
        "retention_days": None if action == "ig_business_profile_follow" else retention_days,
    }, indent=2)


@mcp_server.tool()
@meta_api_tool
async def create_leadform_custom_audience(
    account_id: str,
    name: str,
    page_id: str,
    leadform_ids: Optional[List[str]] = None,
    engagement_type: str = "lead_generation_submitted",
    retention_days: int = 365,
    description: Optional[str] = None,
    access_token: Optional[str] = None,
) -> str:
    """
    Create a Custom Audience based on people who interacted with your lead generation forms.

    Args:
        account_id: Ad account ID (format: act_XXXXXXXXX)
        name: Name for the custom audience
        page_id: Facebook Page ID that owns the lead forms
        leadform_ids: Optional list of specific lead form IDs. If not provided, includes all forms from the page.
        engagement_type: Type of lead form engagement. Options:
            - "lead_generation_submitted" (default): People who submitted (completed) a form
            - "lead_generation_opened": People who opened but didn't submit a form
            - "lead_generation_opened_or_submitted": People who opened or submitted a form
        retention_days: Days to retain users (1-365, default: 365)
        description: Optional description for the audience
        access_token: Meta API access token (optional)

    Returns:
        JSON string with the created audience ID and details
    """
    if not account_id or not name or not page_id:
        return json.dumps({"error": "account_id, name, and page_id are required"}, indent=2)

    retention_days = max(1, min(365, retention_days))

    action_map = {
        "lead_generation_submitted": "lead_generation_submitted",
        "lead_generation_opened": "lead_generation_opened",
        "lead_generation_opened_or_submitted": "lead_generation_opened_or_submitted",
    }
    action = action_map.get(engagement_type, "lead_generation_submitted")

    # Build event sources
    event_sources = [{"id": page_id, "type": "page"}]

    # If specific lead form IDs are provided, add them
    filters = [{"field": "event", "operator": "eq", "value": action}]
    if leadform_ids and len(leadform_ids) > 0:
        filters.append({"field": "form_id", "operator": "any_of", "value": leadform_ids})

    rule = {
        "inclusions": {
            "operator": "or",
            "rules": [
                {
                    "event_sources": event_sources,
                    "retention_seconds": retention_days * 86400,
                    "filter": {"operator": "and", "filters": filters},
                }
            ],
        }
    }

    params = {
        "name": name,
        "rule": json.dumps(rule),
        "prefill": True,
    }
    if description:
        params["description"] = description

    endpoint = f"{account_id}/customaudiences"
    data = await make_api_request(endpoint, access_token, params, method="POST", use_multipart=True, api_version="v25.0")

    if "error" in data:
        return json.dumps({"error": "Failed to create lead form custom audience", "details": data.get("error")}, indent=2)

    return json.dumps({
        "success": True,
        "audience_id": data.get("id"),
        "name": name,
        "subtype": "ENGAGEMENT",
        "page_id": page_id,
        "leadform_ids": leadform_ids,
        "engagement_type": engagement_type,
        "retention_days": retention_days,
    }, indent=2)


@mcp_server.tool()
@meta_api_tool
async def list_custom_audiences(
    account_id: str,
    limit: int = 50,
    access_token: Optional[str] = None,
) -> str:
    """
    List all Custom Audiences in an ad account.

    Args:
        account_id: Ad account ID (format: act_XXXXXXXXX)
        limit: Maximum number of audiences to return (default: 50)
        access_token: Meta API access token (optional)

    Returns:
        JSON with list of custom audiences including id, name, subtype, approximate_count, and delivery_status
    """
    if not account_id:
        return json.dumps({"error": "account_id is required"}, indent=2)

    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"

    endpoint = f"{account_id}/customaudiences"
    params = {
        "fields": "id,name,subtype,description,approximate_count_lower_bound,approximate_count_upper_bound,time_created,time_updated,delivery_status,operation_status,retention_days",
        "limit": min(limit, 200),
    }

    data = await make_api_request(endpoint, access_token, params)

    if "error" in data:
        return json.dumps({"error": "Failed to list custom audiences", "details": data.get("error")}, indent=2)

    audiences = data.get("data", [])
    results = []
    for aud in audiences:
        results.append({
            "id": aud.get("id"),
            "name": aud.get("name"),
            "subtype": aud.get("subtype"),
            "description": aud.get("description"),
            "approximate_count": aud.get("approximate_count_lower_bound"),
            "retention_days": aud.get("retention_days"),
            "delivery_status": aud.get("delivery_status", {}).get("status") if isinstance(aud.get("delivery_status"), dict) else None,
            "operation_status": aud.get("operation_status", {}).get("status") if isinstance(aud.get("operation_status"), dict) else None,
            "time_created": aud.get("time_created"),
            "time_updated": aud.get("time_updated"),
        })

    return json.dumps({
        "account_id": account_id,
        "total_audiences": len(results),
        "audiences": results,
    }, indent=2)


@mcp_server.tool()
@meta_api_tool
async def create_lookalike_audience(
    account_id: str,
    name: str,
    origin_type: str = "custom_audience",
    origin_audience_id: Optional[str] = None,
    origin_ids: Optional[List[str]] = None,
    page_id: Optional[str] = None,
    country: str = "BR",
    ratio: float = 0.01,
    starting_ratio: Optional[float] = None,
    allow_international_seeds: bool = False,
    description: Optional[str] = None,
    access_token: Optional[str] = None,
) -> str:
    """
    Create a Lookalike Audience to reach people similar to your existing customers.
    Lookalike audiences take 1-6 hours to fully populate.

    There are 3 seed types:
    1. custom_audience: Based on an existing Custom Audience (min 100 members)
    2. campaign_conversions: Based on people who converted from campaigns/adsets
    3. page_fans: Based on people who like a Facebook Page

    Args:
        account_id: Ad account ID (format: act_XXXXXXXXX)
        name: Name for the lookalike audience
        origin_type: Seed type. Options: "custom_audience" (default), "campaign_conversions", "page_fans"
        origin_audience_id: Required for custom_audience. The Custom Audience ID to use as seed (min 100 members)
        origin_ids: Required for campaign_conversions. List of campaign or adset IDs to use as seed (min 100 conversions)
        page_id: Required for page_fans. The Facebook Page ID whose fans will be used as seed
        country: Country code to find lookalike members (default: "BR" for Brazil)
        ratio: Audience size as percentage of country population. Range: 0.01 to 0.20 (1% to 20%). Default: 0.01 (1%)
        starting_ratio: Optional starting percentage for a range. E.g., starting_ratio=0.01 + ratio=0.02 = 1%-2% segment
        allow_international_seeds: If True, Facebook will find seed members from other countries if needed (default: False)
        description: Optional description for the audience
        access_token: Meta API access token (optional)

    Returns:
        JSON with the created lookalike audience ID and details
    """
    if not account_id:
        return json.dumps({"error": "account_id is required"}, indent=2)

    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"

    if ratio < 0.01 or ratio > 0.20:
        return json.dumps({"error": "ratio must be between 0.01 and 0.20 (1% to 20%)"}, indent=2)

    if starting_ratio is not None and starting_ratio >= ratio:
        return json.dumps({"error": "starting_ratio must be less than ratio"}, indent=2)

    lookalike_spec: dict = {
        "ratio": ratio,
        "country": country,
        "allow_international_seeds": allow_international_seeds,
    }

    if starting_ratio is not None:
        lookalike_spec["starting_ratio"] = starting_ratio
        lookalike_spec["type"] = "custom_ratio"
    else:
        lookalike_spec["type"] = "custom_ratio"

    params: dict = {
        "name": name,
        "subtype": "LOOKALIKE",
    }

    if origin_type == "custom_audience":
        if not origin_audience_id:
            return json.dumps({"error": "origin_audience_id is required for custom_audience seed type"}, indent=2)
        params["origin_audience_id"] = origin_audience_id

    elif origin_type == "campaign_conversions":
        if not origin_ids or len(origin_ids) == 0:
            return json.dumps({"error": "origin_ids (campaign or adset IDs) is required for campaign_conversions seed type"}, indent=2)
        lookalike_spec["origin_ids"] = origin_ids
        lookalike_spec["conversion_type"] = "campaign_conversions"

    elif origin_type == "page_fans":
        if not page_id:
            return json.dumps({"error": "page_id is required for page_fans seed type"}, indent=2)
        lookalike_spec["page_id"] = page_id
        lookalike_spec["conversion_type"] = "page_like"

    else:
        return json.dumps({"error": f"Invalid origin_type: {origin_type}. Must be 'custom_audience', 'campaign_conversions', or 'page_fans'"}, indent=2)

    params["lookalike_spec"] = json.dumps(lookalike_spec)

    if description:
        params["description"] = description

    endpoint = f"{account_id}/customaudiences"
    data = await make_api_request(endpoint, access_token, params, method="POST", use_multipart=True, api_version="v25.0")

    if "error" in data:
        error_msg = data.get("error", {})
        user_msg = error_msg.get("error_user_msg", "") if isinstance(error_msg, dict) else ""
        return json.dumps({
            "error": "Failed to create lookalike audience",
            "details": error_msg,
            "user_message": user_msg,
        }, indent=2)

    return json.dumps({
        "success": True,
        "audience_id": data.get("id"),
        "name": name,
        "subtype": "LOOKALIKE",
        "origin_type": origin_type,
        "country": country,
        "ratio": ratio,
        "starting_ratio": starting_ratio,
        "note": "Lookalike audiences take 1-6 hours to fully populate. Check status with list_custom_audiences.",
    }, indent=2)


@mcp_server.tool()
@meta_api_tool
async def create_customer_list_audience(
    account_id: str,
    name: str,
    customers: List[Dict[str, str]],
    description: Optional[str] = None,
    access_token: Optional[str] = None,
) -> str:
    """
    Create a Custom Audience from a customer list (emails, phones, names) (v25.0).

    Data is automatically hashed with SHA256 before upload as required by Meta.
    Max 500 custom audiences per account. Each upload batch supports up to 10000 entries.

    Args:
        account_id: Ad account ID (format: act_XXXXXXXXX)
        name: Name for the custom audience
        customers: List of customer dicts. Each dict can have:
            email: Customer email
            phone: Phone number (will auto-add country code 55 for BR if missing)
            fn: First name
            ln: Last name
            Example: [{"email":"joao@email.com","phone":"11999998888","fn":"Joao"}]
        description: Optional description
        access_token: Meta API access token (optional)

    Returns:
        JSON with audience_id and upload stats (received, invalid entries)
    """
    import hashlib

    if not account_id or not name or not customers:
        return json.dumps({"error": "account_id, name, and customers are required"}, indent=2)

    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"

    def sha256(val):
        if not val:
            return ""
        return hashlib.sha256(val.strip().lower().encode("utf-8")).hexdigest()

    def normalize_phone(phone):
        if not phone:
            return ""
        digits = "".join(c for c in phone if c.isdigit())
        if not digits:
            return ""
        if len(digits) <= 11:
            digits = "55" + digits
        return digits

    # Step 1: Create empty audience
    endpoint = f"{account_id}/customaudiences"
    params = {
        "name": name,
        "subtype": "CUSTOM",
        "customer_file_source": "USER_PROVIDED_ONLY",
    }
    if description:
        params["description"] = description

    data = await make_api_request(endpoint, access_token, params, method="POST")
    if "error" in data:
        return json.dumps({"error": "Failed to create audience", "details": data.get("error")}, indent=2)

    audience_id = data.get("id")

    # Step 2: Upload customer data in batches
    batch_size = 2000
    total_received = 0
    total_invalid = 0

    schema = ["EMAIL", "PHONE", "FN", "LN"]

    for i in range(0, len(customers), batch_size):
        batch = customers[i:i + batch_size]
        hashed_data = []
        for c in batch:
            row = [
                sha256(c.get("email", "")),
                sha256(normalize_phone(c.get("phone", ""))),
                sha256(c.get("fn", "")),
                sha256(c.get("ln", "")),
            ]
            hashed_data.append(row)

        payload = json.dumps({"schema": schema, "data": hashed_data})
        upload_endpoint = f"{audience_id}/users"
        upload_params = {"payload": payload}

        result = await make_api_request(upload_endpoint, access_token, upload_params, method="POST")
        total_received += result.get("num_received", 0)
        total_invalid += result.get("num_invalid_entries", 0)

    return json.dumps({
        "success": True,
        "audience_id": audience_id,
        "name": name,
        "total_customers": len(customers),
        "total_received": total_received,
        "total_invalid": total_invalid,
    }, indent=2)
