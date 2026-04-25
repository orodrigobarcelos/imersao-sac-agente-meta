"""Campaign-related functionality for Meta Ads API."""

import json
from typing import List, Optional, Dict, Any, Union
from .api import meta_api_tool, make_api_request
from .accounts import get_ad_accounts
from .server import mcp_server


@mcp_server.tool()
@meta_api_tool
async def get_campaigns(account_id: str, access_token: Optional[str] = None, limit: int = 10, status_filter: str = "", after: str = "") -> str:
    """
    Get campaigns for a Meta Ads account with optional filtering.
    
    Note: By default, the Meta API returns a subset of available fields. 
    Other fields like 'effective_status', 'special_ad_categories', 
    'lifetime_budget', 'spend_cap', 'budget_remaining', 'promoted_object', 
    'source_campaign_id', etc., might be available but require specifying them
    in the API call (currently not exposed by this tool's parameters).
    
    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        access_token: Meta API access token (optional - will use cached token if not provided)
        limit: Maximum number of campaigns to return (default: 10)
        status_filter: Filter by effective status (e.g., 'ACTIVE', 'PAUSED', 'ARCHIVED').
                       Maps to the 'effective_status' API parameter, which expects an array
                       (this function handles the required JSON formatting). Leave empty for all statuses.
        after: Pagination cursor to get the next set of results
    """
    # Require explicit account_id
    if not account_id:
        return json.dumps({"error": "No account ID specified"}, indent=2)
    
    endpoint = f"{account_id}/campaigns"
    params = {
        "fields": "id,name,objective,status,daily_budget,lifetime_budget,buying_type,start_time,stop_time,created_time,updated_time,bid_strategy,is_adset_budget_sharing_enabled,budget_remaining,spend_cap,special_ad_categories",
        "limit": limit
    }
    
    if status_filter:
        # API expects an array, encode it as a JSON string
        params["effective_status"] = json.dumps([status_filter])
    
    if after:
        params["after"] = after
    
    data = await make_api_request(endpoint, access_token, params)
    
    return json.dumps(data, indent=2)


@mcp_server.tool()
@meta_api_tool
async def get_campaign_details(campaign_id: str, access_token: Optional[str] = None) -> str:
    """
    Get detailed information about a specific campaign.

    Note: This function requests a specific set of fields ('id,name,objective,status,...'). 
    The Meta API offers many other fields for campaigns (e.g., 'effective_status', 'source_campaign_id', etc.) 
    that could be added to the 'fields' parameter in the code if needed.
    
    Args:
        campaign_id: Meta Ads campaign ID
        access_token: Meta API access token (optional - will use cached token if not provided)
    """
    if not campaign_id:
        return json.dumps({"error": "No campaign ID provided"}, indent=2)
    
    endpoint = f"{campaign_id}"
    params = {
        "fields": "id,name,objective,status,daily_budget,lifetime_budget,buying_type,start_time,stop_time,created_time,updated_time,bid_strategy,special_ad_categories,special_ad_category_country,budget_remaining,configured_status,effective_status,is_adset_budget_sharing_enabled,spend_cap,is_budget_schedule_enabled,promoted_object"
    }
    
    data = await make_api_request(endpoint, access_token, params)
    
    return json.dumps(data, indent=2)


