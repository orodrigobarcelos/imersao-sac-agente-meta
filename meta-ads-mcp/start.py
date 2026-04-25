#!/usr/bin/env python3
import os
import sys
import subprocess

def main():
    # Get PORT from environment variable, default to 3000
    port = os.environ.get('PORT', '3000')
    
    # Build the command
    cmd = [
        sys.executable, '-m', 'meta_ads_mcp',
        '--transport', 'streamable-http',
        '--host', '0.0.0.0',
        '--port', str(port)
    ]
    
    print(f"Starting MCP server on port {port}")
    print(f"Command: {' '.join(cmd)}")
    
    # Execute the command
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
