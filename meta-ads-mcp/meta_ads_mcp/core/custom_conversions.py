"""Custom Conversions management tools for Meta Ads API.

Supports listing, creating, and deleting Custom Conversions
based on pixel events and URL rules.
"""

import json
from typing import Optional
from .api import meta_api_tool, make_api_request
from .server import mcp_server


@mcp_server.tool()
@meta_api_tool
async def list_custom_conversions(
    account_id: str,
    access_token: Optional[str] = None,
) -> str:
    """
    List all Custom Conversions for an ad account.

    Custom Conversions allow you to track and optimize for specific conversion events
    by defining rules based on URL patterns and pixel events.

    Args:
        account_id: Ad account ID (format: act_XXXXXXXXX)
        access_token: Meta API access token (optional)

    Returns:
        JSON string with list of custom conversions including id, name, description,
        pixel, event type, rule, default value, archived status, and creation time.

    Example:
        list_custom_conversions("act_123456789012345")
    """
    if not account_id:
        return json.dumps({"error": "account_id is required"}, indent=2)
    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"

    endpoint = f"{account_id}/customconversions"
    params = {
        "fields": "id,name,description,pixel,custom_event_type,rule,default_conversion_value,is_archived,creation_time",
        "limit": 100,
    }

    data = await make_api_request(endpoint, access_token, params)
    return json.dumps(data, indent=2)


@mcp_server.tool()
@meta_api_tool
async def create_custom_conversion(
    account_id: str,
    name: str,
    pixel_id: str,
    event_name: str,
    rule_url: Optional[str] = None,
    default_conversion_value: Optional[float] = None,
    description: Optional[str] = None,
    access_token: Optional[str] = None,
) -> str:
    """
    Create a Custom Conversion for an ad account.

    Custom Conversions let you define specific conversion events using a combination
    of pixel events and URL rules, enabling more granular tracking and optimization.

    Args:
        account_id: Ad account ID (format: act_XXXXXXXXX)
        name: Name for the custom conversion (e.g., "Purchase - Thank You Page")
        pixel_id: The Meta Pixel ID to associate with this conversion (required)
        event_name: Pixel event to track. Common values:
            "PURCHASE", "LEAD", "COMPLETE_REGISTRATION", "ADD_TO_CART",
            "INITIATE_CHECKOUT", "ADD_PAYMENT_INFO", "VIEW_CONTENT",
            "SEARCH", "ADD_TO_WISHLIST", "CONTACT", "SUBSCRIBE",
            "START_TRIAL", "PageView"
        rule_url: Optional URL filter rule to narrow down the conversion.
            Format: {"url":{"i_contains":"thank-you"}}
            This filters conversions to only those where the URL contains the specified string.
            Example: to track purchases only on "/thank-you" page, use:
            {"url":{"i_contains":"thank-you"}}
        default_conversion_value: Optional default monetary value for each conversion (float).
            Example: 49.90 for a R$49.90 product purchase.
        description: Optional description for the custom conversion
        access_token: Meta API access token (optional)

    Returns:
        JSON string with the created custom conversion ID.

    Example:
        create_custom_conversion(
            account_id="act_123456789012345",
            name="Purchase - Thank You Page",
            pixel_id="123456789",
            event_name="PURCHASE",
            rule_url='{"url":{"i_contains":"thank-you"}}',
            default_conversion_value=49.90,
            description="Tracks purchases completed on thank-you page"
        )
    """
    if not account_id:
        return json.dumps({"error": "account_id is required"}, indent=2)
    if not name:
        return json.dumps({"error": "name is required"}, indent=2)
    if not pixel_id:
        return json.dumps({"error": "pixel_id is required"}, indent=2)
    if not event_name:
        return json.dumps({"error": "event_name is required"}, indent=2)
    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"

    endpoint = f"{account_id}/customconversions"

    params = {
        "name": name,
        "event_source_id": pixel_id,
        "custom_event_type": event_name,
    }

    if rule_url:
        # Accept either a JSON string or pass through directly
        if isinstance(rule_url, str):
            try:
                json.loads(rule_url)
                params["rule"] = rule_url
            except json.JSONDecodeError:
                return json.dumps({"error": "rule_url must be a valid JSON string. Example: {\"url\":{\"i_contains\":\"thank-you\"}}"}, indent=2)
        else:
            params["rule"] = json.dumps(rule_url)

    if default_conversion_value is not None:
        params["default_conversion_value"] = default_conversion_value

    if description:
        params["description"] = description

    data = await make_api_request(endpoint, access_token, params, method="POST")
    return json.dumps(data, indent=2)


@mcp_server.tool()
@meta_api_tool
async def delete_custom_conversion(
    custom_conversion_id: str,
    access_token: Optional[str] = None,
) -> str:
    """
    Delete a Custom Conversion by its ID.

    This permanently removes the custom conversion. Associated data in past reports
    will still be available, but no new data will be tracked for this conversion.

    Args:
        custom_conversion_id: The ID of the custom conversion to delete.
            You can get this from list_custom_conversions.
        access_token: Meta API access token (optional)

    Returns:
        JSON string with success status ({"success": true}) or error details.

    Example:
        delete_custom_conversion("123456789")
    """
    if not custom_conversion_id:
        return json.dumps({"error": "custom_conversion_id is required"}, indent=2)

    data = await make_api_request(custom_conversion_id, access_token, method="DELETE")
    return json.dumps(data, indent=2)
