"""
FastMCP HTTP Authentication Integration for Meta Ads MCP

This module provides direct integration with FastMCP to inject authentication
from HTTP headers into the tool execution context.
"""

import asyncio
import contextvars
import threading
from typing import Optional
from .utils import logger
import json

# Use context variables for async support
_auth_token: contextvars.ContextVar[Optional[str]] = contextvars.ContextVar('auth_token', default=None)
_meta_app_id: contextvars.ContextVar[Optional[str]] = contextvars.ContextVar('meta_app_id', default=None)
_meta_app_secret: contextvars.ContextVar[Optional[str]] = contextvars.ContextVar('meta_app_secret', default=None)

# Thread-safe global fallback for when contextvars don't propagate
# (e.g. BaseHTTPMiddleware runs call_next in a separate task)
_request_token_lock = threading.Lock()
_request_token_store: dict = {}  # asyncio.Task id -> token

class FastMCPAuthIntegration:
    """Direct integration with FastMCP for HTTP authentication"""
    
    @staticmethod
    def set_auth_token(token: str) -> None:
        """Set authentication token for the current context
        
        Args:
            token: Access token to use for this request
        """
        _auth_token.set(token)
        # Also store in global fallback keyed by current task id
        try:
            task = asyncio.current_task()
            if task:
                with _request_token_lock:
                    _request_token_store[id(task)] = token
        except RuntimeError:
            pass
    
    @staticmethod
    def get_auth_token() -> Optional[str]:
        """Get authentication token for the current context
        
        Returns:
            Access token if set, None otherwise
        """
        # Try contextvars first
        token = _auth_token.get(None)
        if token:
            return token
        # Fallback: check global store (handles BaseHTTPMiddleware context loss)
        try:
            task = asyncio.current_task()
            if task:
                with _request_token_lock:
                    return _request_token_store.get(id(task))
        except RuntimeError:
            pass
        return None
    
    @staticmethod
    def clear_auth_token() -> None:
        """Clear authentication token for the current context"""
        _auth_token.set(None)
        try:
            task = asyncio.current_task()
            if task:
                with _request_token_lock:
                    _request_token_store.pop(id(task), None)
        except RuntimeError:
            pass

    @staticmethod
    def set_meta_app_credentials(app_id: Optional[str], app_secret: Optional[str]) -> None:
        """Set per-request Meta App credentials"""
        _meta_app_id.set(app_id)
        _meta_app_secret.set(app_secret)

    @staticmethod
    def get_meta_app_id() -> Optional[str]:
        return _meta_app_id.get(None)

    @staticmethod
    def get_meta_app_secret() -> Optional[str]:
        return _meta_app_secret.get(None)

    @staticmethod
    def clear_meta_app_credentials() -> None:
        _meta_app_id.set(None)
        _meta_app_secret.set(None)
    
    @staticmethod
    def extract_token_from_headers(headers: dict) -> Optional[str]:
        """Extract token from HTTP headers
        
        Args:
            headers: HTTP request headers
            
        Returns:
            Token if found, None otherwise
        """
        # Check for Bearer token in Authorization header (primary method)
        auth_header = headers.get('Authorization') or headers.get('authorization')
        if auth_header and auth_header.lower().startswith('bearer '):
            token = auth_header[7:].strip()
            logger.debug("Found Bearer token in Authorization header")
            return token
        
        # Check for direct Meta access token
        meta_token = headers.get('X-META-ACCESS-TOKEN') or headers.get('x-meta-access-token')
        if meta_token:
            return meta_token
        
        return None

def patch_fastmcp_server(mcp_server):
    """Patch FastMCP server to inject authentication from HTTP headers
    
    Args:
        mcp_server: FastMCP server instance to patch
    """
    logger.info("Patching FastMCP server for HTTP authentication")
    
    # Store the original run method
    original_run = mcp_server.run
    
    def patched_run(transport="stdio", **kwargs):
        """Enhanced run method that sets up HTTP auth integration"""
        logger.debug(f"Starting FastMCP with transport: {transport}")
        
        if transport == "streamable-http":
            logger.debug("Setting up HTTP authentication for streamable-http transport")
            setup_http_auth_patching()
        
        # Call the original run method
        return original_run(transport=transport, **kwargs)
    
    # Replace the run method
    mcp_server.run = patched_run
    logger.info("FastMCP server patching complete")

def setup_http_auth_patching():
    """Setup HTTP authentication patching for auth system"""
    logger.info("Setting up HTTP authentication patching")
    
    # Import and patch the auth system
    from . import auth
    from . import api
    from . import authentication
    
    # Store the original function
    original_get_current_access_token = auth.get_current_access_token
    
    async def get_current_access_token_with_http_support() -> Optional[str]:
        """Enhanced get_current_access_token that checks HTTP context first"""
        
        # Check for context-scoped token first
        context_token = FastMCPAuthIntegration.get_auth_token()
        if context_token:
            return context_token
        
        # Fall back to original implementation
        return await original_get_current_access_token()
    
    # Replace the function in all modules that imported it
    auth.get_current_access_token = get_current_access_token_with_http_support
    api.get_current_access_token = get_current_access_token_with_http_support
    authentication.get_current_access_token = get_current_access_token_with_http_support
    
    logger.info("Auth system patching complete - patched in auth, api, and authentication modules")

# Global instance for easy access
fastmcp_auth = FastMCPAuthIntegration()

# Forward declaration of setup_starlette_middleware
def setup_starlette_middleware(app):
    pass

