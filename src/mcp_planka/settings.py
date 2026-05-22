from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="PLANKA_", env_file=".env", extra="ignore")

    url: str
    api_key: str | None = None
    username: str | None = None
    password: str | None = None
    accept_terms: bool = True

    mcp_host: str = "0.0.0.0"
    mcp_port: int = 8000