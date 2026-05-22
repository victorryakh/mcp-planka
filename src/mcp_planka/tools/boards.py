from typing import Any

from mcp.server.fastmcp import Context

from ..config import AppContext, serialize_model
from ..server import get_context


def get_project_boards(ctx: Context, project_id: str) -> list[dict[str, Any]]:
    app = get_context(ctx)
    project = app.planka.projects[project_id]
    boards = project.boards
    return [serialize_model(b) for b in boards]


def get_board(ctx: Context, board_id: str) -> dict[str, Any]:
    app = get_context(ctx)
    board = app.planka.boards[board_id]
    return serialize_model(board)