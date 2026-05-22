from datetime import datetime
from typing import Any

from mcp.server.fastmcp import Context

from ..config import AppContext, serialize_model
from ..server import get_context


def get_card_comments(ctx: Context, card_id: str) -> list[dict[str, Any]]:
    app = get_context(ctx)
    card = app.planka.cards[card_id]
    comments = card.comments
    return [serialize_model(c) for c in comments]


def get_board_activity(ctx: Context, board_id: str, since: datetime | None = None) -> list[dict[str, Any]]:
    app = get_context(ctx)
    board = app.planka.boards[board_id]
    all_actions = []
    for lst in board.lists:
        for card in lst.cards:
            for action in card.comments:
                all_actions.append(serialize_model(action))
    all_actions.sort(key=lambda x: x.get("createdAt", ""), reverse=True)
    if since:
        all_actions = [a for a in all_actions if a.get("createdAt", "") >= since.isoformat()]
    return all_actions


def get_project_activity(ctx: Context, project_id: str, since: datetime | None = None) -> list[dict[str, Any]]:
    app = get_context(ctx)
    project = app.planka.projects[project_id]
    all_actions = []
    for board in project.boards:
        for lst in board.lists:
            for card in lst.cards:
                for action in card.comments:
                    all_actions.append(serialize_model(action))
    all_actions.sort(key=lambda x: x.get("createdAt", ""), reverse=True)
    if since:
        all_actions = [a for a in all_actions if a.get("createdAt", "") >= since.isoformat()]
    return all_actions