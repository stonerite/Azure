"""
Core configuration management for Azure Buddy AI.
Loads settings from environment variables with strong typing and default fallbacks.
"""

import os
from pathlib import Path
from typing import Optional
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent

def _load_env_file():
    env_file = BASE_DIR / ".env"
    if env_file.exists():
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    k = k.strip()
                    v = v.strip().strip('"').strip("'")
                    if k not in os.environ:
                        os.environ[k] = v

_load_env_file()

class Settings(BaseModel):
    app_name: str = "Azure Buddy AI"
    version: str = "2.0.0"
    base_dir: Path = BASE_DIR
    port: int = int(os.getenv("PORT", "8000"))
    
    # Supabase Cloud Database
    supabase_url: str = os.getenv("SUPABASE_URL", "").rstrip("/")
    supabase_anon_key: str = os.getenv("SUPABASE_ANON_KEY", "")
    
    # AI Providers
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    
    # Local SQLite Fallback Path
    @property
    def sqlite_db_path(self) -> Path:
        if os.getenv("VERCEL"):
            return Path("/tmp") / "azure_buddy_local.db"
        return BASE_DIR / "azure_buddy_local.db"

    @property
    def is_supabase_enabled(self) -> bool:
        return bool(self.supabase_url and self.supabase_anon_key and "your-project" not in self.supabase_url)

    @property
    def is_llm_enabled(self) -> bool:
        return bool(self.gemini_api_key or self.openai_api_key)

    @property
    def active_llm_provider(self) -> str:
        if self.gemini_api_key:
            return "Google Gemini 2.5 Flash"
        if self.openai_api_key:
            return "OpenAI GPT-4o-mini"
        return "Deterministic Intelligent Engine"

settings = Settings()
