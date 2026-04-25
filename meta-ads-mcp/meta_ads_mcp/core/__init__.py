"""Core functionality for Meta Ads API MCP package."""

from .server import mcp_server
from .accounts import get_ad_accounts, get_account_info, get_pixels, get_account_videos, create_pixel
from .campaigns import get_campaigns, get_campaign_details, create_campaign, update_campaign
from .adsets import get_adsets, get_adset_details, update_adset
from .ads import get_ads, get_ad_details, get_ad_creatives, get_ad_image, update_ad, upload_ad_video
from .insights import get_insights, bulk_get_insights
from .custom_conversions import list_custom_conversions, create_custom_conversion, delete_custom_conversion
from . import authentication  # Import module to register conditional auth tools
from .server import login_cli, main
from .auth import login
from . import ads_library  # Import module to register conditional tools
from .budget_schedules import create_budget_schedule
from .targeting import search_interests, get_interest_suggestions, estimate_audience_size, search_behaviors, search_demographics, search_geo_locations
from .custom_audiences import create_website_custom_audience, create_video_custom_audience, create_page_custom_audience, create_instagram_custom_audience, create_leadform_custom_audience, list_custom_audiences, create_lookalike_audience
from .duplication import duplicate_campaign, duplicate_adset, duplicate_ad, duplicate_creative
from .saved_audiences import list_saved_audiences
from .ab_testing import create_ab_test, list_ab_tests, get_ab_test_results

__all__ = [
    'mcp_server',
    'get_ad_accounts',
    'get_account_info',
    'get_pixels',
    'get_account_videos',
    'get_campaigns',
    'get_campaign_details',
    'create_campaign',
    'update_campaign',
    'get_adsets',
    'get_adset_details',
    'update_adset',
    'get_ads',
    'get_ad_details',
    'get_ad_creatives',
    'get_ad_image',
    'update_ad',
    'upload_ad_video',
    'get_insights',
    'bulk_get_insights',
    'list_custom_conversions',
    'create_custom_conversion',
    'delete_custom_conversion',
    # Note: 'get_login_link' is registered conditionally by the authentication module
    'login_cli',
    'login',
    'main',
    'create_budget_schedule',
    'search_interests',
    'get_interest_suggestions',
    'estimate_audience_size',
    'search_behaviors',
    'search_demographics',
    'search_geo_locations',
    'create_website_custom_audience',
    'create_video_custom_audience',
    'create_page_custom_audience',
    'create_instagram_custom_audience',
    'create_leadform_custom_audience',
    'list_custom_audiences',
    'create_lookalike_audience',
    'duplicate_campaign',
    'duplicate_adset',
    'duplicate_ad',
    'duplicate_creative',
    'create_pixel',
    'list_saved_audiences',
    'create_ab_test',
    'list_ab_tests',
    'get_ab_test_results',
] 