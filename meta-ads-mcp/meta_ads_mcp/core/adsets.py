"""Ad Set-related functionality for Meta Ads API."""

import json
from typing import Optional, Dict, Any, List
from .api import meta_api_tool, make_api_request
from .accounts import get_ad_accounts
from .server import mcp_server


@mcp_server.tool()
@meta_api_tool
async def get_adsets(account_id: str, access_token: Optional[str] = None, limit: int = 10, campaign_id: str = "") -> str:
    """
    Get ad sets for a Meta Ads account with optional filtering by campaign.
    
    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        access_token: Meta API access token (optional - will use cached token if not provided)
        limit: Maximum number of ad sets to return (default: 10)
        campaign_id: Optional campaign ID to filter by
    """
    # Require explicit account_id
    if not account_id:
        return json.dumps({"error": "No account ID specified"}, indent=2)
    
    # Change endpoint based on whether campaign_id is provided
    if campaign_id:
        endpoint = f"{campaign_id}/adsets"
        params = {
            "fields": "id,name,campaign_id,status,daily_budget,lifetime_budget,targeting,bid_amount,bid_strategy,optimization_goal,billing_event,start_time,end_time,created_time,updated_time,is_dynamic_creative,frequency_control_specs{event,interval_days,max_frequency},promoted_object,destination_type,effective_status",
            "limit": limit
        }
    else:
        # Use account endpoint if no campaign_id is given
        endpoint = f"{account_id}/adsets"
        params = {
            "fields": "id,name,campaign_id,status,daily_budget,lifetime_budget,targeting,bid_amount,bid_strategy,optimization_goal,billing_event,start_time,end_time,created_time,updated_time,is_dynamic_creative,frequency_control_specs{event,interval_days,max_frequency},promoted_object,destination_type,effective_status",
            "limit": limit
        }
        # Note: Removed the attempt to add campaign_id to params for the account endpoint case, 
        # as it was ineffective and the logic now uses the correct endpoint for campaign filtering.

    data = await make_api_request(endpoint, access_token, params)
    
    return json.dumps(data, indent=2)


@mcp_server.tool()
@meta_api_tool
async def get_adset_details(adset_id: str, access_token: Optional[str] = None) -> str:
    """
    Get detailed information about a specific ad set.
    
    Args:
        adset_id: Meta Ads ad set ID
        access_token: Meta API access token (optional - will use cached token if not provided)
    
    Example:
        To call this function through MCP, pass the adset_id as the first argument:
        {
            "args": "YOUR_ADSET_ID"
        }
    """
    if not adset_id:
        return json.dumps({"error": "No ad set ID provided"}, indent=2)
    
    endpoint = f"{adset_id}"
    # Explicitly prioritize frequency_control_specs in the fields request
    params = {
        "fields": "id,name,campaign_id,status,frequency_control_specs{event,interval_days,max_frequency},daily_budget,lifetime_budget,targeting,bid_amount,bid_strategy,optimization_goal,billing_event,start_time,end_time,created_time,updated_time,attribution_spec,destination_type,promoted_object,pacing_type,budget_remaining,dsa_beneficiary,dsa_payor,is_dynamic_creative,effective_status"
    }
    
    data = await make_api_request(endpoint, access_token, params)
    
    # For debugging - check if frequency_control_specs was returned
    if 'frequency_control_specs' not in data:
        data['_meta'] = {
            'note': 'No frequency_control_specs field was returned by the API. This means either no frequency caps are set or the API did not include this field in the response.'
        }
    
    return json.dumps(data, indent=2)


