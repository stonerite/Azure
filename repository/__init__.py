"""
Repository factory and exports.
"""

from core.config import settings, Settings
from repository.base import BaseRepository
from repository.sqlite_repo import SQLiteRepository
from repository.supabase_repo import SupabaseRepository

def get_repository(app_settings: Settings = settings) -> BaseRepository:
    """Return the active repository instance (Supabase if configured, SQLite fallback)."""
    if app_settings.is_supabase_enabled:
        return SupabaseRepository(
            supabase_url=app_settings.supabase_url,
            anon_key=app_settings.supabase_anon_key
        )
    return SQLiteRepository(db_path=app_settings.sqlite_db_path)

__all__ = [
    "BaseRepository",
    "SQLiteRepository",
    "SupabaseRepository",
    "get_repository"
]