@mcp_server.tool()
@meta_api_tool
async def create_campaign(
    account_id: str,
    name: str,
    objective: str,
    budget_mode: str = "ABO",
    access_token: Optional[str] = None,
    status: str = "PAUSED",
    special_ad_categories: Optional[List[str]] = None,
    daily_budget: Optional[int] = None,
    lifetime_budget: Optional[int] = None,
    buying_type: Optional[str] = None,
    bid_strategy: Optional[str] = None,
    bid_cap: Optional[int] = None,
    spend_cap: Optional[int] = None,
) -> str:
    """
    Create a new campaign in a Meta Ads account (v25.0).

    There are 3 budget modes that determine where the budget is managed:

    - ABO: Ad set level budgets. No budget on the campaign. Budget is set when creating ad sets.
    - ABO_SHARING: Ad set level budgets with up to 20% sharing between ad sets for better performance.
      Requires bid_strategy. Only works with daily budgets on ad sets.
    - CBO: Campaign Budget Optimization (Advantage Campaign Budget). Budget is set on the campaign
      and Meta distributes it automatically across ad sets for best results.
      Requires daily_budget or lifetime_budget and bid_strategy.

    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        name: Campaign name
        objective: Campaign objective. Must be one of:
                   OUTCOME_AWARENESS, OUTCOME_TRAFFIC, OUTCOME_ENGAGEMENT,
                   OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_APP_PROMOTION.
        budget_mode: Budget strategy for the campaign. One of:
                     'ABO' (default) - budget at ad set level, no sharing
                     'ABO_SHARING' - budget at ad set level with 20% sharing between ad sets
                     'CBO' - Advantage Campaign Budget, budget at campaign level
        access_token: Meta API access token (optional)
        status: Initial campaign status (default: PAUSED)
        special_ad_categories: List of special ad categories. Use empty list [] for none.
                               Options: EMPLOYMENT, HOUSING, CREDIT, ISSUES_ELECTIONS_POLITICS,
                               ONLINE_GAMBLING_AND_GAMING, FINANCIAL_PRODUCTS_SERVICES
        daily_budget: Daily budget in cents (e.g., 5000 = R$50.00). Only used with CBO mode.
        lifetime_budget: Lifetime budget in cents. Only used with CBO mode.
        buying_type: Buying type: 'AUCTION' (default) or 'RESERVED' (reach & frequency)
        bid_strategy: Bid strategy. Options:
                      'LOWEST_COST_WITHOUT_CAP' - automatic bidding, best for cost efficiency
                      'LOWEST_COST_WITH_BID_CAP' - manual max-cost bidding (requires bid_cap)
                      'COST_CAP' - average cost per result cap (requires bid_cap)
                      'LOWEST_COST_WITH_MIN_ROAS' - minimum ROAS bidding
                      Required for CBO and ABO_SHARING. Optional for ABO (set at ad set level).
        bid_cap: Bid cap in cents. Required when bid_strategy is LOWEST_COST_WITH_BID_CAP or COST_CAP.
        spend_cap: Total spending limit for the campaign in cents.
    """
    if not account_id:
        return json.dumps({"error": "No account ID provided"}, indent=2)
    if not name:
        return json.dumps({"error": "No campaign name provided"}, indent=2)
    if not objective:
        return json.dumps({"error": "No campaign objective provided"}, indent=2)

    # Validate objective
    valid_objectives = [
        "OUTCOME_AWARENESS", "OUTCOME_TRAFFIC", "OUTCOME_ENGAGEMENT",
        "OUTCOME_LEADS", "OUTCOME_SALES", "OUTCOME_APP_PROMOTION"
    ]
    if objective not in valid_objectives:
        return json.dumps({
            "error": f"Invalid objective '{objective}'. Must be one of: {', '.join(valid_objectives)}"
        }, indent=2)

    # Validate budget_mode
    budget_mode = budget_mode.upper()
    if budget_mode not in ["ABO", "ABO_SHARING", "CBO"]:
        return json.dumps({
            "error": f"Invalid budget_mode '{budget_mode}'. Must be one of: ABO, ABO_SHARING, CBO"
        }, indent=2)

    # Validate CBO requires budget
    if budget_mode == "CBO" and not daily_budget and not lifetime_budget:
        return json.dumps({
            "error": "CBO mode requires daily_budget or lifetime_budget at campaign level"
        }, indent=2)

    # Validate ABO_SHARING requires bid_strategy
    if budget_mode == "ABO_SHARING" and not bid_strategy:
        bid_strategy = "LOWEST_COST_WITHOUT_CAP"

    # Validate bid_strategy + bid_cap combination
    if bid_strategy and bid_strategy in ["LOWEST_COST_WITH_BID_CAP", "COST_CAP"] and bid_cap is None:
        return json.dumps({
            "error": f"bid_strategy '{bid_strategy}' requires bid_cap to be set"
        }, indent=2)

    if special_ad_categories is None:
        special_ad_categories = []

    endpoint = f"{account_id}/campaigns"

    params = {
        "name": name,
        "objective": objective,
        "status": status,
        "special_ad_categories": json.dumps(special_ad_categories),
    }

    # Budget mode configuration
    if budget_mode == "ABO":
        # ABO: no budget on campaign, no sharing
        params["is_adset_budget_sharing_enabled"] = "false"
        # bid_strategy is optional for ABO (set at ad set level)

    elif budget_mode == "ABO_SHARING":
        # ABO with sharing: no budget on campaign, sharing enabled
        params["is_adset_budget_sharing_enabled"] = "true"
        if bid_strategy:
            params["bid_strategy"] = bid_strategy
        else:
            params["bid_strategy"] = "LOWEST_COST_WITHOUT_CAP"

    elif budget_mode == "CBO":
        # CBO: budget on campaign, Meta distributes across ad sets
        if daily_budget is not None:
            params["daily_budget"] = str(daily_budget)
        if lifetime_budget is not None:
            params["lifetime_budget"] = str(lifetime_budget)
        if bid_strategy:
            params["bid_strategy"] = bid_strategy
        else:
            params["bid_strategy"] = "LOWEST_COST_WITHOUT_CAP"

    # Optional params
    if buying_type:
        params["buying_type"] = buying_type

    if bid_cap is not None:
        params["bid_cap"] = str(bid_cap)

    if spend_cap is not None:
        params["spend_cap"] = str(spend_cap)

    try:
        data = await make_api_request(endpoint, access_token, params, method="POST")
        data["budget_mode"] = budget_mode
        if budget_mode == "ABO":
            data["note"] = "Campaign created with ABO. Set daily_budget or lifetime_budget when creating ad sets."
        elif budget_mode == "ABO_SHARING":
            data["note"] = "Campaign created with ABO + 20% sharing. Set daily_budget on each ad set."
        elif budget_mode == "CBO":
            data["note"] = "Campaign created with CBO. Meta will distribute budget across ad sets automatically."
        return json.dumps(data, indent=2)
    except Exception as e:
        return json.dumps({
            "error": "Failed to create campaign",
            "details": str(e),
            "params_sent": params
        }, indent=2)


