"""Duplication functionality for Meta Ads API v25.0.

Provides tools to duplicate campaigns, ad sets, ads, and creatives
using direct Meta Graph API calls. Each duplication creates new objects
with configurable overrides for name, status, budget, and targeting.
"""

import json
from datetime import datetime, timezone
from typing import Optional, Dict, Any, List
from .server import mcp_server
from .api import meta_api_tool, make_api_request


# ---------------------------------------------------------------------------
# Internal helpers (not exposed as MCP tools)
# ---------------------------------------------------------------------------

async def _duplicate_single_ad(
    ad_id: str,
    target_adset_id: str,
    account_id: str,
    name_suffix: str,
    new_status: str,
    access_token: str,
) -> Dict[str, Any]:
    """Duplicate a single ad into a target ad set.

    Returns a dict with ``original_id``, ``new_id``, and ``status`` keys.
    On failure the ``new_id`` is None and ``error`` is present.
    """
    # Read original ad
    ad_fields = "name,adset_id,creative,status,bid_amount,tracking_specs,conversion_domain"
    ad_data = await make_api_request(ad_id, access_token, {"fields": ad_fields})
    if "error" in ad_data:
        return {"original_id": ad_id, "new_id": None, "status": "failed", "error": ad_data["error"]}

    # Build creation params
    params: Dict[str, Any] = {
        "name": ad_data.get("name", "Ad") + name_suffix,
        "adset_id": target_adset_id,
        "status": new_status,
    }

    # Preserve creative reference
    creative = ad_data.get("creative")
    if creative:
        creative_id = creative.get("id") if isinstance(creative, dict) else creative
        params["creative"] = json.dumps({"creative_id": str(creative_id)})

    # Preserve optional fields
    if ad_data.get("bid_amount"):
        params["bid_amount"] = str(ad_data["bid_amount"])
    if ad_data.get("tracking_specs"):
        params["tracking_specs"] = json.dumps(ad_data["tracking_specs"])
    if ad_data.get("conversion_domain"):
        params["conversion_domain"] = ad_data["conversion_domain"]

    endpoint = f"{account_id}/ads"
    result = await make_api_request(endpoint, access_token, params, method="POST")

    if "error" in result:
        return {"original_id": ad_id, "new_id": None, "status": "failed", "error": result["error"]}

    return {"original_id": ad_id, "new_id": result.get("id"), "status": "created"}


