"""Insights and Reporting functionality for Meta Ads API."""

import json
from typing import Optional, Union, Dict, List
from .api import meta_api_tool, make_api_request
from .server import mcp_server


@mcp_server.tool()
@meta_api_tool
async def get_insights(object_id: str, access_token: Optional[str] = None,
                      time_range: Union[str, Dict[str, str]] = "last_30d",
                      fields: Optional[str] = None,
                      breakdown: str = "",
                      action_breakdowns: Optional[str] = None,
                      level: str = "",
                      time_increment: Optional[str] = None,
                      limit: int = 100,
                      sort: Optional[str] = None,
                      filtering: Optional[str] = None) -> str:
    """
    Get performance insights for a campaign, ad set, ad or account (v25.0).

    Supports all Meta Ads objects: account (act_XXX), campaign, adset, or ad ID.
    Pass any object ID directly — the endpoint is always {object_id}/insights.

    Args:
        object_id: ID of the campaign, ad set, ad or account (act_XXX).
            Examples: "act_123456789012345", "23853784113320682" (campaign),
            "23853784113620682" (adset), "23853784113950682" (ad).
        access_token: Meta API access token (optional)
        time_range: Date range. Either a preset string or dict {"since":"YYYY-MM-DD","until":"YYYY-MM-DD"}.
            Presets: today, yesterday, this_month, last_month, this_quarter, maximum,
            last_3d, last_7d, last_14d, last_28d, last_30d (default), last_90d,
            last_week_mon_sun, last_week_sun_sat, last_quarter, last_year,
            this_week_mon_today, this_week_sun_today, this_year.
            NOTE: Use "maximum" to get all historical data. "last_30d" may return empty if no recent spend.
        fields: Comma-separated metrics to retrieve. Default includes main metrics.
            Common: impressions, clicks, spend, cpc, cpm, ctr, reach, frequency,
            actions, action_values, conversions, cost_per_action_type, unique_clicks,
            purchase_roas, website_purchase_roas, cost_per_unique_click,
            video_p25_watched_actions, video_p50_watched_actions, video_p75_watched_actions,
            video_p95_watched_actions, video_p100_watched_actions, video_thruplay_watched_actions.
            NOTE: purchase_roas/website_purchase_roas only return data if the account has a purchase pixel configured.
        breakdown: Group results by dimension. Common:
            Demographic: age, gender, country, region
            Platform: device_platform (desktop/mobile_app/mobile_web), publisher_platform, platform_position
            Combined: "age,gender" or "publisher_platform,platform_position"
        action_breakdowns: How to break down action results. Options:
            action_type (link_click, landing_page_view, comment, video_view, etc.),
            action_device, conversion_destination, action_destination
        level: Aggregation level: ad, adset, campaign, account.
            If empty, returns data for the object itself.
            Example: pass a campaign ID with level="adset" to see all adsets in that campaign.
        time_increment: Split results by time period.
            "1" = daily (one row per day), "7" = weekly, "monthly" = monthly, "all_days" = single result (default)
        limit: Max results per page (default: 100)
        sort: Sort field + direction. Example: "spend_descending", "impressions_ascending"
        filtering: JSON array of filters. Example: [{"field":"spend","operator":"GREATER_THAN","value":"0"}]
            Operators: GREATER_THAN, LESS_THAN, EQUAL, NOT_EQUAL, IN, NOT_IN, CONTAIN, NOT_CONTAIN

    NOTE: Breakdowns, time_increment, sort, and filtering can all be combined in a single request.
    NOTE: Rate limit for Ads Insights is per USER (not per app). Resets in ~1 hour.
    NOTE: To see Threads metrics separately, use breakdown="publisher_platform,platform_position".
        Threads data appears as publisher_platform="threads" and platform_position="threads_feed".
    NOTE: For UTM tracking on Threads placements, use url_tags in the ad creative with utm_source=threads.
    """
    if not object_id:
        return json.dumps({"error": "No object ID provided"}, indent=2)

    endpoint = f"{object_id}/insights"

    if not fields:
        fields = "account_id,account_name,campaign_id,campaign_name,adset_id,adset_name,ad_id,ad_name,impressions,clicks,spend,cpc,cpm,ctr,reach,frequency,actions,action_values,conversions,unique_clicks,cost_per_action_type"

    params = {
        "fields": fields,
        "limit": limit,
    }

    if level:
        params["level"] = level

    # Handle time range
    if isinstance(time_range, dict):
        if "since" in time_range and "until" in time_range:
            params["time_range"] = json.dumps(time_range)
        else:
            return json.dumps({"error": "Custom time_range must contain both 'since' and 'until' keys in YYYY-MM-DD format"}, indent=2)
    else:
        params["date_preset"] = time_range

    if breakdown:
        params["breakdowns"] = breakdown

    if action_breakdowns:
        params["action_breakdowns"] = action_breakdowns

    if time_increment:
        params["time_increment"] = time_increment

    if sort:
        params["sort"] = [sort]

    if filtering:
        if isinstance(filtering, str):
            try:
                params["filtering"] = json.loads(filtering)
            except json.JSONDecodeError:
                return json.dumps({"error": "filtering must be a valid JSON array. Example: [{\"field\":\"spend\",\"operator\":\"GREATER_THAN\",\"value\":\"0\"}]"}, indent=2)
        else:
            params["filtering"] = filtering

    data = await make_api_request(endpoint, access_token, params)

    return json.dumps(data, indent=2)


