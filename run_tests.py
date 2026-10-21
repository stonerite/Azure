"""
Comprehensive test runner for Azure Buddy AI.
Tests agent core logic, out-of-scope guardrail, anti-looping, and FastAPI HTTP API endpoints.
"""

import asyncio
from pathlib import Path
import tempfile
import uuid
import httpx

from core.models import AgentIntent
from core.agent import AzureBuddyAgent
from repository.sqlite_repo import SQLiteRepository
from server import app

async def run_all_tests():
    print("==================================================")
    print("Running Azure Buddy AI Test Suite")
    print("==================================================")
    
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        db_path = Path(f.name)
        
    repo = SQLiteRepository(db_path=db_path)
    agent = AzureBuddyAgent(repository=repo)
    passed = 0
    total = 0

    # Test 1: Out of Scope in English
    total += 1
    session_id = str(uuid.uuid4())
    msg, intent = await agent.handle_message(session_id, "How do I configure an AWS S3 bucket using Python?", client_lang="English")
    assert intent == AgentIntent.OUT_OF_SCOPE, f"Expected OUT_OF_SCOPE, got {intent}"
    assert "apologize" in msg.content.lower(), "Apology missing in English out-of-scope response"
    assert "Cloud Concepts" in msg.content, "Capabilities missing in out-of-scope response"
    passed += 1
    print(" [PASS] Test 1: Out of Scope Guardrail (English)")

    # Test 2: Out of Scope in Sheng
    total += 1
    session_id = str(uuid.uuid4())
    await agent.handle_message(session_id, "Nieleze kwa Sheng", client_lang="Sheng")
    msg, intent = await agent.handle_message(session_id, "Nipee tips za football na odds za kesho")
    assert intent == AgentIntent.OUT_OF_SCOPE, f"Expected OUT_OF_SCOPE, got {intent}"
    assert "Pole sana buda" in msg.content, "Sheng apology missing"
    assert "Cloud Concepts" in msg.content, "Sheng capabilities list missing"
    passed += 1
    print(" [PASS] Test 2: Out of Scope Guardrail (Sheng)")

    # Test 3: Anti-looping Quiz Validation
    total += 1
    session_id = str(uuid.uuid4())
    msg1, intent1 = await agent.handle_message(session_id, "Quiz me")
    assert intent1 == AgentIntent.QUIZ_START, f"Expected QUIZ_START, got {intent1}"
    assert "Question 1/5" in msg1.content, "Question header missing"

    msg2, intent2 = await agent.handle_message(session_id, "B")
    assert intent2 == AgentIntent.QUIZ_ANSWER, f"Expected QUIZ_ANSWER, got {intent2}"
    assert ("CORRECT" in msg2.content or "NOT QUITE" in msg2.content), "Answer evaluation missing"
    assert "Why:" in msg2.content, "Explanation missing"

    # Spam answer B again
    msg3, intent3 = await agent.handle_message(session_id, "B")
    assert intent3 == AgentIntent.QUIZ_ANSWER, f"Expected QUIZ_ANSWER, got {intent3}"
    assert "already answered this question" in msg3.content.lower(), "Spam warning missing"

    # Advance to question 2
    msg4, intent4 = await agent.handle_message(session_id, "Next")
    assert intent4 == AgentIntent.QUIZ_ADVANCE, f"Expected QUIZ_ADVANCE, got {intent4}"
    assert "Question 2/5" in msg4.content, "Did not advance to Question 2/5"
    passed += 1
    print(" [PASS] Test 3: Anti-Looping Quiz Validation & Advancement")

    # Test 4: Language Retention
    total += 1
    session_id = str(uuid.uuid4())
    msg_lang, intent_lang = await agent.handle_message(session_id, "Nieleze kwa Sheng na mifano ya mtaani")
    assert intent_lang == AgentIntent.LANGUAGE_SWITCH
    assert "Niaje buda" in msg_lang.content

    msg_area, intent_area = await agent.handle_message(session_id, "Cloud Concepts")
    assert intent_area == AgentIntent.SELECT_AREA
    assert ("Uzito kwenye mtihani" in msg_area.content or "mada" in msg_area.content.lower())
    assert "**1.1**" in msg_area.content
    passed += 1
    print(" [PASS] Test 4: Language Context Retention across Turns")

    # Test 5: Concept Analogy with East African Context
    total += 1
    session_id = str(uuid.uuid4())
    msg_concept, intent_concept = await agent.handle_message(session_id, "Explain the Shared Responsibility Model", client_lang="English")
    assert intent_concept == AgentIntent.EXPLAIN_CONCEPT
    assert "Gikomba" in msg_concept.content or "market" in msg_concept.content
    assert "**Shared Responsibility Model**" in msg_concept.content
    assert "Exam Tip" in msg_concept.content
    passed += 1
    print(" [PASS] Test 5: East African Concept Analogy Formatting")

    # Test 6: FastAPI HTTP Endpoints via ASGITransport
    total += 1
    from api.routes import get_repo, get_agent
    app.dependency_overrides[get_repo] = lambda: repo
    app.dependency_overrides[get_agent] = lambda: agent

    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        # GET /api/status
        status_res = await client.get("/api/status")
        assert status_res.status_code == 200, f"Status API failed: {status_res.text}"
        status_data = status_res.json()
        assert "database_mode" in status_data
        assert "version" in status_data

        # POST /api/sessions
        sess_res = await client.post("/api/sessions", json={"title": "Integration Test Session", "language": "English"})
        assert sess_res.status_code == 200
        sess_data = sess_res.json()
        api_sess_id = sess_data["id"]

        # POST /api/chat (Out-of-scope trigger)
        chat_res = await client.post("/api/chat", json={
            "session_id": api_sess_id,
            "message": "Write me a python script for AWS",
            "language": "English"
        })
        assert chat_res.status_code == 200
        chat_data = chat_res.json()
        assert chat_data["intent"] == "out_of_scope"
        assert "apologize" in chat_data["message"]["content"].lower()

        # GET /api/sessions/{session_id}/messages
        msgs_res = await client.get(f"/api/sessions/{api_sess_id}/messages")
        assert msgs_res.status_code == 200
        msgs = msgs_res.json()["messages"]
        assert len(msgs) == 2  # 1 user + 1 assistant

        # GET / (Serve UI)
        index_res = await client.get("/")
        assert index_res.status_code == 200
        assert "Azure Buddy" in index_res.text

    passed += 1
    print(" [PASS] Test 6: FastAPI HTTP Endpoints (/api/status, /api/sessions, /api/chat, /)")

    # Test 7: Multi-User Privacy & Zero Data Leak Isolation
    total += 1
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        user_a = "usr_alice_privacy_1"
        user_b = "usr_bob_privacy_2"

        # Alice creates a private session
        alice_create = await client.post(
            "/api/sessions",
            headers={"X-User-Id": user_a},
            json={"title": "Alice Private Azure Notes", "language": "English"}
        )
        assert alice_create.status_code == 200
        alice_session_id = alice_create.json()["id"]

        # Alice chats in her session
        await client.post(
            "/api/chat",
            headers={"X-User-Id": user_a},
            json={"session_id": alice_session_id, "message": "Explain Availability Zones", "language": "English"}
        )

        # Bob lists sessions with his own user id
        bob_list = await client.get("/api/sessions", headers={"X-User-Id": user_b})
        assert bob_list.status_code == 200
        bob_sessions = [s["id"] for s in bob_list.json()["sessions"]]
        assert alice_session_id not in bob_sessions, "Data Leak: Bob can see Alice's session in his list!"

        # Bob tries to directly read Alice's message history by guessing session ID
        bob_peek = await client.get(f"/api/sessions/{alice_session_id}/messages", headers={"X-User-Id": user_b})
        assert bob_peek.status_code == 404, "Data Leak: Bob accessed Alice's private messages!"

        # Bob tries to delete Alice's session
        bob_delete = await client.delete(f"/api/sessions/{alice_session_id}", headers={"X-User-Id": user_b})
        assert bob_delete.status_code == 404, "Security issue: Bob was able to delete Alice's session!"

        # Alice can still access her session
        alice_read = await client.get(f"/api/sessions/{alice_session_id}/messages", headers={"X-User-Id": user_a})
        assert alice_read.status_code == 200
        assert len(alice_read.json()["messages"]) >= 2

    passed += 1
    print(" [PASS] Test 7: Multi-User Workspace Privacy & Zero Data Leak Isolation")

    # Cleanup
    if db_path.exists():
        try:
            db_path.unlink()
        except Exception:
            pass

    print("==================================================")
    print(f"Results: {passed}/{total} tests passed successfully!")
    print("==================================================")

if __name__ == "__main__":
    asyncio.run(run_all_tests())
