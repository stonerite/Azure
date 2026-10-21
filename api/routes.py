"""
FastAPI route handlers for Azure Buddy AI.
"""

import uuid
from typing import Optional, Dict, Any, List
from fastapi import APIRouter, HTTPException, Depends, Header

from core.config import settings, Settings
from core.models import (
    ChatRequest, ChatResponse, CreateSessionRequest, ConfigUpdateRequest,
    SystemStatusResponse, Message, Session
)
from repository.base import BaseRepository
from repository import get_repository
from core.agent import AzureBuddyAgent

router = APIRouter(prefix="/api", tags=["Azure Buddy"])

def get_current_user_id(x_user_id: Optional[str] = Header(None)) -> str:
    """Extract client user identity for private workspace isolation."""
    if x_user_id and x_user_id.strip():
        return x_user_id.strip()
    return "anonymous"

# Global state instances
_repo: Optional[BaseRepository] = None
_agent: Optional[AzureBuddyAgent] = None

def get_repo() -> BaseRepository:
    global _repo
    if _repo is None:
        _repo = get_repository(settings)
    return _repo

def get_agent(repo: BaseRepository = Depends(get_repo)) -> AzureBuddyAgent:
    global _agent
    if _agent is None or _agent.repo != repo:
        _agent = AzureBuddyAgent(repository=repo)
    return _agent

@router.get("/status", response_model=SystemStatusResponse)
async def get_system_status(repo: BaseRepository = Depends(get_repo)):
    """Check database health, AI provider status, and system metadata."""
    is_healthy = await repo.is_healthy()
    return SystemStatusResponse(
        supabase_connected=is_healthy and settings.is_supabase_enabled,
        database_mode="Supabase Cloud" if (settings.is_supabase_enabled and is_healthy) else "Local SQLite",
        ai_active=settings.is_llm_enabled,
        ai_provider=settings.active_llm_provider,
        version=settings.version
    )

@router.post("/config")
async def update_config(req: ConfigUpdateRequest):
    """Dynamically update connection strings or AI API keys."""
    global _repo, _agent
    if req.supabase_url is not None:
        settings.supabase_url = req.supabase_url.strip().rstrip("/")
    if req.supabase_anon_key is not None:
        settings.supabase_anon_key = req.supabase_anon_key.strip()
    if req.gemini_api_key is not None:
        settings.gemini_api_key = req.gemini_api_key.strip()
    if req.openai_api_key is not None:
        settings.openai_api_key = req.openai_api_key.strip()

    # Reinitialize repo and agent with new settings
    _repo = get_repository(settings)
    _agent = AzureBuddyAgent(repository=_repo)

    status = await get_system_status(_repo)
    return {"status": "ok", "config_status": status}

@router.get("/sessions")
async def list_sessions(
    user_id: str = Depends(get_current_user_id),
    repo: BaseRepository = Depends(get_repo)
):
    """List private study sessions for the authenticated or anonymous user."""
    sessions = await repo.list_sessions(user_id=user_id, limit=30)
    return {"sessions": [s.model_dump() for s in sessions]}

@router.post("/sessions")
async def create_session(
    req: Optional[CreateSessionRequest] = None,
    user_id: str = Depends(get_current_user_id),
    repo: BaseRepository = Depends(get_repo)
):
    """Create a new private study session."""
    session_id = str(uuid.uuid4())
    title = req.title if req and req.title else "New Study Session"
    language = req.language if req and req.language else "English"
    effective_user_id = req.user_id if (req and req.user_id and req.user_id != "anonymous") else user_id
    session = await repo.create_session(
        session_id=session_id,
        title=title,
        language=language,
        user_id=effective_user_id
    )
    return session.model_dump()

@router.get("/sessions/{session_id}/messages")
async def get_session_messages(
    session_id: str,
    user_id: str = Depends(get_current_user_id),
    repo: BaseRepository = Depends(get_repo)
):
    """Retrieve message history for a session with ownership verification."""
    session = await repo.get_session(session_id, user_id=user_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found or unauthorized")
    messages = await repo.get_messages(session_id=session_id, limit=100)
    return {"messages": [m.model_dump() for m in messages]}

@router.delete("/sessions/{session_id}")
async def delete_session(
    session_id: str,
    user_id: str = Depends(get_current_user_id),
    repo: BaseRepository = Depends(get_repo)
):
    """Delete a session only if owned by the current user."""
    success = await repo.delete_session(session_id=session_id, user_id=user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Session not found or unauthorized")
    return {"status": "ok"}

@router.post("/chat", response_model=ChatResponse)
async def chat_interaction(
    req: ChatRequest,
    user_id: str = Depends(get_current_user_id),
    agent: AzureBuddyAgent = Depends(get_agent)
):
    """Process a user message within the user's private workspace."""
    effective_user_id = req.user_id if (req and req.user_id and req.user_id != "anonymous") else user_id
    reply_msg, intent = await agent.handle_message(
        session_id=req.session_id,
        user_text=req.message,
        client_lang=req.language,
        user_id=effective_user_id
    )
    return ChatResponse(message=reply_msg, intent=intent.value)