async def _duplicate_single_adset(
    adset_id: str,
    target_campaign_id: str,
    account_id: str,
    name_suffix: str,
    include_ads: bool,
    new_daily_budget: Optional[int],
    new_targeting: Optional[Dict[str, Any]],
    new_status: str,
    access_token: str,
) -> Dict[str, Any]:
    """Duplicate a single ad set and optionally its ads.

    Returns a mapping with ``original_id``, ``new_id``, ``ads`` list, and
    ``status``.
    """
    # Read original adset
    adset_fields = (
        "name,campaign_id,status,daily_budget,lifetime_budget,targeting,"
        "bid_amount,bid_strategy,optimization_goal,billing_event,"
        "start_time,end_time,promoted_object,destination_type,"
        "is_dynamic_creative,frequency_control_specs,attribution_spec,"
        "pacing_type,dsa_beneficiary,dsa_payor"
    )
    adset_data = await make_api_request(adset_id, access_token, {"fields": adset_fields})
    if "error" in adset_data:
        return {
            "original_id": adset_id,
            "new_id": None,
            "status": "failed",
            "error": adset_data["error"],
            "ads": [],
        }

    # Build creation params
    params: Dict[str, Any] = {
        "name": adset_data.get("name", "Ad Set") + name_suffix,
        "campaign_id": target_campaign_id,
        "status": new_status,
    }

    # Budget: use override or original (mutually exclusive — only one allowed)
    if new_daily_budget is not None:
        params["daily_budget"] = str(new_daily_budget)
    elif adset_data.get("daily_budget"):
        params["daily_budget"] = str(adset_data["daily_budget"])
    elif adset_data.get("lifetime_budget"):
        params["lifetime_budget"] = str(adset_data["lifetime_budget"])

    # Targeting: use override or original
    targeting = new_targeting if new_targeting is not None else adset_data.get("targeting")
    if targeting:
        params["targeting"] = json.dumps(targeting)

    # Copy over standard fields if present
    optional_fields = [
        "bid_amount", "bid_strategy", "optimization_goal", "billing_event",
        "destination_type", "is_dynamic_creative",
        "dsa_beneficiary", "dsa_payor",
    ]
    for field in optional_fields:
        value = adset_data.get(field)
        if value is not None:
            if isinstance(value, bool):
                params[field] = "true" if value else "false"
            else:
                params[field] = str(value) if not isinstance(value, str) else value

    # promoted_object is a dict — JSON-encode it
    if adset_data.get("promoted_object"):
        params["promoted_object"] = json.dumps(adset_data["promoted_object"])

    # start_time / end_time: only copy if in the future
    if adset_data.get("start_time"):
        try:
            start_dt = datetime.fromisoformat(adset_data["start_time"].replace("+0000", "+00:00"))
            if start_dt > datetime.now(timezone.utc):
                params["start_time"] = adset_data["start_time"]
        except (ValueError, TypeError):
            pass
    if adset_data.get("end_time"):
        try:
            end_dt = datetime.fromisoformat(adset_data["end_time"].replace("+0000", "+00:00"))
            if end_dt > datetime.now(timezone.utc):
                params["end_time"] = adset_data["end_time"]
        except (ValueError, TypeError):
            pass

    # frequency_control_specs
    if adset_data.get("frequency_control_specs"):
        params["frequency_control_specs"] = json.dumps(adset_data["frequency_control_specs"])

    # attribution_spec
    if adset_data.get("attribution_spec"):
        params["attribution_spec"] = json.dumps(adset_data["attribution_spec"])

    # pacing_type
    if adset_data.get("pacing_type"):
        params["pacing_type"] = json.dumps(adset_data["pacing_type"])

    endpoint = f"{account_id}/adsets"
    result = await make_api_request(endpoint, access_token, params, method="POST")

    if "error" in result:
        return {
            "original_id": adset_id,
            "new_id": None,
            "status": "failed",
            "error": result["error"],
            "ads": [],
        }

    new_adset_id = result.get("id")
    ads_results: List[Dict[str, Any]] = []

    # Duplicate ads if requested
    if include_ads and new_adset_id:
        ads_data = await make_api_request(
            f"{adset_id}/ads", access_token, {"fields": "id", "limit": 100}
        )
        original_ads = ads_data.get("data", [])

        for ad in original_ads:
            ad_result = await _duplicate_single_ad(
                ad_id=ad["id"],
                target_adset_id=new_adset_id,
                account_id=account_id,
                name_suffix=name_suffix,
                new_status=new_status,
                access_token=access_token,
            )
            ads_results.append(ad_result)

    return {
        "original_id": adset_id,
        "new_id": new_adset_id,
        "status": "created",
        "ads": ads_results,
    }


# ---------------------------------------------------------------------------
# MCP Tools
# ---------------------------------------------------------------------------

