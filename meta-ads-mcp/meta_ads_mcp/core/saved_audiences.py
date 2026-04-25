"""Saved Audiences management tools for Meta Ads API.

Saved Audiences are pre-defined targeting configurations created in the
Ads Manager UI. This module provides read-only access to list them so
their IDs can be reused in ad set targeting.
"""

import json
from typing import Optional
from .api import meta_api_tool, make_api_request
from .server import mcp_server


@mcp_server.tool()
@meta_api_tool
async def list_saved_audiences(
    account_id: str,
    access_token: Optional[str] = None,
) -> str:
    """
    List all Saved Audiences for an ad account.

    Saved Audiences are targeting configurations created and managed in the
    Meta Ads Manager UI. They combine demographics, interests, behaviors,
    and custom audiences into reusable targeting presets.

    This tool is read-only because the Meta API does not support creating or
    editing Saved Audiences programmatically. Use this to discover existing
    audiences and reuse their IDs when creating ad sets.

    To use a Saved Audience in an ad set, pass the audience ID in the
    targeting parameter: {"saved_audience_id": "<audience_id>"}.

    Args:
        account_id: Ad account ID (format: act_XXXXXXXXX)
        access_token: Meta API access token (optional)

    Returns:
        JSON string with list of saved audiences including id, name,
        targeting spec, approximate size bounds, status, and timestamps.

    Example:
        list_saved_audiences("act_123456789012345")
    """
    if not account_id:
        return json.dumps({"error": "account_id is required"}, indent=2)

    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"

    endpoint = f"{account_id}/saved_audiences"
    params = {
        "fields": "id,name,targeting,approximate_count_lower_bound,approximate_count_upper_bound,run_status,time_created,time_updated",
        "limit": 100,
    }

    data = await make_api_request(endpoint, access_token, params)
    return json.dumps(data, indent=2)
