"""Authentication-specific functionality for Meta Ads API.

The Meta Ads MCP server supports two authentication modes:

1. **Direct Token Mode** (recommended)
   - Uses META_ACCESS_TOKEN environment variable
   - User provides their Meta token directly
   - Best for production and multi-tenant setups

2. **Development/Local OAuth Mode**
   - Uses local callback server on localhost for OAuth redirect
   - Best for local development and testing

Environment Variables:
- META_ACCESS_TOKEN: Direct Meta token (primary)
- META_ADS_DISABLE_CALLBACK_SERVER: Disables local OAuth server
- META_ADS_DISABLE_LOGIN_LINK: Hard-disables the get_login_link tool
"""

import json
from typing import Optional
import asyncio
import os
from .api import meta_api_tool
from .auth import start_callback_server, shutdown_callback_server, auth_manager, get_current_access_token
from .server import mcp_server
from .utils import logger, META_APP_SECRET
# Only register the login link tool if not explicitly disabled
ENABLE_LOGIN_LINK = not bool(os.environ.get("META_ADS_DISABLE_LOGIN_LINK", ""))


async def get_login_link(access_token: Optional[str] = None) -> str:
    """
    Get a clickable login link for Meta Ads authentication.
    
    NOTE: If META_ACCESS_TOKEN is already set in the environment, this will
    confirm authentication is active. Otherwise, it will start the local OAuth flow.
    
    Args:
        access_token: Meta API access token (optional - will use cached token if not provided)
    
    Returns:
        A clickable resource link for Meta authentication
    """
    callback_server_disabled = bool(os.environ.get("META_ADS_DISABLE_CALLBACK_SERVER", ""))

    # If an access token was provided or exists in env, return success
    if access_token:
        return json.dumps({
            "message": "Already Authenticated",
            "status": "Using provided access token for authentication",
            "token_info": f"Token preview: {access_token[:4]}...",
            "authentication_method": "direct_token",
            "ready_to_use": "You can now use all Meta Ads MCP tools and commands."
        }, indent=2)

    env_token = os.environ.get("META_ACCESS_TOKEN")
    if env_token:
        return json.dumps({
            "message": "Already Authenticated",
            "status": "Using META_ACCESS_TOKEN from environment",
            "token_info": f"Token preview: {env_token[:4]}...",
            "authentication_method": "env_token",
            "ready_to_use": "You can now use all Meta Ads MCP tools and commands."
        }, indent=2)
    
    if callback_server_disabled:
        return json.dumps({
            "message": "Authentication Required",
            "instructions": "Please set META_ACCESS_TOKEN environment variable with your Meta API token.",
            "how_to_get_token": "Generate a token at https://developers.facebook.com/tools/explorer/",
            "authentication_method": "direct_token_required"
        }, indent=2)
    else:
        # Original Meta authentication flow (development/local)
        # Check if we have a cached token
        cached_token = auth_manager.get_access_token()
        token_status = "No token" if not cached_token else "Valid token"
        
        # If we already have a valid token and none was provided, just return success
        if cached_token and not access_token:
            logger.info("get_login_link called with existing valid token")
            return json.dumps({
                "message": "✅ Already Authenticated", 
                "status": "You're successfully authenticated with Meta Ads!",
                "token_info": f"Token preview: {cached_token[:4]}...",
                "created_at": auth_manager.token_info.created_at if hasattr(auth_manager, "token_info") else None,
                "expires_in": auth_manager.token_info.expires_in if hasattr(auth_manager, "token_info") else None,
                "authentication_method": "meta_oauth",
                "ready_to_use": "You can now use all Meta Ads MCP tools and commands."
            }, indent=2)
        
        # IMPORTANT: Start the callback server first by calling our helper function
        # This ensures the server is ready before we provide the URL to the user
        logger.info("Starting callback server for authentication")
        try:
            port = start_callback_server()
            logger.info(f"Callback server started on port {port}")
            
            # Generate direct login URL
            auth_manager.redirect_uri = f"http://localhost:{port}/callback"  # Ensure port is set correctly
            logger.info(f"Setting redirect URI to {auth_manager.redirect_uri}")
            login_url = auth_manager.get_auth_url()
            logger.info(f"Generated login URL: {login_url}")
        except Exception as e:
            logger.error(f"Failed to start callback server: {e}")
            return json.dumps({
                "message": "❌ Local Authentication Unavailable",
                "error": "Cannot start local callback server for authentication",
                "reason": str(e),
                "solutions": [
                    "Set META_ACCESS_TOKEN environment variable with your Meta API token",
                    "Check if another service is using the required ports"
                ],
                "authentication_method": "meta_oauth_disabled"
            }, indent=2)
        
        # Check if we can exchange for long-lived tokens
        token_exchange_supported = bool(META_APP_SECRET)
        token_duration = "60 days" if token_exchange_supported else "1-2 hours"
        
        # Return a special format that helps the LLM format the response properly
        response = {
            "message": "🔗 Click to Authenticate",
            "login_url": login_url,
            "markdown_link": f"[🚀 Authenticate with Meta Ads]({login_url})",
            "instructions": "Click the link above to authenticate with Meta Ads.",
            "server_info": f"Local callback server running on port {port}",
            "token_duration": f"Your token will be valid for approximately {token_duration}",
            "authentication_method": "meta_oauth",
            "what_happens_next": "After clicking, you'll be redirected to Meta's authentication page. Once completed, your token will be automatically saved.",
            "security_note": "This uses a secure local callback server for development purposes."
        }
        
        # Wait a moment to ensure the server is fully started
        await asyncio.sleep(1)
        
    return json.dumps(response, indent=2)

# Conditionally register as MCP tool only when enabled
if ENABLE_LOGIN_LINK:
    get_login_link = mcp_server.tool()(get_login_link)