@mcp_server.tool()
@meta_api_tool
async def duplicate_campaign(
    campaign_id: str,
    account_id: str,
    name_suffix: str = " - Copy",
    include_adsets: bool = True,
    include_ads: bool = True,
    new_daily_budget: Optional[int] = None,
    new_lifetime_budget: Optional[int] = None,
    new_status: str = "PAUSED",
    access_token: Optional[str] = None,
) -> str:
    """
    Duplicate a Meta Ads campaign with all its ad sets and ads.

    Creates a full copy of the specified campaign. By default, all ad sets
    and their ads are also duplicated and linked to the new campaign. The
    new campaign is created in PAUSED status unless overridden.

    Budget overrides apply to the **campaign** level only (for CBO campaigns).
    Ad-set-level budgets are preserved from the originals.

    Args:
        campaign_id: ID of the campaign to duplicate
        account_id: Ad account ID (format: act_XXXXXXXXX) where the copy will be created
        name_suffix: Suffix appended to the campaign name (default: " - Copy")
        include_adsets: Whether to also duplicate all ad sets (default: True)
        include_ads: Whether to also duplicate ads inside each ad set (default: True).
                     Only effective when include_adsets is True.
        new_daily_budget: Override daily budget for the new campaign in cents (CBO only)
        new_lifetime_budget: Override lifetime budget for the new campaign in cents (CBO only)
        new_status: Status for all new objects: ACTIVE or PAUSED (default: PAUSED)
        access_token: Meta API access token (optional)
    """
    if not campaign_id:
        return json.dumps({"error": "No campaign_id provided"}, indent=2)
    if not account_id:
        return json.dumps({"error": "No account_id provided"}, indent=2)
    if new_status not in ("ACTIVE", "PAUSED"):
        return json.dumps({"error": f"new_status must be ACTIVE or PAUSED, got '{new_status}'"}, indent=2)
    if new_daily_budget is not None and new_lifetime_budget is not None:
        return json.dumps({"error": "Cannot set both new_daily_budget and new_lifetime_budget. Choose one."}, indent=2)

    # ---------------------------------------------------------------
    # 1. Read original campaign
    # ---------------------------------------------------------------
    campaign_fields = (
        "name,objective,status,special_ad_categories,daily_budget,"
        "lifetime_budget,bid_strategy,buying_type,spend_cap,"
        "is_adset_budget_sharing_enabled"
    )
    original = await make_api_request(campaign_id, access_token, {"fields": campaign_fields})
    if "error" in original:
        return json.dumps({
            "error": "Failed to read original campaign",
            "details": original["error"],
        }, indent=2)

    # ---------------------------------------------------------------
    # 2. Create new campaign
    # ---------------------------------------------------------------
    params: Dict[str, Any] = {
        "name": original.get("name", "Campaign") + name_suffix,
        "objective": original.get("objective"),
        "status": new_status,
        "special_ad_categories": json.dumps(original.get("special_ad_categories", [])),
    }

    # Budget
    if new_daily_budget is not None:
        params["daily_budget"] = str(new_daily_budget)
    elif original.get("daily_budget"):
        params["daily_budget"] = str(original["daily_budget"])

    if new_lifetime_budget is not None:
        params["lifetime_budget"] = str(new_lifetime_budget)
    elif original.get("lifetime_budget"):
        params["lifetime_budget"] = str(original["lifetime_budget"])

    # Optional campaign-level fields
    if original.get("bid_strategy"):
        params["bid_strategy"] = original["bid_strategy"]
    if original.get("buying_type"):
        params["buying_type"] = original["buying_type"]
    if original.get("spend_cap"):
        params["spend_cap"] = str(original["spend_cap"])
    if original.get("is_adset_budget_sharing_enabled") is not None:
        params["is_adset_budget_sharing_enabled"] = (
            "true" if original["is_adset_budget_sharing_enabled"] else "false"
        )

    campaign_result = await make_api_request(
        f"{account_id}/campaigns", access_token, params, method="POST"
    )
    if "error" in campaign_result:
        return json.dumps({
            "error": "Failed to create campaign copy",
            "details": campaign_result["error"],
        }, indent=2)

    new_campaign_id = campaign_result.get("id")

    # ---------------------------------------------------------------
    # 3. Duplicate ad sets (and optionally ads)
    # ---------------------------------------------------------------
    adsets_results: List[Dict[str, Any]] = []
    total_ads_created = 0
    total_ads_failed = 0

    if include_adsets and new_campaign_id:
        adsets_data = await make_api_request(
            f"{campaign_id}/adsets", access_token, {"fields": "id", "limit": 100}
        )
        original_adsets = adsets_data.get("data", [])

        for adset in original_adsets:
            adset_result = await _duplicate_single_adset(
                adset_id=adset["id"],
                target_campaign_id=new_campaign_id,
                account_id=account_id,
                name_suffix=name_suffix,
                include_ads=include_ads,
                new_daily_budget=None,  # preserve original adset budgets
                new_targeting=None,     # preserve original targeting
                new_status=new_status,
                access_token=access_token,
            )
            adsets_results.append(adset_result)
            for ad in adset_result.get("ads", []):
                if ad.get("status") == "created":
                    total_ads_created += 1
                else:
                    total_ads_failed += 1

    # ---------------------------------------------------------------
    # 4. Build summary report
    # ---------------------------------------------------------------
    adsets_created = sum(1 for a in adsets_results if a.get("status") == "created")
    adsets_failed = sum(1 for a in adsets_results if a.get("status") == "failed")

    # Determine success: false if campaign failed or all ads failed
    all_ads_failed = include_ads and total_ads_created == 0 and total_ads_failed > 0
    is_success = bool(new_campaign_id) and not all_ads_failed

    report = {
        "success": is_success,
        "operation": "duplicate_campaign",
        "original_campaign_id": campaign_id,
        "new_campaign_id": new_campaign_id,
        "summary": {
            "campaign": "created",
            "adsets_created": adsets_created,
            "adsets_failed": adsets_failed,
            "ads_created": total_ads_created,
            "ads_failed": total_ads_failed,
        },
        "mapping": {
            "campaign": {"original": campaign_id, "new": new_campaign_id},
            "adsets": [
                {
                    "original": r["original_id"],
                    "new": r.get("new_id"),
                    "status": r["status"],
                    "error": r.get("error"),
                    "ads": r.get("ads", []),
                }
                for r in adsets_results
            ],
        },
    }

    return json.dumps(report, indent=2)


