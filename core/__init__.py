"""
Core package for Azure Buddy AI.
"""

from .config import settings, Settings
from .models import (
    MessageRole, AgentIntent, Message, Session, QuizAttempt, QuizState,
    ChatRequest, ChatResponse, CreateSessionRequest, ConfigUpdateRequest, SystemStatusResponse
)
from .agent import AzureBuddyAgent

__all__ = [
    "settings",
    "Settings",
    "MessageRole",
    "AgentIntent",
    "Message",
    "Session",
    "QuizAttempt",
    "QuizState",
    "ChatRequest",
    "ChatResponse",
    "CreateSessionRequest",
    "ConfigUpdateRequest",
    "SystemStatusResponse",
    "AzureBuddyAgent"
]
