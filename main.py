import sys

import uvicorn
from mcp_planka.server import mcp
from mcp_planka.settings import Settings


def main() -> None:
    settings = Settings()

    if len(sys.argv) > 1 and sys.argv[1] == "--stdio":
        mcp.run(transport="stdio")
    else:
        app = mcp.streamable_http_app()
        uvicorn.run(app, host=settings.mcp_host, port=settings.mcp_port)


if __name__ == "__main__":
    main()