@mcp_server.tool()
@meta_api_tool
async def duplicate_adset(
    adset_id: str,
    target_campaign_id: Optional[str] = None,
    name_suffix: str = " - Copy",
    include_ads: bool = True,
    new_daily_budget: Optional[int] = None,
    new_targeting: Optional[str] = None,
    new_status: str = "PAUSED",
    access_token: Optional[str] = None,
) -> str:
    """
    Duplicate a Meta Ads ad set, optionally into a different campaign.

    Creates a copy of the specified ad set. If target_campaign_id is not
    provided, the copy is placed in the same campaign as the original.
    All ads within the ad set are also duplicated by default.

    Args:
        adset_id: ID of the ad set to duplicate
        target_campaign_id: Campaign ID for the copy. If omitted, uses the
                            original ad set's campaign.
        name_suffix: Suffix appended to the ad set name (default: " - Copy")
        include_ads: Whether to duplicate ads within the ad set (default: True)
        new_daily_budget: Override daily budget in cents for the new ad set
        new_targeting: Override targeting as a JSON string (e.g.
                       '{"geo_locations":{"countries":["BR"]}}')
        new_status: Status for new objects: ACTIVE or PAUSED (default: PAUSED)
        access_token: Meta API access token (optional)
    """
    if not adset_id:
        return json.dumps({"error": "No adset_id provided"}, indent=2)
    if new_status not in ("ACTIVE", "PAUSED"):
        return json.dumps({"error": f"new_status must be ACTIVE or PAUSED, got '{new_status}'"}, indent=2)

    # Discover account_id and campaign_id from the original
    meta_data = await make_api_request(
        adset_id, access_token, {"fields": "account_id,campaign_id"}
    )
    if "error" in meta_data:
        return json.dumps({
            "error": "Failed to read original ad set metadata",
            "details": meta_data["error"],
        }, indent=2)

    account_id = meta_data.get("account_id", "")
    if account_id and not account_id.startswith("act_"):
        account_id = f"act_{account_id}"
    if not account_id:
        return json.dumps({"error": "Could not determine account_id from ad set"}, indent=2)

    if not target_campaign_id:
        target_campaign_id = meta_data.get("campaign_id")
    if not target_campaign_id:
        return json.dumps({"error": "Could not determine target campaign_id"}, indent=2)

    # Parse new_targeting if provided as JSON string
    parsed_targeting: Optional[Dict[str, Any]] = None
    if new_targeting:
        try:
            parsed_targeting = json.loads(new_targeting) if isinstance(new_targeting, str) else new_targeting
        except json.JSONDecodeError as e:
            return json.dumps({
                "error": "Invalid new_targeting JSON",
                "details": str(e),
            }, indent=2)

    result = await _duplicate_single_adset(
        adset_id=adset_id,
        target_campaign_id=target_campaign_id,
        account_id=account_id,
        name_suffix=name_suffix,
        include_ads=include_ads,
        new_daily_budget=new_daily_budget,
        new_targeting=parsed_targeting,
        new_status=new_status,
        access_token=access_token,
    )

    ads_created = sum(1 for a in result.get("ads", []) if a.get("status") == "created")
    ads_failed = sum(1 for a in result.get("ads", []) if a.get("status") == "failed")

    report = {
        "success": result.get("status") == "created",
        "operation": "duplicate_adset",
        "original_adset_id": adset_id,
        "new_adset_id": result.get("new_id"),
        "target_campaign_id": target_campaign_id,
        "summary": {
            "adset": result.get("status"),
            "ads_created": ads_created,
            "ads_failed": ads_failed,
        },
        "mapping": {
            "adset": {"original": adset_id, "new": result.get("new_id")},
            "ads": result.get("ads", []),
        },
    }

    if result.get("error"):
        report["error"] = result["error"]

    return json.dumps(report, indent=2)


