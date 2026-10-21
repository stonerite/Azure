"""
SQLite implementation of BaseRepository for local storage and fallback.
"""

import sqlite3
import json
import asyncio
from pathlib import Path
from typing import Optional, List, Any
from datetime import datetime, timezone

from core.models import Session, Message, MessageRole, QuizAttempt
from repository.base import BaseRepository

class SQLiteRepository(BaseRepository):
    def __init__(self, db_path: Path):
        self.db_path = str(db_path)
        self._init_db()

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL DEFAULT 'anonymous',
                title TEXT NOT NULL DEFAULT 'New Study Session',
                language TEXT DEFAULT 'English',
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)
        # Auto-migrate table if user_id doesn't exist
        cursor.execute("PRAGMA table_info(sessions)")
        cols = [r["name"] for r in cursor.fetchall()]
        if "user_id" not in cols:
            cursor.execute("ALTER TABLE sessions ADD COLUMN user_id TEXT DEFAULT 'anonymous'")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id TEXT PRIMARY KEY,
                session_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                metadata TEXT DEFAULT '{}',
                created_at TEXT NOT NULL,
                FOREIGN KEY (session_id) REFERENCES sessions (id) ON DELETE CASCADE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS quiz_attempts (
                id TEXT PRIMARY KEY,
                session_id TEXT NOT NULL,
                question_id INTEGER,
                topic TEXT,
                selected_option TEXT,
                is_correct BOOLEAN NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY (session_id) REFERENCES sessions (id) ON DELETE CASCADE
            )
        """)
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_messages_sess ON messages(session_id);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_quiz_sess ON quiz_attempts(session_id);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sessions_user ON sessions(user_id);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sessions_updated ON sessions(updated_at DESC);")
        conn.commit()
        conn.close()

    async def create_session(
        self,
        session_id: str,
        title: str = "New Study Session",
        language: str = "English",
        user_id: str = "anonymous"
    ) -> Session:
        def _sync_create():
            now = datetime.now(timezone.utc).isoformat()
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO sessions (id, user_id, title, language, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
                (session_id, user_id, title, language, now, now)
            )
            conn.commit()
            conn.close()
            return Session(id=session_id, user_id=user_id, title=title, language=language, created_at=now, updated_at=now)
        return await asyncio.to_thread(_sync_create)

    async def get_session(self, session_id: str, user_id: Optional[str] = None) -> Optional[Session]:
        def _sync_get():
            conn = self._get_connection()
            cursor = conn.cursor()
            if user_id:
                cursor.execute(
                    "SELECT * FROM sessions WHERE id = ? AND (user_id = ? OR user_id = 'anonymous')",
                    (session_id, user_id)
                )
            else:
                cursor.execute("SELECT * FROM sessions WHERE id = ?", (session_id,))
            row = cursor.fetchone()
            conn.close()
            if row:
                return Session(
                    id=row["id"],
                    user_id=row["user_id"] if "user_id" in row.keys() else "anonymous",
                    title=row["title"],
                    language=row["language"],
                    created_at=row["created_at"],
                    updated_at=row["updated_at"]
                )
            return None
        return await asyncio.to_thread(_sync_get)

    async def list_sessions(self, user_id: Optional[str] = None, limit: int = 20) -> List[Session]:
        def _sync_list():
            conn = self._get_connection()
            cursor = conn.cursor()
            if user_id:
                cursor.execute(
                    "SELECT * FROM sessions WHERE user_id = ? ORDER BY updated_at DESC LIMIT ?",
                    (user_id, limit)
                )
            else:
                cursor.execute("SELECT * FROM sessions ORDER BY updated_at DESC LIMIT ?", (limit,))
            rows = cursor.fetchall()
            conn.close()
            return [
                Session(
                    id=row["id"],
                    user_id=row["user_id"] if "user_id" in row.keys() else "anonymous",
                    title=row["title"],
                    language=row["language"],
                    created_at=row["created_at"],
                    updated_at=row["updated_at"]
                )
                for row in rows
            ]
        return await asyncio.to_thread(_sync_list)

    async def update_session(
        self,
        session_id: str,
        title: Optional[str] = None,
        language: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> Optional[Session]:
        def _sync_update():
            now = datetime.now(timezone.utc).isoformat()
            conn = self._get_connection()
            cursor = conn.cursor()
            
            updates = ["updated_at = ?"]
            params: List[Any] = [now]
            
            if title is not None:
                updates.append("title = ?")
                params.append(title)
            if language is not None:
                updates.append("language = ?")
                params.append(language)
                
            params.append(session_id)
            query = f"UPDATE sessions SET {', '.join(updates)} WHERE id = ?"
            if user_id:
                query += " AND (user_id = ? OR user_id = 'anonymous')"
                params.append(user_id)

            cursor.execute(query, params)
            conn.commit()
            
            cursor.execute("SELECT * FROM sessions WHERE id = ?", (session_id,))
            row = cursor.fetchone()
            conn.close()
            if row:
                return Session(
                    id=row["id"],
                    user_id=row["user_id"] if "user_id" in row.keys() else "anonymous",
                    title=row["title"],
                    language=row["language"],
                    created_at=row["created_at"],
                    updated_at=row["updated_at"]
                )
            return None
        return await asyncio.to_thread(_sync_update)

    async def delete_session(self, session_id: str, user_id: Optional[str] = None) -> bool:
        def _sync_delete():
            conn = self._get_connection()
            cursor = conn.cursor()
            if user_id:
                cursor.execute("SELECT id FROM sessions WHERE id = ? AND (user_id = ? OR user_id = 'anonymous')", (session_id, user_id))
                if not cursor.fetchone():
                    conn.close()
                    return False

            cursor.execute("DELETE FROM quiz_attempts WHERE session_id = ?", (session_id,))
            cursor.execute("DELETE FROM messages WHERE session_id = ?", (session_id,))
            cursor.execute("DELETE FROM sessions WHERE id = ?", (session_id,))
            affected = cursor.rowcount
            conn.commit()
            conn.close()
            return affected > 0
        return await asyncio.to_thread(_sync_delete)

    async def save_message(self, message: Message) -> Message:
        def _sync_save():
            conn = self._get_connection()
            cursor = conn.cursor()
            metadata_str = json.dumps(message.metadata or {})
            cursor.execute(
                "INSERT INTO messages (id, session_id, role, content, metadata, created_at) VALUES (?, ?, ?, ?, ?, ?)",
                (message.id, message.session_id, message.role.value, message.content, metadata_str, message.created_at)
            )
            # Update session's updated_at
            cursor.execute("UPDATE sessions SET updated_at = ? WHERE id = ?", (message.created_at, message.session_id))
            conn.commit()
            conn.close()
            return message
        return await asyncio.to_thread(_sync_save)

    async def get_messages(self, session_id: str, limit: int = 50) -> List[Message]:
        def _sync_get():
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM messages WHERE session_id = ? ORDER BY created_at ASC LIMIT ?",
                (session_id, limit)
            )
            rows = cursor.fetchall()
            conn.close()
            messages = []
            for row in rows:
                meta = {}
                try:
                    if row["metadata"]:
                        meta = json.loads(row["metadata"])
                except Exception:
                    meta = {}
                messages.append(Message(
                    id=row["id"],
                    session_id=row["session_id"],
                    role=MessageRole(row["role"]),
                    content=row["content"],
                    metadata=meta,
                    created_at=row["created_at"]
                ))
            return messages
        return await asyncio.to_thread(_sync_get)

    async def save_quiz_attempt(self, attempt: QuizAttempt) -> QuizAttempt:
        def _sync_save():
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO quiz_attempts (id, session_id, question_id, topic, selected_option, is_correct, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (attempt.id, attempt.session_id, attempt.question_id, attempt.topic, attempt.selected_option, 1 if attempt.is_correct else 0, attempt.created_at)
            )
            conn.commit()
            conn.close()
            return attempt
        return await asyncio.to_thread(_sync_save)

    async def get_quiz_attempts(self, session_id: str) -> List[QuizAttempt]:
        def _sync_get():
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM quiz_attempts WHERE session_id = ? ORDER BY created_at ASC",
                (session_id,)
            )
            rows = cursor.fetchall()
            conn.close()
            return [
                QuizAttempt(
                    id=row["id"],
                    session_id=row["session_id"],
                    question_id=row["question_id"],
                    topic=row["topic"],
                    selected_option=row["selected_option"],
                    is_correct=bool(row["is_correct"]),
                    created_at=row["created_at"]
                )
                for row in rows
            ]
        return await asyncio.to_thread(_sync_get)

    async def is_healthy(self) -> bool:
        def _sync_check():
            try:
                conn = self._get_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT 1")
                res = cursor.fetchone()
                conn.close()
                return res is not None
            except Exception:
                return False
        return await asyncio.to_thread(_sync_check)