@mcp_server.tool()
@meta_api_tool
async def bulk_get_insights(
    account_ids: List[str],
    access_token: Optional[str] = None,
    time_range: Union[str, Dict[str, str]] = "last_30d",
    fields: Optional[str] = None,
    level: str = "account",
) -> str:
    """
    Get performance insights for multiple ad accounts at once.

    Fetches insights from each account and returns aggregated results.
    If one account fails, the others still return data (partial results).

    Args:
        account_ids: List of ad account IDs (format: ["act_XXXXXXXXX", "act_YYYYYYYYY"]).
        access_token: Meta API access token (optional)
        time_range: Date range. Either a preset string or dict {"since":"YYYY-MM-DD","until":"YYYY-MM-DD"}.
            Presets: today, yesterday, this_month, last_month, this_quarter, maximum,
            last_3d, last_7d, last_14d, last_28d, last_30d (default), last_90d,
            last_week_mon_sun, last_week_sun_sat, last_quarter, last_year,
            this_week_mon_today, this_week_sun_today, this_year.
        fields: Comma-separated metrics to retrieve. Default:
            account_id, account_name, impressions, clicks, spend, cpc, cpm, ctr,
            reach, frequency, actions.
        level: Aggregation level: ad, adset, campaign, account (default: "account").

    Returns:
        JSON string with results per account, including data and any errors.

    Example:
        bulk_get_insights(
            account_ids=["act_111111111", "act_222222222"],
            time_range="last_7d",
            fields="impressions,clicks,spend,cpc",
            level="campaign"
        )

    NOTE: Errors for individual accounts are included in the response under "errors".
        Successfully retrieved accounts appear under "results".
    NOTE: Rate limits apply per user. Querying many accounts may hit rate limits faster.
    """
    if not account_ids:
        return json.dumps({"error": "account_ids list is required and cannot be empty"}, indent=2)

    if not fields:
        fields = "account_id,account_name,impressions,clicks,spend,cpc,cpm,ctr,reach,frequency,actions"

    # Validate time_range once before the loop
    time_params = {}
    if isinstance(time_range, dict):
        if "since" in time_range and "until" in time_range:
            time_params["time_range"] = json.dumps(time_range)
        else:
            return json.dumps({"error": "Custom time_range must contain both 'since' and 'until' keys in YYYY-MM-DD format"}, indent=2)
    else:
        time_params["date_preset"] = time_range

    results = []
    errors = []

    for account_id in account_ids:
        try:
            endpoint = f"{account_id}/insights"
            params = {
                "fields": fields,
                "level": level,
                **time_params,
            }

            data = await make_api_request(endpoint, access_token, params)

            if "error" in data:
                errors.append({
                    "account_id": account_id,
                    "error": data["error"],
                })
            else:
                results.append({
                    "account_id": account_id,
                    "data": data.get("data", []),
                })
        except Exception as e:
            errors.append({
                "account_id": account_id,
                "error": str(e),
            })

    response = {
        "results": results,
        "total_accounts_requested": len(account_ids),
        "total_accounts_success": len(results),
        "total_accounts_error": len(errors),
    }

    if errors:
        response["errors"] = errors

    return json.dumps(response, indent=2)

 