@mcp_server.tool()
@meta_api_tool
async def duplicate_ad(
    ad_id: str,
    target_adset_id: Optional[str] = None,
    name_suffix: str = " - Copy",
    new_status: str = "PAUSED",
    access_token: Optional[str] = None,
) -> str:
    """
    Duplicate a single Meta ad, optionally into a different ad set.

    Creates a copy of the specified ad using the same creative. If
    target_adset_id is not provided, the copy is placed in the same ad
    set as the original.

    Args:
        ad_id: ID of the ad to duplicate
        target_adset_id: Ad set ID for the copy. If omitted, uses the
                         original ad's ad set.
        name_suffix: Suffix appended to the ad name (default: " - Copy")
        new_status: Status for the new ad: ACTIVE or PAUSED (default: PAUSED)
        access_token: Meta API access token (optional)
    """
    if not ad_id:
        return json.dumps({"error": "No ad_id provided"}, indent=2)
    if new_status not in ("ACTIVE", "PAUSED"):
        return json.dumps({"error": f"new_status must be ACTIVE or PAUSED, got '{new_status}'"}, indent=2)

    # Discover account_id and adset_id from the original
    meta_data = await make_api_request(
        ad_id, access_token, {"fields": "account_id,adset_id"}
    )
    if "error" in meta_data:
        return json.dumps({
            "error": "Failed to read original ad metadata",
            "details": meta_data["error"],
        }, indent=2)

    account_id = meta_data.get("account_id", "")
    if account_id and not account_id.startswith("act_"):
        account_id = f"act_{account_id}"
    if not account_id:
        return json.dumps({"error": "Could not determine account_id from ad"}, indent=2)

    if not target_adset_id:
        target_adset_id = meta_data.get("adset_id")
    if not target_adset_id:
        return json.dumps({"error": "Could not determine target adset_id"}, indent=2)

    result = await _duplicate_single_ad(
        ad_id=ad_id,
        target_adset_id=target_adset_id,
        account_id=account_id,
        name_suffix=name_suffix,
        new_status=new_status,
        access_token=access_token,
    )

    report = {
        "success": result.get("status") == "created",
        "operation": "duplicate_ad",
        "original_ad_id": ad_id,
        "new_ad_id": result.get("new_id"),
        "target_adset_id": target_adset_id,
        "status": result.get("status"),
    }

    if result.get("error"):
        report["error"] = result["error"]

    return json.dumps(report, indent=2)


