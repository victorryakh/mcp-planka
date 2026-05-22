import uvicorn
from mcp_planka.server import mcp
from mcp_planka.settings import Settings

if __name__ == "__main__":
    settings = Settings()
    app = mcp.streamable_http_app()
    uvicorn.run(app, host=settings.mcp_host, port=settings.mcp_port)