@mcp_server.tool()
@meta_api_tool
async def create_adset(
    account_id: str,
    campaign_id: str,
    name: str,
    optimization_goal: str,
    billing_event: str = "IMPRESSIONS",
    status: str = "PAUSED",
    daily_budget: Optional[int] = None,
    lifetime_budget: Optional[int] = None,
    targeting: Optional[Dict[str, Any]] = None,
    bid_amount: Optional[int] = None,
    bid_strategy: Optional[str] = None,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    dsa_beneficiary: Optional[str] = None,
    dsa_payor: Optional[str] = None,
    promoted_object: Optional[Dict[str, Any]] = None,
    destination_type: Optional[str] = None,
    is_dynamic_creative: Optional[bool] = None,
    access_token: Optional[str] = None
) -> str:
    """
    Create a new ad set in a Meta Ads account (v25.0).

    Ad sets define targeting, budget (for ABO campaigns), optimization goal, and billing.
    The ad set MUST belong to a campaign (campaign_id is required).

    For CBO campaigns: do NOT pass daily_budget/lifetime_budget (budget is on the campaign).
    For ABO campaigns: you MUST pass daily_budget or lifetime_budget.

    Important CBO rule: all ad sets in a CBO campaign with LOWEST_COST_WITHOUT_CAP must
    share the SAME optimization_goal. To use different optimization_goals, create separate campaigns.

    Tested valid combinations per objective (v25.0):

    OUTCOME_SALES:
      - OFFSITE_CONVERSIONS + {pixel_id, custom_event_type: PURCHASE/ADD_TO_CART/INITIATED_CHECKOUT/
        CONTENT_VIEW/COMPLETE_REGISTRATION/ADD_PAYMENT_INFO/ADD_TO_WISHLIST/SEARCH/SUBSCRIBE/
        START_TRIAL/CONTACT/CUSTOMIZE_PRODUCT/DONATE/FIND_LOCATION/SCHEDULE/SUBMIT_APPLICATION}
        (NOT valid: LEAD — use OUTCOME_LEADS)
      - CONVERSATIONS + destination_type=MESSENGER + {page_id}
      - CONVERSATIONS + destination_type=INSTAGRAM_DIRECT + {page_id}
      - CONVERSATIONS + destination_type=WHATSAPP + {page_id} (requires WhatsApp Business Platform API)
      - LANDING_PAGE_VIEWS + {pixel_id, custom_event_type}
      - LINK_CLICKS + {pixel_id, custom_event_type}
      - IMPRESSIONS + {pixel_id, custom_event_type}
      - VALUE + {pixel_id, custom_event_type: PURCHASE} (requires LOWEST_COST_WITH_MIN_ROAS)

    OUTCOME_TRAFFIC:
      - LINK_CLICKS (no promoted_object needed)
      - LANDING_PAGE_VIEWS (no promoted_object needed)
      - CONVERSATIONS + destination_type=MESSENGER/INSTAGRAM_DIRECT + {page_id}
      - IMPRESSIONS (no promoted_object needed)

    OUTCOME_LEADS:
      - OFFSITE_CONVERSIONS + {pixel_id, custom_event_type: LEAD/COMPLETE_REGISTRATION}
      - LEAD_GENERATION + destination_type=ON_AD + {page_id} (native instant form)
        IMPORTANT: Token MUST have pages_manage_metadata + leads_retrieval + pages_manage_ads permissions.
        Page must accept Lead Ads TOS at https://www.facebook.com/ads/leadgen/tos/?page_id=PAGE_ID
        Accept TOS as your PERSONAL profile, not as the page.
      (NOT valid: CONVERSATIONS — use OUTCOME_TRAFFIC or OUTCOME_ENGAGEMENT)

    OUTCOME_AWARENESS:
      - REACH (no promoted_object needed)
      - IMPRESSIONS (no promoted_object needed)

    OUTCOME_ENGAGEMENT:
      - POST_ENGAGEMENT + destination_type=ON_POST + {page_id} (required for ad creation)
      - THRUPLAY + destination_type=ON_VIDEO + {page_id} (required for ad creation)
      - CONVERSATIONS + destination_type=MESSENGER + {page_id}
      - REACH (no promoted_object needed)
      - IMPRESSIONS (no promoted_object needed)

    OUTCOME_APP_PROMOTION:
      - APP_INSTALLS + {application_id, object_store_url} (requires published app)

    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        campaign_id: Campaign ID this ad set belongs to (REQUIRED)
        name: Ad set name
        optimization_goal: What to optimize for. Common values:
            OFFSITE_CONVERSIONS - website conversions via pixel
            CONVERSATIONS - messaging (Messenger/Instagram DM/WhatsApp)
            LINK_CLICKS - clicks to website
            LANDING_PAGE_VIEWS - full page loads (not just clicks)
            IMPRESSIONS - maximum reach/impressions
            VALUE - optimize for purchase value (requires MIN_ROAS bid strategy)
            LEAD_GENERATION - leads via instant forms
            REACH - unique people reached
            APP_INSTALLS - mobile app installs
        billing_event: How you're charged. Default: IMPRESSIONS (recommended for most cases)
        status: Initial status: PAUSED (default) or ACTIVE
        daily_budget: Daily budget in cents (e.g., 5000 = R$50). Only for ABO campaigns.
        lifetime_budget: Lifetime budget in cents. Only for ABO campaigns. Requires end_time.
        targeting: Targeting specs. Minimum required: {"geo_locations": {"countries": ["BR"]}}
            Demographics: age_min, age_max, genders ([1]=male, [2]=female, [1,2]=both)
            Location: geo_locations.countries, geo_locations.regions, geo_locations.cities
            Audiences: custom_audiences ([{id}]), excluded_custom_audiences ([{id}])
            Interests: flexible_spec ([{interests: [{id, name}]}]) — requires targeting_automation.advantage_audience
            Advantage+: targeting_automation.advantage_audience (0=manual, 1=Meta decides)
            Placements (inside targeting):
              publisher_platforms: ["facebook","instagram","threads","messenger","audience_network"]
              device_platforms: ["mobile","desktop"]
              facebook_positions: ["feed","right_hand_column","marketplace","video_feeds","story",
                "search","instream_video","facebook_reels","facebook_reels_overlay","profile_feed","notification"]
              instagram_positions: ["stream","story","explore","explore_home","reels",
                "profile_feed","ig_search","profile_reels"]
              threads_positions: ["threads_stream"] (requires instagram stream)
              messenger_positions: ["story","sponsored_messages"]
              whatsapp_positions: ["status"] (requires instagram story + WhatsApp Business Platform)
            Placement rules:
              - If no placement fields: automatic (Meta decides all placements)
              - audience_network requires facebook feed
              - stories require device_platforms: mobile
              - threads requires instagram stream
            Examples:
              Only Instagram: {"publisher_platforms":["instagram"],"instagram_positions":["stream","story","reels"]}
              Only Reels: {"publisher_platforms":["facebook","instagram"],"facebook_positions":["facebook_reels"],"instagram_positions":["reels"]}
              Only Mobile: {"device_platforms":["mobile"]}
        bid_amount: Bid amount in cents. Required for LOWEST_COST_WITH_BID_CAP or COST_CAP strategies.
        bid_strategy: Bid strategy at ad set level (only for ABO campaigns).
        start_time: Start time ISO 8601 (e.g., '2026-04-01T00:00:00-0300')
        end_time: End time ISO 8601. Required if using lifetime_budget.
        dsa_beneficiary: DSA beneficiary name (required for EU-targeted ads)
        dsa_payor: DSA payor name (required for EU-targeted ads)
        promoted_object: What the ad set promotes. Examples:
            Website conversions: {"pixel_id": "123", "custom_event_type": "PURCHASE"}
            Messenger/WhatsApp/IG: {"page_id": "123"}
            App installs: {"application_id": "123", "object_store_url": "https://..."}
            Lead forms: {"page_id": "123"}
        destination_type: Where users go after clicking. Values:
            WEBSITE - landing page (default for conversions)
            MESSENGER - Facebook Messenger
            INSTAGRAM_DIRECT - Instagram DMs
            WHATSAPP - WhatsApp (requires WhatsApp Business Platform API)
            ON_AD - interaction within the ad (lead forms)
            APP - mobile app
        is_dynamic_creative: Enable Advantage+ Creative (dynamic creative optimization)
        access_token: Meta API access token (optional)
    """
    if not account_id:
        return json.dumps({"error": "No account ID provided"}, indent=2)
    if not campaign_id:
        return json.dumps({"error": "No campaign ID provided"}, indent=2)
    if not name:
        return json.dumps({"error": "No ad set name provided"}, indent=2)
    if not optimization_goal:
        return json.dumps({"error": "No optimization goal provided"}, indent=2)

    # Validate promoted_object is required for most optimization goals
    goals_requiring_promoted_object = [
        "OFFSITE_CONVERSIONS", "VALUE", "CONVERSATIONS",
        "APP_INSTALLS", "LEAD_GENERATION"
    ]
    if optimization_goal in goals_requiring_promoted_object and not promoted_object:
        return json.dumps({
            "error": f"promoted_object is required for optimization_goal '{optimization_goal}'",
            "examples": {
                "OFFSITE_CONVERSIONS": {"pixel_id": "YOUR_PIXEL_ID", "custom_event_type": "PURCHASE"},
                "CONVERSATIONS": {"page_id": "YOUR_PAGE_ID"},
                "APP_INSTALLS": {"application_id": "YOUR_APP_ID", "object_store_url": "https://..."},
                "LEAD_GENERATION": {"page_id": "YOUR_PAGE_ID"},
            }
        }, indent=2)

    # LEAD_GENERATION requires specific destination_type and permissions
    if optimization_goal == "LEAD_GENERATION":
        if not destination_type:
            destination_type = "ON_AD"
        if promoted_object and "page_id" not in promoted_object:
            return json.dumps({
                "error": "LEAD_GENERATION requires promoted_object with page_id",
                "example": {"page_id": "YOUR_PAGE_ID"}
            }, indent=2)

    # Validate bid_strategy + bid_amount
    strategies_requiring_bid = ["LOWEST_COST_WITH_BID_CAP", "COST_CAP"]
    if bid_strategy and bid_strategy in strategies_requiring_bid and bid_amount is None:
        return json.dumps({
            "error": f"bid_strategy '{bid_strategy}' requires bid_amount to be set"
        }, indent=2)

    # Check parent campaign bid_strategy for compatibility
    if bid_amount is None:
        try:
            camp_data = await make_api_request(campaign_id, access_token, {"fields": "bid_strategy,name,daily_budget"})
            camp_bid = camp_data.get("bid_strategy", "")
            if camp_bid in strategies_requiring_bid:
                return json.dumps({
                    "error": f"Campaign '{camp_data.get('name', campaign_id)}' uses bid_strategy '{camp_bid}' which requires bid_amount on ad sets.",
                    "solution": "Provide bid_amount parameter, or create a new campaign with budget_mode='ABO' and LOWEST_COST_WITHOUT_CAP.",
                }, indent=2)
        except Exception:
            pass

    # Default targeting if not provided
    if not targeting:
        targeting = {"geo_locations": {"countries": ["BR"]}}

    # v25 requires targeting_automation.advantage_audience when using flexible_spec (interests)
    if "flexible_spec" in targeting and "targeting_automation" not in targeting:
        targeting["targeting_automation"] = {"advantage_audience": 0}

    # Auto-validate interests before creating adset
    if "flexible_spec" in targeting:
        interest_ids = []
        for spec in targeting["flexible_spec"]:
            for interest in spec.get("interests", []):
                if "id" in interest:
                    interest_ids.append(str(interest["id"]))
        if interest_ids:
            try:
                validate_params = {"type": "adinterestvalid", "interest_fbid_list": json.dumps(interest_ids)}
                validation = await make_api_request("search", access_token, validate_params)
                invalid = [i["name"] for i in validation.get("data", []) if not i.get("valid")]
                if invalid:
                    return json.dumps({
                        "error": "Invalid interests detected. These interests no longer exist or were removed by Meta.",
                        "invalid_interests": invalid,
                        "solution": "Use search_interests to find valid alternatives, then retry."
                    }, indent=2)
            except Exception:
                pass  # Don't block creation if validation fails

    endpoint = f"{account_id}/adsets"

    params = {
        "name": name,
        "campaign_id": campaign_id,
        "status": status,
        "optimization_goal": optimization_goal,
        "billing_event": billing_event,
        "targeting": json.dumps(targeting),
    }

    # Budget (only for ABO campaigns)
    if daily_budget is not None:
        params["daily_budget"] = str(daily_budget)
    if lifetime_budget is not None:
        params["lifetime_budget"] = str(lifetime_budget)

    # Bid
    if bid_amount is not None:
        params["bid_amount"] = str(bid_amount)
    if bid_strategy:
        params["bid_strategy"] = bid_strategy

    # Scheduling
    if start_time:
        params["start_time"] = start_time
    if end_time:
        params["end_time"] = end_time

    # DSA compliance (EU)
    if dsa_beneficiary:
        params["dsa_beneficiary"] = dsa_beneficiary
    if dsa_payor:
        params["dsa_payor"] = dsa_payor

    # Promoted object
    if promoted_object:
        params["promoted_object"] = json.dumps(promoted_object)

    # Destination type
    if destination_type:
        params["destination_type"] = destination_type

    # Dynamic creative
    if is_dynamic_creative is not None:
        params["is_dynamic_creative"] = "true" if is_dynamic_creative else "false"

    try:
        data = await make_api_request(endpoint, access_token, params, method="POST")
        return json.dumps(data, indent=2)
    except Exception as e:
        error_msg = str(e)
        result = {
            "error": "Failed to create ad set",
            "details": error_msg,
            "params_sent": params
        }
        # Enhanced error messages for common issues
        if "1815089" in error_msg or "Termos de Servi" in error_msg or "Terms of Service" in error_msg:
            page_id = promoted_object.get("page_id", "PAGE_ID") if promoted_object else "PAGE_ID"
            result["solution"] = (
                f"Lead Ads TOS not accepted. Fix: "
                f"1) Token needs permissions: pages_manage_metadata, leads_retrieval, pages_manage_ads. "
                f"2) Accept TOS as your PERSONAL profile (not as page) at: "
                f"https://www.facebook.com/ads/leadgen/tos/?page_id={page_id}"
            )
        elif "1885760" in error_msg or "otimização para seleções" in error_msg:
            result["solution"] = (
                "All ad sets in a CBO campaign with LOWEST_COST_WITHOUT_CAP must share the SAME "
                "optimization_goal. Create a separate campaign for this optimization_goal."
            )
        elif "2446886" in error_msg or "WhatsApp Business" in error_msg:
            result["solution"] = (
                "WhatsApp ads require WhatsApp Business Platform API (not the app). "
                "Configure at: business.facebook.com > Settings > WhatsApp Accounts"
            )
        return json.dumps(result, indent=2)