def setup_fastmcp_http_auth(mcp_server):
    """Setup HTTP authentication integration with FastMCP
    
    Args:
        mcp_server: FastMCP server instance to configure
    """
    logger.info("Setting up FastMCP HTTP authentication integration")
    
    # 1. Patch FastMCP's run method to ensure our get_current_access_token patch is applied
    # This remains crucial for the token to be picked up by tool calls.
    patch_fastmcp_server(mcp_server) # This patches mcp_server.run
    
    # 2. Patch the methods that provide the Starlette app instance
    # This ensures our middleware is added to the app Uvicorn will actually serve.

    app_provider_methods = []
    if mcp_server.settings.json_response:
        if hasattr(mcp_server, "streamable_http_app") and callable(mcp_server.streamable_http_app):
            app_provider_methods.append("streamable_http_app")
        else:
            logger.warning("mcp_server.streamable_http_app not found or not callable, cannot patch for JSON responses.")
    else: # SSE
        if hasattr(mcp_server, "sse_app") and callable(mcp_server.sse_app):
            app_provider_methods.append("sse_app")
        else:
            logger.warning("mcp_server.sse_app not found or not callable, cannot patch for SSE responses.")

    if not app_provider_methods:
        logger.error("No suitable app provider method (streamable_http_app or sse_app) found on mcp_server. Cannot add HTTP Auth middleware.")
        # Fallback or error handling might be needed here if this is critical
    
    for method_name in app_provider_methods:
        original_app_provider_method = getattr(mcp_server, method_name)
        
        def new_patched_app_provider_method(*args, **kwargs):
            # Call the original method to get/create the Starlette app
            app = original_app_provider_method(*args, **kwargs)
            if app:
                logger.debug(f"Original {method_name} returned app: {type(app)}. Adding AuthInjectionMiddleware.")
                # Now, add our middleware to this specific app instance
                setup_starlette_middleware(app) 
            else:
                logger.error(f"Original {method_name} returned None or a non-app object.")
            return app
            
        setattr(mcp_server, method_name, new_patched_app_provider_method)
        logger.debug(f"Patched mcp_server.{method_name} to inject AuthInjectionMiddleware.")

    # The old setup_request_middleware call is no longer needed here,
    # as middleware addition is now handled by patching the app provider methods.
    # try:
    #     setup_request_middleware(mcp_server) 
    # except Exception as e:
    #     logger.warning(f"Could not setup request middleware: {e}")

    logger.info("FastMCP HTTP authentication integration setup attempt complete.")

# Remove the old setup_request_middleware function as its logic is integrated above
# def setup_request_middleware(mcp_server): ... (delete this function)

# --- AuthInjectionMiddleware definition ---
# NOTE: We use a pure ASGI middleware instead of BaseHTTPMiddleware because
# BaseHTTPMiddleware runs call_next in a separate asyncio.Task, which breaks
# contextvars propagation. This is a known Starlette issue.
from starlette.types import ASGIApp, Receive, Scope, Send

class AuthInjectionMiddleware:
    """Pure ASGI middleware that injects auth tokens into the request context.
    Unlike BaseHTTPMiddleware, this preserves contextvars across the request lifecycle."""
    
    def __init__(self, app: ASGIApp) -> None:
        self.app = app
    
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        
        # Extract headers from scope
        headers_dict = {}
        for key, value in scope.get("headers", []):
            headers_dict[key.decode("latin-1").lower()] = value.decode("latin-1")
        
        logger.debug(f"HTTP Auth Middleware: Processing request to {scope.get('path', '/')}")
        
        # Extract auth token from headers
        auth_token = None
        auth_header = headers_dict.get('authorization', '')
        if auth_header.lower().startswith('bearer '):
            auth_token = auth_header[7:].strip()
        
        if not auth_token:
            auth_token = headers_dict.get('x-meta-access-token')

        # Extract Meta App credentials from headers (per-user app)
        meta_app_id = headers_dict.get('x-meta-app-id')
        meta_app_secret = headers_dict.get('x-meta-app-secret')

        if auth_token:
            logger.debug(f"HTTP Auth Middleware: Setting auth token: {auth_token[:4]}...")
            FastMCPAuthIntegration.set_auth_token(auth_token)
        else:
            logger.warning("HTTP Auth Middleware: No authentication token found in headers")

        if meta_app_id and meta_app_secret:
            logger.info(f"HTTP Auth Middleware: Setting per-user Meta App credentials (app_id: {meta_app_id})")
            FastMCPAuthIntegration.set_meta_app_credentials(meta_app_id, meta_app_secret)

        try:
            await self.app(scope, receive, send)
        finally:
            if auth_token:
                FastMCPAuthIntegration.clear_auth_token()
            if meta_app_id:
                FastMCPAuthIntegration.clear_meta_app_credentials()

def setup_starlette_middleware(app):
    """Wrap the Starlette app with AuthInjectionMiddleware.
    
    Args:
        app: Starlette app instance
    """
    if not app:
        logger.error("Cannot setup Starlette middleware, app is None.")
        return

    # For pure ASGI middleware, we wrap the app directly
    # Check if already wrapped by looking at user_middleware
    already_added = False
    if hasattr(app, 'user_middleware'):
        for middleware_item in app.user_middleware:
            if getattr(middleware_item, 'cls', None) == AuthInjectionMiddleware:
                already_added = True
                break
            
    if not already_added:
        try:
            app.add_middleware(AuthInjectionMiddleware)
            logger.info("AuthInjectionMiddleware added to Starlette app successfully.")
        except Exception as e:
            logger.error(f"Failed to add AuthInjectionMiddleware to Starlette app: {e}", exc_info=True)
    else:
        logger.debug("AuthInjectionMiddleware already present in Starlette app's middleware stack.") 