@mcp_server.tool()
@meta_api_tool
async def update_campaign(
    campaign_id: str,
    access_token: Optional[str] = None,
    name: Optional[str] = None,
    status: Optional[str] = None,
    special_ad_categories: Optional[List[str]] = None,
    daily_budget: Optional[int] = None,
    lifetime_budget: Optional[int] = None,
    bid_strategy: Optional[str] = None,
    bid_cap: Optional[int] = None,
    spend_cap: Optional[int] = None,
    is_adset_budget_sharing_enabled: Optional[bool] = None,
) -> str:
    """
    Update an existing campaign in a Meta Ads account (v25.0).

    Important limitations:
    - You CANNOT switch between daily_budget and lifetime_budget on an existing campaign.
    - You CAN add a daily_budget to an ABO campaign (converts it to CBO).
    - You CANNOT set daily_budget=0 to remove it from a CBO campaign.
    - To switch from CBO to ABO, use adset_budgets parameter (not yet supported in this tool).

    Args:
        campaign_id: Meta Ads campaign ID
        access_token: Meta API access token (optional)
        name: New campaign name
        status: New campaign status: 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'
        special_ad_categories: List of special ad categories
        daily_budget: New daily budget in cents (e.g., 5000 = R$50.00). For CBO campaigns only.
        lifetime_budget: New lifetime budget in cents. For CBO campaigns only.
        bid_strategy: New bid strategy: LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP,
                      COST_CAP, LOWEST_COST_WITH_MIN_ROAS
        bid_cap: Bid cap in cents. Used with adset_bid_amounts when switching bid strategies.
        spend_cap: Total spending limit in cents. Set to 922337203685478 to remove.
        is_adset_budget_sharing_enabled: Enable/disable 20% budget sharing between ad sets.
    """
    if not campaign_id:
        return json.dumps({"error": "No campaign ID provided"}, indent=2)

    endpoint = f"{campaign_id}"
    params = {}

    if name is not None:
        params["name"] = name
    if status is not None:
        params["status"] = status
    if special_ad_categories is not None:
        params["special_ad_categories"] = json.dumps(special_ad_categories)
    if daily_budget is not None:
        params["daily_budget"] = str(daily_budget)
    if lifetime_budget is not None:
        params["lifetime_budget"] = str(lifetime_budget)
    if bid_strategy is not None:
        params["bid_strategy"] = bid_strategy
    if bid_cap is not None:
        params["bid_cap"] = str(bid_cap)
    if spend_cap is not None:
        params["spend_cap"] = str(spend_cap)
    if is_adset_budget_sharing_enabled is not None:
        params["is_adset_budget_sharing_enabled"] = "true" if is_adset_budget_sharing_enabled else "false"

    if not params:
        return json.dumps({"error": "No update parameters provided"}, indent=2)

    try:
        data = await make_api_request(endpoint, access_token, params, method="POST")
        return json.dumps(data, indent=2)
    except Exception as e:
        return json.dumps({
            "error": f"Failed to update campaign {campaign_id}",
            "details": str(e),
            "params_sent": params
        }, indent=2)