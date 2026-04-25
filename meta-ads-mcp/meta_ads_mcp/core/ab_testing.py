"""A/B Testing (Ad Studies) management tools for Meta Ads API.

Provides tools to create, list, and retrieve results for A/B tests
(also known as Ad Studies or Split Tests) via the Meta Graph API.
Supports both SPLIT_TEST (compare ad sets/campaigns) and
SPLIT_TEST_V2 (compare creatives) test types.
"""

import json
from typing import Optional, List, Dict, Any
from .api import meta_api_tool, make_api_request
from .server import mcp_server


@mcp_server.tool()
@meta_api_tool
async def create_ab_test(
    business_id: str,
    name: str,
    cells: str,
    start_time: int,
    end_time: int,
    test_type: str = "SPLIT_TEST",
    description: Optional[str] = None,
    daily_budget: Optional[int] = None,
    access_token: Optional[str] = None,
) -> str:
    """
    Create an A/B test (Ad Study) for a business.

    A/B tests allow you to compare different ad strategies by splitting your
    audience into groups and measuring which performs better. Two test types
    are supported:

    - SPLIT_TEST: Compare different ad sets or campaigns against each other.
      Each cell references adsets or campaigns to compare.
    - SPLIT_TEST_V2: Compare different creatives (ads) against each other.
      Each cell references ads to compare. Requires daily_budget.

    Args:
        business_id: Meta Business ID that owns the ad accounts.
        name: Name for the A/B test (e.g., "Creative Test - April 2026").
        cells: JSON string with a list of test cells. Each cell must have:
            - name: Cell name (e.g., "Group A")
            - treatment_percentage: Percentage of audience for this cell (all must sum to 100)
            - adsets: List of ad set IDs (for SPLIT_TEST)
            - campaigns: List of campaign IDs (for SPLIT_TEST)
            - ads: List of ad IDs (for SPLIT_TEST_V2)
            Example for SPLIT_TEST:
                '[{"name":"Group A","treatment_percentage":50,"adsets":["123"]},
                  {"name":"Group B","treatment_percentage":50,"adsets":["456"]}]'
            Example for SPLIT_TEST_V2:
                '[{"name":"Creative A","treatment_percentage":50,"ads":["789"]},
                  {"name":"Creative B","treatment_percentage":50,"ads":["012"]}]'
        start_time: Unix timestamp (seconds) for when the test should start.
        end_time: Unix timestamp (seconds) for when the test should end.
            Minimum test duration is 1 day, recommended is 7+ days.
        test_type: Type of test. Either "SPLIT_TEST" (default) or "SPLIT_TEST_V2".
        description: Optional description for the test.
        daily_budget: Daily budget in cents. Required for SPLIT_TEST_V2.
            Example: 5000 = $50.00 (or R$50.00 depending on account currency).
        access_token: Meta API access token (optional)

    Returns:
        JSON string with the created ad study ID.

    Example:
        create_ab_test(
            business_id="1234567890",
            name="Landing Page Test",
            cells='[{"name":"Page A","treatment_percentage":50,"adsets":["111"]},{"name":"Page B","treatment_percentage":50,"adsets":["222"]}]',
            start_time=1712000000,
            end_time=1712604800,
            test_type="SPLIT_TEST"
        )
    """
    if not business_id:
        return json.dumps({"error": "business_id is required"}, indent=2)
    if not name:
        return json.dumps({"error": "name is required"}, indent=2)
    if not cells:
        return json.dumps({"error": "cells is required"}, indent=2)
    if start_time is None:
        return json.dumps({"error": "start_time is required"}, indent=2)
    if end_time is None:
        return json.dumps({"error": "end_time is required"}, indent=2)
    if end_time <= start_time:
        return json.dumps({"error": "end_time must be after start_time"}, indent=2)

    # Parse cells if it's a JSON string
    if isinstance(cells, str):
        try:
            cells_list = json.loads(cells)
        except json.JSONDecodeError:
            return json.dumps({"error": "cells must be a valid JSON string. See docstring for format."}, indent=2)
    else:
        cells_list = cells

    if not isinstance(cells_list, list) or len(cells_list) < 2:
        return json.dumps({"error": "cells must contain at least 2 test groups"}, indent=2)

    if test_type not in ("SPLIT_TEST", "SPLIT_TEST_V2"):
        return json.dumps({"error": "test_type must be 'SPLIT_TEST' or 'SPLIT_TEST_V2'"}, indent=2)

    if test_type == "SPLIT_TEST_V2" and not daily_budget:
        return json.dumps({"error": "daily_budget is required for SPLIT_TEST_V2 tests"}, indent=2)

    endpoint = f"{business_id}/ad_studies"

    params: Dict[str, Any] = {
        "name": name,
        "type": test_type,
        "start_time": str(start_time),
        "end_time": str(end_time),
        "cells": json.dumps(cells_list),
    }

    if description:
        params["description"] = description

    # SPLIT_TEST_V2 requires additional creative test configuration
    if test_type == "SPLIT_TEST_V2":
        params["creative_test_config"] = json.dumps({"daily_budget": daily_budget})
        params["cooldown_start_time"] = str(start_time)
        params["observation_end_time"] = str(end_time)

    data = await make_api_request(endpoint, access_token, params, method="POST", use_multipart=True)
    return json.dumps(data, indent=2)


@mcp_server.tool()
@meta_api_tool
async def list_ab_tests(
    business_id: str,
    access_token: Optional[str] = None,
) -> str:
    """
    List all A/B tests (Ad Studies) for a business.

    Returns all ad studies associated with the business, including their
    current status, configuration, and high-level results.

    Args:
        business_id: Meta Business ID.
        access_token: Meta API access token (optional)

    Returns:
        JSON string with list of ad studies including id, name, description,
        type, start/end times, cells configuration, and results.

    Example:
        list_ab_tests("1234567890")
    """
    if not business_id:
        return json.dumps({"error": "business_id is required"}, indent=2)

    endpoint = f"{business_id}/ad_studies"
    params = {
        "fields": "id,name,description,type,start_time,end_time,cells,results",
        "limit": 50,
    }

    data = await make_api_request(endpoint, access_token, params)
    return json.dumps(data, indent=2)


@mcp_server.tool()
@meta_api_tool
async def get_ab_test_results(
    study_id: str,
    access_token: Optional[str] = None,
) -> str:
    """
    Get detailed results for a specific A/B test (Ad Study).

    Retrieves the full configuration and results of a completed or
    in-progress A/B test, including per-cell performance breakdown
    with the ad sets, campaigns, or ads assigned to each test group.

    Args:
        study_id: The Ad Study ID to retrieve results for.
            You can get this from list_ab_tests.
        access_token: Meta API access token (optional)

    Returns:
        JSON string with the study details including cells with their
        assigned ad objects and aggregated results.

    Example:
        get_ab_test_results("123456789")
    """
    if not study_id:
        return json.dumps({"error": "study_id is required"}, indent=2)

    endpoint = f"{study_id}"
    params = {
        "fields": "id,name,description,type,start_time,end_time,cells{name,treatment_percentage,adsets,campaigns,ads},results",
    }

    data = await make_api_request(endpoint, access_token, params)
    return json.dumps(data, indent=2)
