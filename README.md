# Azure Buddy - AI Study Assistant & AZ-900 Tutor

An AI-powered, production-grade study assistant for the **Microsoft Certified: Azure Fundamentals (AZ-900)** exam (July 2026 skills outline), complete with East African analogies, multilingual tutoring (English, Kiswahili, Sheng), and full session persistence using **Supabase** (with automatic local SQLite fallback).

---

## High-Grade Modular Architecture

```
C:\Users\TPN\Desktop\Azure\
├── core/                       # Core agent & orchestration
│   ├── config.py               # Strongly typed settings & env loading
│   ├── models.py               # Domain models, enums & API schemas
│   └── agent.py                # AzureBuddyAgent orchestrator & intent router
├── knowledge/                  # AZ-900 2026 Knowledge Base
│   ├── questions.py            # 60 categorized practice questions with traps
│   ├── analogies.py            # Multilingual East African analogies
│   └── syllabus.py             # 2026 domain objectives & exam facts
├── repository/                 # Repository Pattern Persistence
│   ├── base.py                 # Abstract BaseRepository interface
│   ├── sqlite_repo.py          # Local SQLite storage & fallback
│   └── supabase_repo.py        # Supabase cloud REST client via httpx
├── api/                        # HTTP Interface
│   └── routes.py               # Clean FastAPI router (/api/chat, /api/sessions, etc.)
├── static/                     # Minimalist UI Assets
│   └── index.html              # Distraction-free interface with dynamic quiz dock
├── tests/                      # Automated Test Suite
│   └── test_agent.py           # Pytest integration tests
├── run_tests.py                # Standalone test runner
├── server.py                   # Slim FastAPI application entry point
├── supabase_schema.sql         # Production database migration
└── updated_scope_2026.md       # Official July 2026 exam outline reference
```

---

## Key Capabilities & Guardrails

1. **Deterministic Out-of-Scope Guardrail**:
   - If prompted outside the AZ-900 curriculum (e.g., AWS, GCP, AZ-104, general programming, sports, cooking), Azure Buddy politely apologizes and lists its exact exam capabilities in the user's active language.
2. **Stateful 5-Question Quiz Engine**:
   - 60 original AZ-900 questions mapped to July 2026 domains.
   - Built-in anti-spam protection: prevents re-evaluating or looping on submitted answers.
   - Dynamic UI dock controls (`[ A ] [ B ] [ C ] [ D ] [ Next → ]`) only render when answering/advancing questions.
3. **Language Context Retention**:
   - Seamlessly maintains conversation context in **English**, **Kiswahili**, or **Sheng** with relatable East African examples (Gikomba market, M-Pesa agents in CBD/Westlands, Thika Road matatus).
   - Official Azure terms remain in English and bolded (`**Availability Zone**`, `**Shared Responsibility Model**`).
4. **Cloud Database with Local Resilience**:
   - Connects to Supabase for multi-device sync with instant fallback to SQLite when working offline.

---

## Running the Application

### 1. Launch the Server
```powershell
python server.py
```
Open your browser at:
👉 **[http://localhost:8000](http://localhost:8000)**

### 2. Run the Automated Test Suite
```powershell
python run_tests.py
```

---

## Connecting Supabase & LLM Providers

- **Supabase**: Set `SUPABASE_URL` and `SUPABASE_ANON_KEY` in `.env` or in the web UI Settings dialog. Run `supabase_schema.sql` in your Supabase SQL Editor.
- **AI Providers**: Set `GEMINI_API_KEY` (Google Gemini 2.5 Flash) or `OPENAI_API_KEY` (GPT-4o-mini). If no API key is provided, the built-in intelligent study engine powers the entire experience completely offline.

---
*Unofficial AZ-900 study aid. Not affiliated with or endorsed by Microsoft. Always verify on Microsoft Learn.*
