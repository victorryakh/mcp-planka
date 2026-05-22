from datetime import datetime
from typing import Any

from mcp.server.fastmcp import Context

from ..config import AppContext, serialize_model
from ..server import get_context


def get_board_cards(ctx: Context, board_id: str) -> list[dict[str, Any]]:
    app = get_context(ctx)
    board = app.planka.boards[board_id]
    cards = board.cards
    return [serialize_model(c) for c in cards]


def get_card(ctx: Context, card_id: str) -> dict[str, Any]:
    app = get_context(ctx)
    card = app.planka.cards[card_id]
    return serialize_model(card)


def create_card(
    ctx: Context,
    list_id: str,
    name: str,
    description: str | None = None,
    due_date: datetime | None = None,
) -> dict[str, Any]:
    app = get_context(ctx)
    new_card = app.planka.create_card(
        list_id=list_id,
        name=name,
        description=description,
        due_date=due_date,
    )
    return serialize_model(new_card)


def update_card(
    ctx: Context,
    card_id: str,
    name: str | None = None,
    description: str | None = None,
    due_date: datetime | None = None,
) -> dict[str, Any]:
    app = get_context(ctx)
    card = app.planka.cards[card_id]
    if name is not None:
        card.name = name
    if description is not None:
        card.description = description
    if due_date is not None:
        card.due_date = due_date
    card.update()
    return serialize_model(card)


def delete_card(ctx: Context, card_id: str) -> dict[str, str]:
    app = get_context(ctx)
    app.planka.delete_card(card_id=card_id)
    return {"status": "deleted", "card_id": card_id}


def move_card(ctx: Context, card_id: str, list_id: str, position: int | None = None) -> dict[str, Any]:
    app = get_context(ctx)
    card = app.planka.cards[card_id]
    card.list_id = list_id
    if position is not None:
        card.position = position
    card.update()
    return serialize_model(card)


def search_cards(ctx: Context, query: str) -> list[dict[str, Any]]:
    app = get_context(ctx)
    cards = app.planka.cards[{"name": lambda n: query.lower() in n.lower()}]
    return [serialize_model(c) for c in cards]