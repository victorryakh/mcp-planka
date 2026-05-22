from typing import Any

from mcp.server.fastmcp import Context

from ..config import AppContext, serialize_model
from ..server import get_context


def get_projects(ctx: Context) -> list[dict[str, Any]]:
    app = get_context(ctx)
    projects = app.planka.projects
    return [serialize_model(p) for p in projects]


def get_project(ctx: Context, project_id: str) -> dict[str, Any]:
    app = get_context(ctx)
    project = app.planka.projects[project_id]
    return serialize_model(project)