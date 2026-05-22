from typing import Any

from mcp.server.fastmcp import Context

from ..config import AppContext, serialize_model
from ..server import get_context


def get_board_lists(ctx: Context, board_id: str) -> list[dict[str, Any]]:
    app = get_context(ctx)
    board = app.planka.boards[board_id]
    lists = board.lists
    return [serialize_model(lst) for lst in lists]


def create_list(ctx: Context, board_id: str, name: str) -> dict[str, Any]:
    app = get_context(ctx)
    new_list = app.planka.create_list(board_id=board_id, name=name)
    return serialize_model(new_list)