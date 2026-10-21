"""
Abstract Base Repository defining the database interface for Azure Buddy.
"""

from abc import ABC, abstractmethod
from typing import Optional, List
from core.models import Session, Message, QuizAttempt

class BaseRepository(ABC):
    @abstractmethod
    async def create_session(self, session_id: str, title: str = "New Study Session", language: str = "English", user_id: str = "anonymous") -> Session:
        """Create a new study session."""
        pass

    @abstractmethod
    async def get_session(self, session_id: str, user_id: Optional[str] = None) -> Optional[Session]:
        """Retrieve a session by ID with optional user ownership check."""
        pass

    @abstractmethod
    async def list_sessions(self, user_id: Optional[str] = None, limit: int = 20) -> List[Session]:
        """List recent sessions for a user ordered by updated_at descending."""
        pass

    @abstractmethod
    async def update_session(self, session_id: str, title: Optional[str] = None, language: Optional[str] = None, user_id: Optional[str] = None) -> Optional[Session]:
        """Update a session's title or active language."""
        pass

    @abstractmethod
    async def delete_session(self, session_id: str, user_id: Optional[str] = None) -> bool:
        """Delete a session and all its associated messages and quiz attempts."""
        pass

    @abstractmethod
    async def save_message(self, message: Message) -> Message:
        """Save a chat message."""
        pass

    @abstractmethod
    async def get_messages(self, session_id: str, limit: int = 50) -> List[Message]:
        """Get message history for a session ordered by created_at ascending."""
        pass

    @abstractmethod
    async def save_quiz_attempt(self, attempt: QuizAttempt) -> QuizAttempt:
        """Save a quiz question attempt."""
        pass

    @abstractmethod
    async def get_quiz_attempts(self, session_id: str) -> List[QuizAttempt]:
        """Get all quiz attempts for a session."""
        pass

    @abstractmethod
    async def is_healthy(self) -> bool:
        """Check if the database connection is healthy."""
        pass