@mcp_server.tool()
@meta_api_tool
async def update_adset(adset_id: str, name: Optional[str] = None, frequency_control_specs: Optional[List[Dict[str, Any]]] = None, bid_strategy: Optional[str] = None,
                        bid_amount: Optional[int] = None, status: Optional[str] = None, targeting: Optional[Dict[str, Any]] = None,
                        optimization_goal: Optional[str] = None, daily_budget: Optional[int] = None, lifetime_budget: Optional[int] = None,
                        is_dynamic_creative: Optional[bool] = None,
                        access_token: Optional[str] = None) -> str:
    """
    Update an ad set with new settings (v25.0).

    Important limitations:
    - You CANNOT edit pixel_id, custom_event_type, or optimization_goal after the ad set is published.
      To change these, create a new ad set.
    - You CANNOT edit frequency_control_specs after the campaign has started.
    - You CAN always edit: name, targeting, status, daily_budget, lifetime_budget, bid_amount, bid_strategy.

    Args:
        adset_id: Meta Ads ad set ID
        frequency_control_specs: List of frequency control specifications 
                                 (e.g. [{"event": "IMPRESSIONS", "interval_days": 7, "max_frequency": 3}])
        bid_strategy: Bid strategy (e.g., 'LOWEST_COST_WITH_BID_CAP')
        bid_amount: Bid amount in account currency (in cents for USD)
        status: Update ad set status (ACTIVE, PAUSED, etc.)
        targeting: Complete targeting specifications (will replace existing targeting)
                  (e.g. {"targeting_automation":{"advantage_audience":1}, "geo_locations": {"countries": ["US"]}})
        optimization_goal: Conversion optimization goal (e.g., 'LINK_CLICKS', 'CONVERSIONS', 'APP_INSTALLS', etc.)
        daily_budget: Daily budget in account currency (in cents) as a string
        lifetime_budget: Lifetime budget in account currency (in cents) as a string
        is_dynamic_creative: Enable/disable Dynamic Creative for this ad set.
        access_token: Meta API access token (optional - will use cached token if not provided)
    """
    if not adset_id:
        return json.dumps({"error": "No ad set ID provided"}, indent=2)
    
    params = {}

    if name is not None:
        params['name'] = name

    if frequency_control_specs is not None:
        params['frequency_control_specs'] = frequency_control_specs
    
    if bid_strategy is not None:
        params['bid_strategy'] = bid_strategy
        
    if bid_amount is not None:
        params['bid_amount'] = str(bid_amount)
        
    if status is not None:
        params['status'] = status
        
    if optimization_goal is not None:
        params['optimization_goal'] = optimization_goal
        
    if targeting is not None:
        # Ensure proper JSON encoding for targeting
        if isinstance(targeting, dict):
            params['targeting'] = json.dumps(targeting)
        else:
            params['targeting'] = targeting  # Already a string
    
    # Add budget parameters if provided
    if daily_budget is not None:
        params['daily_budget'] = str(daily_budget)
    
    if lifetime_budget is not None:
        params['lifetime_budget'] = str(lifetime_budget)
    
    if is_dynamic_creative is not None:
        params['is_dynamic_creative'] = "true" if bool(is_dynamic_creative) else "false"
    
    if not params:
        return json.dumps({"error": "No update parameters provided"}, indent=2)

    endpoint = f"{adset_id}"
    
    try:
        # Use POST method for updates as per Meta API documentation
        data = await make_api_request(endpoint, access_token, params, method="POST")
        return json.dumps(data, indent=2)
    except Exception as e:
        error_msg = str(e)
        # Include adset_id in error for better context
        return json.dumps({
            "error": f"Failed to update ad set {adset_id}",
            "details": error_msg,
            "params_sent": params
        }, indent=2) 