@mcp_server.tool()
@meta_api_tool
async def duplicate_creative(
    creative_id: str,
    account_id: str,
    name_suffix: str = " - Copy",
    new_message: Optional[str] = None,
    new_headline: Optional[str] = None,
    new_description: Optional[str] = None,
    new_cta_type: Optional[str] = None,
    new_link_url: Optional[str] = None,
    access_token: Optional[str] = None,
) -> str:
    """
    Duplicate a Meta ad creative with optional content overrides.

    Creates a copy of the specified creative. You can override the primary
    text (message), headline, description, call-to-action type, and link
    URL in the copy. Fields not overridden are preserved from the original.

    Supported CTA types include: LEARN_MORE, SHOP_NOW, SIGN_UP, SUBSCRIBE,
    DOWNLOAD, GET_QUOTE, BOOK_TRAVEL, CONTACT_US, APPLY_NOW, BUY_NOW,
    GET_OFFER, ORDER_NOW, WATCH_MORE, SEE_MENU, SEND_MESSAGE, WHATSAPP_MESSAGE.

    Args:
        creative_id: ID of the creative to duplicate
        account_id: Ad account ID (format: act_XXXXXXXXX) for the new creative
        name_suffix: Suffix appended to the creative name (default: " - Copy")
        new_message: Override the primary text / message body
        new_headline: Override the headline (link_data.name)
        new_description: Override the description (link_data.description)
        new_cta_type: Override the call-to-action type (e.g. LEARN_MORE, SHOP_NOW)
        new_link_url: Override the destination URL
        access_token: Meta API access token (optional)
    """
    if not creative_id:
        return json.dumps({"error": "No creative_id provided"}, indent=2)
    if not account_id:
        return json.dumps({"error": "No account_id provided"}, indent=2)
    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"

    # ---------------------------------------------------------------
    # 1. Read original creative
    # ---------------------------------------------------------------
    creative_fields = "name,object_story_spec,url_tags,asset_feed_spec"
    original = await make_api_request(creative_id, access_token, {"fields": creative_fields})
    if "error" in original:
        return json.dumps({
            "error": "Failed to read original creative",
            "details": original["error"],
        }, indent=2)

    # ---------------------------------------------------------------
    # 2. Build creation params
    # ---------------------------------------------------------------
    params: Dict[str, Any] = {
        "name": original.get("name", "Creative") + name_suffix,
    }

    # Copy url_tags if present
    if original.get("url_tags"):
        params["url_tags"] = original["url_tags"]

    # ---------------------------------------------------------------
    # 3. Handle object_story_spec with overrides
    # ---------------------------------------------------------------
    oss = original.get("object_story_spec")
    if oss:
        oss = dict(oss)  # shallow copy to avoid mutating original

        # Apply overrides to link_data
        link_data = oss.get("link_data")
        if link_data:
            link_data = dict(link_data)  # shallow copy

            if new_message is not None:
                link_data["message"] = new_message
            if new_headline is not None:
                link_data["name"] = new_headline
            if new_description is not None:
                link_data["description"] = new_description
            if new_link_url is not None:
                link_data["link"] = new_link_url
            if new_cta_type is not None:
                link_data["call_to_action"] = {"type": new_cta_type}

            oss["link_data"] = link_data

        # Apply overrides to video_data (for video creatives)
        video_data = oss.get("video_data")
        if video_data and not link_data:
            video_data = dict(video_data)

            if new_message is not None:
                video_data["message"] = new_message
            if new_headline is not None:
                video_data["title"] = new_headline
            if new_description is not None:
                video_data["link_description"] = new_description
            if new_link_url is not None:
                video_data["link"] = new_link_url  # or call_to_action.value.link
            if new_cta_type is not None:
                cta = video_data.get("call_to_action", {})
                cta = dict(cta)
                cta["type"] = new_cta_type
                if new_link_url is not None:
                    cta["value"] = {"link": new_link_url}
                video_data["call_to_action"] = cta

            oss["video_data"] = video_data

        params["object_story_spec"] = json.dumps(oss)

    # ---------------------------------------------------------------
    # 4. Handle asset_feed_spec (for dynamic creatives)
    # ---------------------------------------------------------------
    afs = original.get("asset_feed_spec")
    if afs:
        afs = dict(afs)

        # Override bodies (messages)
        if new_message is not None and "bodies" in afs:
            afs["bodies"] = [{"text": new_message}]

        # Override titles (headlines)
        if new_headline is not None and "titles" in afs:
            afs["titles"] = [{"text": new_headline}]

        # Override descriptions
        if new_description is not None and "descriptions" in afs:
            afs["descriptions"] = [{"text": new_description}]

        # Override link URLs
        if new_link_url is not None and "link_urls" in afs:
            afs["link_urls"] = [{"website_url": new_link_url}]

        # Override CTA
        if new_cta_type is not None and "call_to_action_types" in afs:
            afs["call_to_action_types"] = [new_cta_type]

        params["asset_feed_spec"] = json.dumps(afs)

    # ---------------------------------------------------------------
    # 5. Create the new creative
    # ---------------------------------------------------------------
    endpoint = f"{account_id}/adcreatives"
    result = await make_api_request(endpoint, access_token, params, method="POST")

    if "error" in result:
        return json.dumps({
            "error": "Failed to create creative copy",
            "details": result["error"],
        }, indent=2)

    report = {
        "success": True,
        "operation": "duplicate_creative",
        "original_creative_id": creative_id,
        "new_creative_id": result.get("id"),
        "overrides_applied": {
            "message": new_message is not None,
            "headline": new_headline is not None,
            "description": new_description is not None,
            "cta_type": new_cta_type is not None,
            "link_url": new_link_url is not None,
        },
    }

    return json.dumps(report, indent=2)
