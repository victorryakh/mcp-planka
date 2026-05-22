from dataclasses import dataclass
from typing import Any

from plankapy import Planka

from .settings import Settings


@dataclass
class AppContext:
    planka: Planka
    settings: Settings


def create_app_context(settings: Settings) -> AppContext:
    planka = Planka(
        url=settings.url,
        api_key=settings.api_key,
        username=settings.username,
        password=settings.password,
        accept_terms=settings.accept_terms,
    )
    return AppContext(planka=planka, settings=settings)


def serialize_model(model: Any) -> dict[str, Any]:
    if hasattr(model, "model_dump"):
        return model.model_dump()
    if hasattr(model, "__dict__"):
        result = {}
        for key, value in model.__dict__.items():
            if not key.startswith("_"):
                result[key] = serialize_model(value) if hasattr(value, "__dict__") else value
        return result
    return model