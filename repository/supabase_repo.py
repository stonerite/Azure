"""
Supabase REST implementation of BaseRepository using httpx.
"""

from typing import Optional, List, Any, Dict
from datetime import datetime, timezone
import httpx
import logging

from core.models import Session, Message, MessageRole, QuizAttempt
from repository.base import BaseRepository

logger = logging.getLogger("azure_buddy.supabase")

class SupabaseRepository(BaseRepository):
    def __init__(self, supabase_url: str, anon_key: str):
        self.base_url = supabase_url.rstrip("/")
        self.anon_key = anon_key
        self.headers = {
            "apikey": self.anon_key,
            "Authorization": f"Bearer {self.anon_key}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        }

    def _client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(base_url=self.base_url, headers=self.headers, timeout=10.0)

    async def create_session(
        self,
        session_id: str,
        title: str = "New Study Session",
        language: str = "English",
        user_id: str = "anonymous"
    ) -> Session:
        now = datetime.now(timezone.utc).isoformat()
        payload = {
            "id": session_id,
            "user_id": user_id,
            "title": title,
            "language": language,
            "created_at": now,
            "updated_at": now
        }
        async with self._client() as client:
            resp = await client.post("/rest/v1/sessions", json=payload)
            if resp.status_code == 400 and "user_id" in resp.text:
                # Schema fallback if user_id column has not yet been added to Supabase
                fallback_payload = {k: v for k, v in payload.items() if k != "user_id"}
                resp = await client.post("/rest/v1/sessions", json=fallback_payload)

            resp.raise_for_status()
            data = resp.json()
            row = data[0] if isinstance(data, list) and data else payload
            return Session(
                id=row["id"],
                user_id=row.get("user_id", user_id),
                title=row["title"],
                language=row.get("language", language),
                created_at=row["created_at"],
                updated_at=row["updated_at"]
            )

    async def get_session(self, session_id: str, user_id: Optional[str] = None) -> Optional[Session]:
        async with self._client() as client:
            resp = await client.get(f"/rest/v1/sessions?id=eq.{session_id}&select=*")
            if resp.status_code == 200:
                data = resp.json()
                if data and len(data) > 0:
                    row = data[0]
                    session_user = row.get("user_id", "anonymous")
                    if user_id and session_user != user_id and session_user != "anonymous":
                        return None
                    return Session(
                        id=row["id"],
                        user_id=session_user,
                        title=row["title"],
                        language=row.get("language", "English"),
                        created_at=row["created_at"],
                        updated_at=row["updated_at"]
                    )
            return None

    async def list_sessions(self, user_id: Optional[str] = None, limit: int = 20) -> List[Session]:
        async with self._client() as client:
            query = f"/rest/v1/sessions?select=*&order=updated_at.desc&limit={limit}"
            if user_id:
                query = f"/rest/v1/sessions?user_id=eq.{user_id}&select=*&order=updated_at.desc&limit={limit}"
            resp = await client.get(query)
            if resp.status_code == 400 and "user_id" in resp.text:
                # Fallback if user_id column doesn't exist yet in Supabase schema cache
                resp = await client.get(f"/rest/v1/sessions?select=*&order=updated_at.desc&limit={limit}")

            if resp.status_code == 200:
                data = resp.json()
                results = []
                for row in data:
                    row_user = row.get("user_id")
                    if user_id and row_user and row_user != user_id and row_user != "anonymous":
                        continue
                    results.append(
                        Session(
                            id=row["id"],
                            user_id=row_user or "anonymous",
                            title=row["title"],
                            language=row.get("language", "English"),
                            created_at=row["created_at"],
                            updated_at=row["updated_at"]
                        )
                    )
                return results
            return []

    async def update_session(
        self,
        session_id: str,
        title: Optional[str] = None,
        language: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> Optional[Session]:
        session = await self.get_session(session_id, user_id)
        if not session:
            return None

        now = datetime.now(timezone.utc).isoformat()
        payload: Dict[str, Any] = {"updated_at": now}
        if title is not None:
            payload["title"] = title
        if language is not None:
            payload["language"] = language

        async with self._client() as client:
            resp = await client.patch(f"/rest/v1/sessions?id=eq.{session_id}", json=payload)
            if resp.status_code in [200, 204]:
                data = resp.json() if resp.status_code == 200 else []
                if data and len(data) > 0:
                    row = data[0]
                    return Session(
                        id=row["id"],
                        user_id=row.get("user_id", "anonymous"),
                        title=row["title"],
                        language=row.get("language", "English"),
                        created_at=row["created_at"],
                        updated_at=row["updated_at"]
                    )
                return await self.get_session(session_id, user_id)
            return None

    async def delete_session(self, session_id: str, user_id: Optional[str] = None) -> bool:
        if user_id:
            session = await self.get_session(session_id, user_id)
            if not session:
                return False

        async with self._client() as client:
            resp = await client.delete(f"/rest/v1/sessions?id=eq.{session_id}")
            return resp.status_code in [200, 204]

    async def save_message(self, message: Message) -> Message:
        payload = {
            "id": message.id,
            "session_id": message.session_id,
            "role": message.role.value,
            "content": message.content,
            "metadata": message.metadata or {},
            "created_at": message.created_at
        }
        async with self._client() as client:
            resp = await client.post("/rest/v1/messages", json=payload)
            resp.raise_for_status()
            # Also touch session updated_at
            await client.patch(
                f"/rest/v1/sessions?id=eq.{message.session_id}",
                json={"updated_at": message.created_at}
            )
            return message

    async def get_messages(self, session_id: str, limit: int = 50) -> List[Message]:
        async with self._client() as client:
            resp = await client.get(
                f"/rest/v1/messages?session_id=eq.{session_id}&select=*&order=created_at.asc&limit={limit}"
            )
            if resp.status_code == 200:
                data = resp.json()
                return [
                    Message(
                        id=row["id"],
                        session_id=row["session_id"],
                        role=MessageRole(row["role"]),
                        content=row["content"],
                        metadata=row.get("metadata") or {},
                        created_at=row["created_at"]
                    )
                    for row in data
                ]
            return []

    async def save_quiz_attempt(self, attempt: QuizAttempt) -> QuizAttempt:
        payload = {
            "id": attempt.id,
            "session_id": attempt.session_id,
            "question_id": attempt.question_id,
            "topic": attempt.topic,
            "selected_option": attempt.selected_option,
            "is_correct": attempt.is_correct,
            "created_at": attempt.created_at
        }
        async with self._client() as client:
            resp = await client.post("/rest/v1/quiz_attempts", json=payload)
            resp.raise_for_status()
            return attempt

    async def get_quiz_attempts(self, session_id: str) -> List[QuizAttempt]:
        async with self._client() as client:
            resp = await client.get(
                f"/rest/v1/quiz_attempts?session_id=eq.{session_id}&select=*&order=created_at.asc"
            )
            if resp.status_code == 200:
                data = resp.json()
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
                    for row in data
                ]
            return []

    async def is_healthy(self) -> bool:
        try:
            async with self._client() as client:
                resp = await client.get("/rest/v1/sessions?limit=1")
                return resp.status_code in [200, 206]
        except Exception as e:
            logger.warning(f"Supabase health check failed: {e}")
            return False
