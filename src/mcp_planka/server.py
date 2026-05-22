from contextlib import asynccontextmanager
from typing import Any, AsyncIterator

from mcp.server.fastmcp import Context, FastMCP

from .config import AppContext, create_app_context, serialize_model
from .settings import Settings


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    settings = Settings()
    ctx = create_app_context(settings)
    try:
        ctx.planka.login()
    except Exception as e:
        raise RuntimeError(f"Failed to login to Planka: {e}") from e
    yield ctx


mcp = FastMCP(
    name="Planka MCP Server",
    json_response=True,
    lifespan=app_lifespan,
)


def get_context(ctx: Context) -> AppContext:
    return ctx.request_context.lifespan_context


def serialize_model(model: Any) -> dict[str, Any]:
    result = {}
    for key, value in model.__dict__.items():
        if key.startswith("_"):
            continue
        if hasattr(value, "__dict__") and not isinstance(value, (str, int, float, bool, list, dict)):
            result[key] = serialize_model(value)
        elif isinstance(value, list):
            result[key] = [serialize_model(v) if hasattr(v, "__dict__") else v for v in value]
        else:
            result[key] = value
    return result


@mcp.resource("planka://me")
def get_current_user_resource(ctx: Context) -> dict[str, Any]:
    app = get_context(ctx)
    user = app.planka.me
    return serialize_model(user)


@mcp.resource("planka://projects")
def get_projects_resource(ctx: Context) -> list[dict[str, Any]]:
    app = get_context(ctx)
    projects = app.planka.projects
    return [serialize_model(p) for p in projects]


@mcp.resource("planka://project/{project_id}")
def get_project_resource(ctx: Context, project_id: str) -> dict[str, Any]:
    app = get_context(ctx)
    project = app.planka.projects[project_id]
    return serialize_model(project)


@mcp.resource("planka://board/{board_id}")
def get_board_resource(ctx: Context, board_id: str) -> dict[str, Any]:
    app = get_context(ctx)
    board = app.planka.boards[board_id]
    return serialize_model(board)


from .tools.projects import get_projects, get_project
from .tools.boards import get_project_boards, get_board
from .tools.lists import get_board_lists, create_list
from .tools.cards import (
    get_board_cards,
    get_card,
    create_card,
    update_card,
    delete_card,
    move_card,
    search_cards,
)
from .tools.activity import get_card_comments, get_board_activity, get_project_activity

mcp.add_tool(get_projects)
mcp.add_tool(get_project)
mcp.add_tool(get_project_boards)
mcp.add_tool(get_board)
mcp.add_tool(get_board_lists)
mcp.add_tool(create_list)
mcp.add_tool(get_board_cards)
mcp.add_tool(get_card)
mcp.add_tool(create_card)
mcp.add_tool(update_card)
mcp.add_tool(delete_card)
mcp.add_tool(move_card)
mcp.add_tool(search_cards)
mcp.add_tool(get_card_comments)
mcp.add_tool(get_board_activity)
mcp.add_tool(get_project_activity)