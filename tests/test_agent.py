"""
Comprehensive unit and integration test suite for Azure Buddy AI.
Tests out-of-scope guardrail, anti-looping quiz validation, and language retention.
"""

import pytest
import asyncio
from pathlib import Path
import tempfile
import uuid

from core.models import AgentIntent, MessageRole
from core.agent import AzureBuddyAgent
from repository.sqlite_repo import SQLiteRepository

@pytest.fixture
def temp_repo():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        db_path = Path(f.name)
    repo = SQLiteRepository(db_path=db_path)
    yield repo
    if db_path.exists():
        try:
            db_path.unlink()
        except Exception:
            pass

@pytest.fixture
def agent(temp_repo):
    return AzureBuddyAgent(repository=temp_repo)

@pytest.mark.asyncio
async def test_out_of_scope_english(agent):
    session_id = str(uuid.uuid4())
    user_text = "How do I configure an AWS S3 bucket using Python?"
    msg, intent = await agent.handle_message(session_id, user_text, client_lang="English")

    assert intent == AgentIntent.OUT_OF_SCOPE
    assert "apologize" in msg.content.lower()
    assert "outside the scope" in msg.content.lower()
    assert "Cloud Concepts" in msg.content
    assert "Azure Architecture" in msg.content
    assert "Azure Management" in msg.content

@pytest.mark.asyncio
async def test_out_of_scope_sheng(agent):
    session_id = str(uuid.uuid4())
    # Switch to Sheng first
    await agent.handle_message(session_id, "Nieleze kwa Sheng", client_lang="Sheng")
    # Ask out-of-scope query
    msg, intent = await agent.handle_message(session_id, "Nipee tips za football na odds za kesho")

    assert intent == AgentIntent.OUT_OF_SCOPE
    assert "Pole sana buda" in msg.content
    assert "nje ya scope" in msg.content
    assert "Cloud Concepts" in msg.content

@pytest.mark.asyncio
async def test_anti_looping_quiz_validation(agent):
    session_id = str(uuid.uuid4())

    # 1. Start fresh quiz
    msg1, intent1 = await agent.handle_message(session_id, "Quiz me")
    assert intent1 == AgentIntent.QUIZ_START
    assert "Question 1/5" in msg1.content

    # 2. Answer question with 'B'
    msg2, intent2 = await agent.handle_message(session_id, "B")
    assert intent2 == AgentIntent.QUIZ_ANSWER
    assert ("CORRECT" in msg2.content or "NOT QUITE" in msg2.content)
    assert "Why:" in msg2.content

    # 3. Spam answer 'B' again immediately without clicking Next
    msg3, intent3 = await agent.handle_message(session_id, "B")
    assert intent3 == AgentIntent.QUIZ_ANSWER
    assert "already answered this question" in msg3.content.lower()

    # 4. Advance with 'Next'
    msg4, intent4 = await agent.handle_message(session_id, "Next")
    assert intent4 == AgentIntent.QUIZ_ADVANCE
    assert "Question 2/5" in msg4.content

@pytest.mark.asyncio
async def test_language_retention(agent):
    session_id = str(uuid.uuid4())

    # Switch to Sheng
    msg1, intent1 = await agent.handle_message(session_id, "Nieleze kwa Sheng na mifano ya mtaani")
    assert intent1 == AgentIntent.LANGUAGE_SWITCH
    assert "Niaje buda" in msg1.content

    # Follow up with "Cloud Concepts"
    msg2, intent2 = await agent.handle_message(session_id, "Cloud Concepts")
    assert intent2 == AgentIntent.SELECT_AREA
    # Should retain Sheng context and bold English terms
    assert "Uzito kwenye mtihani" in msg2.content or "mada" in msg2.content.lower()
    assert "**1.1**" in msg2.content

@pytest.mark.asyncio
async def test_concept_analogy_formatting(agent):
    session_id = str(uuid.uuid4())
    msg, intent = await agent.handle_message(session_id, "Explain the Shared Responsibility Model", client_lang="English")

    assert intent == AgentIntent.EXPLAIN_CONCEPT
    assert "Gikomba" in msg.content or "market" in msg.content
    assert "**Shared Responsibility Model**" in msg.content
    assert "Exam Tip" in msg.content
