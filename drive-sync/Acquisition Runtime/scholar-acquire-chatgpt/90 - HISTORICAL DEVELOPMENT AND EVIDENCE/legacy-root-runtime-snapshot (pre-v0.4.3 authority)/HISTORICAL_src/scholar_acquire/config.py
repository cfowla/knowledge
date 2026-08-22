from __future__ import annotations

import os
from pathlib import Path
from pydantic import BaseModel, Field


class Settings(BaseModel):
    contact_email: str | None = Field(default_factory=lambda: os.getenv("SCHOLAR_FETCH_EMAIL") or os.getenv("UNPAYWALL_EMAIL") or os.getenv("NCBI_EMAIL"))
    openalex_api_key: str | None = Field(default_factory=lambda: os.getenv("OPENALEX_API_KEY"))
    cache_dir: Path = Field(default_factory=lambda: Path(os.getenv("SCHOLAR_FETCH_CACHE", "~/.cache/scholar-acquire")).expanduser())
    user_agent_name: str = "scholar-acquire-chatgpt/0.4.0"

    def user_agent(self) -> str:
        if self.contact_email:
            return f"{self.user_agent_name} (mailto:{self.contact_email})"
        return self.user_agent_name
