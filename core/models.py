"""
Domain models and API contracts for Azure Buddy.
"""

from enum import Enum
from typing import Optional, List, Dict, Any
from datetime import datetime, timezone
from pydantic import BaseModel, Field

class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

class AgentIntent(str, Enum):
    QUIZ_START = "quiz_start"
    QUIZ_ANSWER = "quiz_answer"
    QUIZ_ADVANCE = "quiz_advance"
    EXPLAIN_CONCEPT = "explain_concept"
    SELECT_AREA = "select_area"
    OUT_OF_SCOPE = "out_of_scope"
    LANGUAGE_SWITCH = "language_switch"
    GENERAL_CHAT = "general_chat"

class Message(BaseModel):
    id: str
    session_id: str
    role: MessageRole
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class Session(BaseModel):
    id: str
    user_id: str = "anonymous"
    title: str = "New Study Session"
    language: str = "English"
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class QuizAttempt(BaseModel):
    id: str
    session_id: str
    question_id: int
    topic: str
    selected_option: str
    is_correct: bool
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class QuizState(BaseModel):
    mode: str = "idle"  # "idle" or "quiz"
    current_question: Optional[Dict[str, Any]] = None
    last_answered_id: Optional[int] = None
    question_index: int = 0
    total_questions: int = 5
    score: int = 0
    asked_ids: List[int] = Field(default_factory=list)
    missed_topics: List[str] = Field(default_factory=list)
    language: str = "English"

# API Requests & Responses
class ChatRequest(BaseModel):
    session_id: str
    message: str
    language: Optional[str] = "English"
    user_id: Optional[str] = "anonymous"

class ChatResponse(BaseModel):
    message: Message
    intent: Optional[str] = None

class CreateSessionRequest(BaseModel):
    title: Optional[str] = "New Session"
    language: Optional[str] = "English"
    user_id: Optional[str] = "anonymous"

class ConfigUpdateRequest(BaseModel):
    supabase_url: Optional[str] = None
    supabase_anon_key: Optional[str] = None
    gemini_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None

class SystemStatusResponse(BaseModel):
    supabase_connected: bool
    database_mode: str
    ai_active: bool
    ai_provider: str
    version: str
