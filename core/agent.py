"""
Azure Buddy AI Agent Orchestrator.
Coordinates intent classification, out-of-scope guardrails, stateful quiz engine,
East African analogies, LLM routing (Gemini / OpenAI), and repository persistence.
"""

import re
import uuid
import random
import logging
from typing import Optional, Dict, Any, List, Tuple
from datetime import datetime, timezone
import httpx

from core.config import settings
from core.models import (
    Message, MessageRole, AgentIntent, QuizState, QuizAttempt, Session
)
from knowledge.questions import QUESTIONS
from knowledge.analogies import ANALOGIES, get_concept_explanation
from knowledge.syllabus import SYLLABUS, EXAM_FACTS, get_area_summary
from repository.base import BaseRepository

logger = logging.getLogger("azure_buddy.agent")

# Read system prompt once
SYSTEM_PROMPT_PATH = settings.base_dir / "azure_buddy_system_prompt.md"
if SYSTEM_PROMPT_PATH.exists():
    with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
        SYSTEM_PROMPT = f.read()
else:
    SYSTEM_PROMPT = "You are Azure Buddy, an unofficial AZ-900 study assistant using simple language and East African analogies."

OUT_OF_SCOPE_KEYWORDS = [
    "az-104", "az-204", "az-400", "az-500", "sc-900", "ms-900", "dp-900", "ai-900",
    "aws", "amazon web services", "ec2", "s3 bucket", "lambda", "gcp", "google cloud",
    "python script", "javascript", "react", "html code", "css style", "django", "flask",
    "write an essay", "homework", "weather in", "football", "who won", "recipe", "song lyrics",
    "crypto", "bitcoin", "solana", "stock market"
]

class AzureBuddyAgent:
    def __init__(self, repository: BaseRepository):
        self.repo = repository
        self._quiz_states: Dict[str, QuizState] = {}

    def get_quiz_state(self, session_id: str, default_lang: str = "English") -> QuizState:
        if session_id not in self._quiz_states:
            self._quiz_states[session_id] = QuizState(language=default_lang)
        return self._quiz_states[session_id]

    def reset_quiz_state(self, session_id: str, lang: Optional[str] = None) -> QuizState:
        current_lang = lang or (self._quiz_states[session_id].language if session_id in self._quiz_states else "English")
        state = QuizState(
            mode="quiz",
            language=current_lang,
            question_index=0,
            total_questions=5,
            score=0,
            asked_ids=[],
            missed_topics=[],
            current_question=None,
            last_answered_id=None
        )
        self._quiz_states[session_id] = state
        return state

    def classify_intent(self, text: str, state: QuizState) -> AgentIntent:
        lower = text.strip().lower()

        # 1. Out of Scope Check
        if any(k in lower for k in OUT_OF_SCOPE_KEYWORDS):
            return AgentIntent.OUT_OF_SCOPE

        # 2. Language Switch Check
        if any(w in lower for w in ["in sheng", "kwa sheng", "nieleze kwa sheng", "sheng please", "in kiswahili", "kwa kiswahili", "in english"]):
            return AgentIntent.LANGUAGE_SWITCH

        # 3. Quiz Start / Restart
        if any(k in lower for k in [
            "start quiz", "new test", "fresh test", "start fresh", "take a test",
            "take test", "quiz me", "practice question", "start new test"
        ]):
            return AgentIntent.QUIZ_START

        # 4. Quiz Advance (Next Question)
        if lower in ["next", "next question", "continue", "next please", "proceed", "move on", "endelea", "songa"]:
            if state.mode == "quiz":
                return AgentIntent.QUIZ_ADVANCE

        # 5. Quiz Answer Selection (A, B, C, D)
        # Matches single letters or "A.", "Choice B", etc.
        opt_match = re.match(r"^(?:choice\s+|option\s+)?([a-d])[\.\)]?$", lower)
        if opt_match and state.mode == "quiz":
            return AgentIntent.QUIZ_ANSWER

        # 6. Area Selection
        if any(a in lower for a in ["cloud concept", "cloud concepts", "architecture", "governance", "cost management"]):
            return AgentIntent.SELECT_AREA

        # 7. Concept Explanation
        if any(c in lower for c in [
            "shared responsibility", "availability zone", "region", "zone", "iaas", "paas", "saas",
            "scalability", "elasticity", "policy", "rbac", "resource group", "resource lock",
            "pricing calculator", "tco", "entra"
        ]):
            return AgentIntent.EXPLAIN_CONCEPT

        return AgentIntent.GENERAL_CHAT

    def get_out_of_scope_message(self, lang: str) -> str:
        """Polite apology and exact capabilities list."""
        if lang.lower() == "sheng":
            return (
                "Pole sana buda, lakini hiyo iko nje ya scope ya mtihani wa **AZ-900 (Microsoft Azure Fundamentals)**.\n\n"
                "Hapa ndio madini ninayoweza kukugawia:\n"
                "- **Cloud Concepts**: Shared Responsibility Model, IaaS, PaaS, SaaS, na CapEx vs OpEx.\n"
                "- **Azure Architecture & Services**: Regions, Availability Zones, Virtual Machines, na Storage.\n"
                "- **Management & Governance**: Pricing Calculator, Azure Policy, Resource Locks, na Monitoring.\n"
                "- **Practice Quizzes**: Maswali ya kujipima ya AZ-900 yenye mitego na majibu yake (sema **'Quiz me'**).\n"
                "- **Mifano ya Mtaani**: Kuelewa cloud kwa mifano halisi ya Afrika Mashariki.\n\n"
                "Tuchambue mada gani ya AZ-900 sasa, au nikupe swali (sema **'Quiz me'**)? 🚀"
            )
        elif lang.lower() in ["kiswahili", "swahili"]:
            return (
                "Samahani sana, lakini mada hiyo iko nje ya wigo wa mtihani wa **AZ-900 (Microsoft Azure Fundamentals)**.\n\n"
                "Hapa kuna yale ninayoweza kukusaidia nayo:\n"
                "- **Cloud Concepts**: Shared Responsibility Model, IaaS, PaaS, SaaS, na mifumo ya gharama.\n"
                "- **Azure Architecture and Services**: Regions, Availability Zones, Virtual Machines, na Storage.\n"
                "- **Azure Management and Governance**: Azure Policy, Resource Locks, na Pricing Calculator.\n"
                "- **Mitihani ya Majaribio**: Maswali halisi ya kujipima ya mtindo wa mtihani (sema **'Quiz me'**).\n"
                "- **Mifano Rahisi**: Maelezo fasaha yenye mifano halisi ya maisha yetu ya kila siku kwa Kiswahili na Sheng.\n\n"
                "Je, ungependa tujifunze mada ipi ya AZ-900, au ujaribu swali la mtihani (sema **'Quiz me'**)? ✨"
            )
        else:
            return (
                "I apologize, but that is outside the scope of the **AZ-900 (Microsoft Azure Fundamentals)** exam.\n\n"
                "Here is what I can help you with:\n"
                "- **Cloud Concepts**: Shared Responsibility Model, IaaS / PaaS / SaaS, Cloud Models, and CapEx vs OpEx.\n"
                "- **Azure Architecture and Services**: Regions, Availability Zones, Virtual Machines, Storage Tiers, and Networking.\n"
                "- **Azure Management and Governance**: Cost Management, Azure Policy, Resource Locks, and Monitoring tools.\n"
                "- **Practice Tests**: Original multiple-choice questions to test your exam readiness (say **'Quiz me'**).\n"
                "- **Relatable Analogies**: Explanations in English, Kiswahili, or Sheng with East African examples.\n\n"
                "Which AZ-900 area would you like to explore, or should we take a quick quiz (say **'Quiz me'**)?"
            )

    def _format_question(self, q_item: Dict[str, Any], index: int, total: int, lang: str) -> str:
        options_text = "\n".join([f"**{opt}.** {text}" for opt, text in q_item["options"].items()])
        prompt_instruction = "Reply with your choice (**A**, **B**, **C**, or **D**) to check your answer!"
        if lang.lower() == "sheng":
            prompt_instruction = "Jibu na (**A**, **B**, **C**, au **D**) tuone kama umegonga ndipo!"
        elif lang.lower() in ["kiswahili", "swahili"]:
            prompt_instruction = "Jibu kwa herufi (**A**, **B**, **C**, au **D**) ili kuthibitisha jibu lako!"

        return (
            f"### 📝 Question {index}/{total}\n"
            f"**Skill Area:** {q_item['area']} | `{q_item['tag']}`\n\n"
            f"**{q_item['q']}**\n\n"
            f"{options_text}\n\n"
            f"👉 {prompt_instruction}"
        )

    def _pick_next_question(self, state: QuizState) -> Optional[Dict[str, Any]]:
        remaining = [q for q in QUESTIONS if q["id"] not in state.asked_ids]
        if not remaining:
            remaining = QUESTIONS
        chosen = random.choice(remaining)
        state.asked_ids.append(chosen["id"])
        state.current_question = chosen
        state.last_answered_id = None
        state.question_index += 1
        return chosen

    async def _call_llm(self, user_text: str, history: List[Message], language: str) -> Optional[str]:
        """Route to Gemini or OpenAI if configured and healthy."""
        # 1. Try Gemini
        if settings.gemini_api_key:
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={settings.gemini_api_key}"
                contents = []
                for m in history[-8:]:
                    role = "user" if m.role == MessageRole.USER else "model"
                    contents.append({"role": role, "parts": [{"text": m.content}]})
                contents.append({"role": "user", "parts": [{"text": user_text}]})

                sys_instruction = (
                    f"{SYSTEM_PROMPT}\n\n"
                    f"ACTIVE USER LANGUAGE PREFERENCE: {language}.\n"
                    f"Rule reminder: Keep official Azure terms in English and bold (e.g. **Availability Zone**). "
                    f"If asked out of scope, apologize politely and list capabilities."
                )

                payload = {
                    "systemInstruction": {"parts": [{"text": sys_instruction}]},
                    "contents": contents,
                    "generationConfig": {"temperature": 0.4, "maxOutputTokens": 800}
                }
                async with httpx.AsyncClient(timeout=20.0) as client:
                    res = await client.post(url, json=payload)
                    if res.status_code == 200:
                        data = res.json()
                        candidates = data.get("candidates", [])
                        if candidates and "content" in candidates[0]:
                            parts = candidates[0]["content"].get("parts", [])
                            if parts and "text" in parts[0]:
                                return parts[0]["text"]
            except Exception as e:
                logger.warning(f"Gemini API call failed: {e}")

        # 2. Try OpenAI
        if settings.openai_api_key:
            try:
                url = "https://api.openai.com/v1/chat/completions"
                messages = [{
                    "role": "system",
                    "content": f"{SYSTEM_PROMPT}\n\nACTIVE USER LANGUAGE PREFERENCE: {language}."
                }]
                for m in history[-8:]:
                    messages.append({"role": m.role.value, "content": m.content})
                messages.append({"role": "user", "content": user_text})

                payload = {
                    "model": "gpt-4o-mini",
                    "messages": messages,
                    "temperature": 0.4
                }
                headers = {"Authorization": f"Bearer {settings.openai_api_key}"}
                async with httpx.AsyncClient(timeout=20.0) as client:
                    res = await client.post(url, headers=headers, json=payload)
                    if res.status_code == 200:
                        return res.json()["choices"][0]["message"]["content"]
            except Exception as e:
                logger.warning(f"OpenAI API call failed: {e}")

        return None

    async def handle_message(
        self,
        session_id: str,
        user_text: str,
        client_lang: Optional[str] = None,
        user_id: str = "anonymous"
    ) -> Tuple[Message, AgentIntent]:
        """Main agent interaction pipeline."""
        # 1. Fetch Session and State
        session = await self.repo.get_session(session_id, user_id=user_id)
        if not session:
            session = await self.repo.create_session(
                session_id=session_id,
                title="New Study Session",
                language=client_lang or "English",
                user_id=user_id
            )

        active_lang = client_lang or session.language or "English"
        state = self.get_quiz_state(session_id, default_lang=active_lang)

        # 2. Detect Explicit Language Switching
        lower = user_text.lower().strip()
        if "sheng" in lower:
            active_lang = "Sheng"
        elif "kiswahili" in lower or "swahili" in lower:
            active_lang = "Kiswahili"
        elif "english" in lower and "in english" in lower:
            active_lang = "English"

        state.language = active_lang
        if session.language != active_lang:
            await self.repo.update_session(session_id, language=active_lang, user_id=user_id)

        # 3. Classify Intent
        intent = self.classify_intent(user_text, state)

        # 4. Save User Message
        user_msg = Message(
            id=str(uuid.uuid4()),
            session_id=session_id,
            role=MessageRole.USER,
            content=user_text,
            metadata={"intent": intent.value, "language": active_lang}
        )
        await self.repo.save_message(user_msg)

        # 5. Route by Intent

        # A) OUT OF SCOPE
        if intent == AgentIntent.OUT_OF_SCOPE:
            reply_text = self.get_out_of_scope_message(active_lang)
            msg = await self._save_assistant_reply(session_id, reply_text, intent, active_lang)
            return msg, intent

        # B) LANGUAGE SWITCH CONFIRMATION
        if intent == AgentIntent.LANGUAGE_SWITCH:
            if active_lang == "Sheng":
                reply_text = (
                    "Niaje buda! Tuko fiti sana. Kuanzia sasa nitakugawia maneno ya Azure na mifano ya mtaani kama matatu za Thika Road, maduka za M-Pesa, na stoo za Gikomba.\n\n"
                    "Unataka tuchambue nini leo:\n"
                    "- **Cloud Concepts** (Uzito 25-30%)\n"
                    "- **Architecture and Services** (Uzito 35-40%)\n"
                    "- **Governance and Cost Management** (Uzito 30-35%)\n\n"
                    "Au unataka nikupe swali (sema **'Quiz me'**)? 🚀"
                )
            elif active_lang == "Kiswahili":
                reply_text = (
                    "Habari! Kuanzia sasa tutajifunza mtihani wa AZ-900 kwa lugha fasaha ya Kiswahili yenye mifano halisi ya maisha yetu ya kila siku ya Afrika Mashariki.\n\n"
                    "Tunaweza kuanzia wapi leo:\n"
                    "- **Cloud Concepts** (Misingi ya Cloud)\n"
                    "- **Architecture and Services** (Muundo na Huduma za Azure)\n"
                    "- **Governance and Cost Management** (Utawala na Usimamizi wa Gharama)\n\n"
                    "Au ungependa swali la kujipima (sema **'Quiz me'**)? ✨"
                )
            else:
                reply_text = (
                    "Switched to English! I'll guide you through the AZ-900 syllabus with clear East African analogies.\n\n"
                    "Where would you like to begin:\n"
                    "- **Cloud Concepts** (25-30%)\n"
                    "- **Architecture and Services** (35-40%)\n"
                    "- **Management and Governance** (30-35%)\n\n"
                    "Or say **'Quiz me'** to take a 5-question test! 🚀"
                )
            msg = await self._save_assistant_reply(session_id, reply_text, intent, active_lang)
            return msg, intent

        # C) QUIZ START
        if intent == AgentIntent.QUIZ_START:
            state = self.reset_quiz_state(session_id, active_lang)
            q = self._pick_next_question(state)
            greeting = "Niaje buda! Tuanze test mpya ya maswali tano ya AZ-900 mara moja." if active_lang == "Sheng" else (
                "Habari! Tuanze mtihani wa maswali 5 ya AZ-900 mara moja." if active_lang == "Kiswahili" else
                "Awesome! Let's start a fresh 5-question AZ-900 practice test."
            )
            q_formatted = self._format_question(q, state.question_index, state.total_questions, active_lang)
            reply_text = f"{greeting}\n\n{q_formatted}"
            msg = await self._save_assistant_reply(session_id, reply_text, intent, active_lang)
            return msg, intent

        # D) QUIZ ANSWER
        if intent == AgentIntent.QUIZ_ANSWER:
            opt_match = re.match(r"^(?:choice\s+|option\s+)?([a-d])[\.\)]?$", lower)
            choice = opt_match.group(1).upper() if opt_match else "A"

            # Anti-looping check: Is there an active question awaiting answer?
            if state.current_question is None:
                # User is replying with an option when question was already answered!
                warn = (
                    "Ushajibu hili swali buda! Bonyeza **'Next'** twende mbele, au sema **'Start new test'** kuanza upya." if active_lang == "Sheng" else
                    "Umekwisha jibu swali hili! Bonyeza **'Next'** ili kuendelea na swali linalofuata, au sema **'Start new test'** kuanza upya." if active_lang == "Kiswahili" else
                    "You've already answered this question! Click **'Next'** to proceed, or say **'Start new test'** to reset."
                )
                msg = await self._save_assistant_reply(session_id, warn, intent, active_lang)
                return msg, intent

            # Evaluate Answer
            q = state.current_question
            is_correct = (choice == q["ans"])

            # Record attempt
            attempt = QuizAttempt(
                id=str(uuid.uuid4()),
                session_id=session_id,
                question_id=q["id"],
                topic=q["tag"],
                selected_option=choice,
                is_correct=is_correct
            )
            await self.repo.save_quiz_attempt(attempt)

            # Update State
            if is_correct:
                state.score += 1
                result_banner = (
                    "🔥 **SAFI SANA! Umepata (Correct)!**" if active_lang == "Sheng" else
                    "🎉 **SAFI SANA! Jibu lako ni SAHIHI!**" if active_lang == "Kiswahili" else
                    "🎉 **CORRECT! Outstanding work!**"
                )
            else:
                state.missed_topics.append(q["tag"])
                result_banner = (
                    f"❌ **BADO KIDOGO!** Jibu sahihi lilikuwa **{q['ans']}**." if active_lang == "Sheng" else
                    f"❌ **SI SAHIHI!** Jibu sahihi ni **{q['ans']}**." if active_lang == "Kiswahili" else
                    f"❌ **NOT QUITE!** The correct answer was **{q['ans']}**."
                )

            trap_explanation = ""
            if not is_correct and choice in q.get("traps", {}):
                trap_explanation = f"\n\n**⚠️ Trap Analysis:** {q['traps'][choice]}"

            # Next step prompt
            if state.question_index < state.total_questions:
                next_prompt = (
                    f"Bonyeza **'Next'** kuona swali linalofuata ({state.question_index + 1}/{state.total_questions})!" if active_lang == "Sheng" else
                    f"Bonyeza **'Next'** ili kuona swali linalofuata ({state.question_index + 1}/{state.total_questions})!" if active_lang == "Kiswahili" else
                    f"Click **'Next'** to proceed to question {state.question_index + 1}/{state.total_questions}!"
                )
            else:
                next_prompt = (
                    "Bonyeza **'Next'** kuona matokeo yako ya jumla ya mtihani huu!" if active_lang == "Sheng" else
                    "Bonyeza **'Next'** kuona matokeo yako ya jumla ya mtihani!" if active_lang == "Kiswahili" else
                    "Click **'Next'** to see your complete quiz results summary!"
                )

            reply_text = (
                f"{result_banner}\n\n"
                f"**Why:** {q['why']}"
                f"{trap_explanation}\n\n"
                f"👉 {next_prompt}"
            )

            # Mark question as answered
            state.last_answered_id = q["id"]
            state.current_question = None

            msg = await self._save_assistant_reply(session_id, reply_text, intent, active_lang)
            return msg, intent

        # E) QUIZ ADVANCE
        if intent == AgentIntent.QUIZ_ADVANCE:
            if state.question_index >= state.total_questions:
                # Show Test Summary
                pct = round((state.score / state.total_questions) * 100)
                passed = (state.score >= 4)  # 80%+ passes 700 threshold

                if active_lang == "Sheng":
                    summary = (
                        f"### 🏁 Mtihani Umekamilika (Quiz Finished)!\n\n"
                        f"**Alama Zako:** {state.score}/{state.total_questions} ({pct}%)\n\n"
                    )
                    if passed:
                        summary += "🏆 **Wewe ni mnoma sana!** Ukipiga hivi kwa mtihani wa AZ-900, unafika alama ya 700+ bila jasho!\n\n"
                    else:
                        summary += "💪 **Bidii kidogo tu buda!** Mtihani wa AZ-900 unahitaji alama 700/1000 ili kupita.\n\n"

                    if state.missed_topics:
                        summary += "**Mada za kupitia tena:**\n" + "\n".join([f"- `{t}`" for t in set(state.missed_topics)]) + "\n\n"
                    summary += "Unataka mtihani mwingine mpya (sema **'Quiz me'**) au tuchambue mada maalum?"
                elif active_lang == "Kiswahili":
                    summary = (
                        f"### 🏁 Matokeo ya Mtihani (Quiz Finished)!\n\n"
                        f"**Alama Zako:** {state.score}/{state.total_questions} ({pct}%)\n\n"
                    )
                    if passed:
                        summary += "🏆 **Hongera sana!** Kiwango chako cha maarifa kiko juu sana na uko tayari kwa mtihani wa AZ-900!\n\n"
                    else:
                        summary += "💪 **Kazi nzuri, ongeza juhudi kidogo!** Mtihani wa AZ-900 unahitaji alama 700 (takriban 70%) ili kufaulu.\n\n"

                    if state.missed_topics:
                        summary += "**Mada za kurudia kusoma:**\n" + "\n".join([f"- `{t}`" for t in set(state.missed_topics)]) + "\n\n"
                    summary += "Je, ungependa mtihani mwingine (sema **'Quiz me'**) au maelezo ya mada yoyote?"
                else:
                    summary = (
                        f"### 🏁 Practice Test Complete!\n\n"
                        f"**Your Score:** {state.score}/{state.total_questions} ({pct}%)\n\n"
                    )
                    if passed:
                        summary += "🏆 **Great job!** You demonstrated strong mastery across the tested AZ-900 objectives (Passing score is 700/1000).\n\n"
                    else:
                        summary += "💪 **Good practice effort!** Review the topics below to ensure you consistently score above the 700 passing mark.\n\n"

                    if state.missed_topics:
                        summary += "**Topics to review:**\n" + "\n".join([f"- `{t}`" for t in set(state.missed_topics)]) + "\n\n"
                    summary += "Would you like another 5-question test (say **'Quiz me'**), or should we review a specific concept?"

                state.mode = "idle"
                msg = await self._save_assistant_reply(session_id, summary, intent, active_lang)
                return msg, intent
            else:
                # Next Question
                q = self._pick_next_question(state)
                q_formatted = self._format_question(q, state.question_index, state.total_questions, active_lang)
                msg = await self._save_assistant_reply(session_id, q_formatted, intent, active_lang)
                return msg, intent

        # F) CONCEPT EXPLANATION
        if intent == AgentIntent.EXPLAIN_CONCEPT:
            concept_key = None
            if "shared responsibility" in lower:
                concept_key = "shared_responsibility"
            elif any(k in lower for k in ["availability zone", "region", "zone"]):
                concept_key = "regions_and_zones"
            elif any(k in lower for k in ["iaas", "paas", "saas"]):
                concept_key = "iaas_paas_saas"
            elif any(k in lower for k in ["scalability", "elasticity"]):
                concept_key = "elasticity_and_scalability"
            elif any(k in lower for k in ["policy", "rbac"]):
                concept_key = "policy_vs_rbac"

            if concept_key:
                explanation = get_concept_explanation(concept_key, active_lang)
                if explanation:
                    msg = await self._save_assistant_reply(session_id, explanation, intent, active_lang)
                    return msg, intent

        # G) SELECT AREA SYLLABUS
        if intent == AgentIntent.SELECT_AREA:
            area_key = "area_1"
            if "architecture" in lower:
                area_key = "area_2"
            elif any(k in lower for k in ["governance", "cost", "management"]):
                area_key = "area_3"

            area_summary = get_area_summary(area_key, active_lang)
            msg = await self._save_assistant_reply(session_id, area_summary, intent, active_lang)
            return msg, intent

        # H) ROUTE TO LLM IF ACTIVE
        history = await self.repo.get_messages(session_id, limit=10)
        llm_reply = await self._call_llm(user_text, history, active_lang)
        if llm_reply:
            msg = await self._save_assistant_reply(session_id, llm_reply, intent, active_lang)
            return msg, intent

        # I) DETERMINISTIC GENERAL CHAT FALLBACK
        fallback_reply = self._build_general_fallback(active_lang)
        msg = await self._save_assistant_reply(session_id, fallback_reply, intent, active_lang)
        return msg, intent

    def _build_general_fallback(self, lang: str) -> str:
        if lang.lower() == "sheng":
            return (
                "Niaje buda! Karibu tena kwenye **Azure Buddy**.\n\n"
                "Hapa ndio madini tunayoweza kuchambua leo:\n"
                "- Sema **'Cloud Concepts'** tuchambue IaaS, PaaS, SaaS na Shared Responsibility.\n"
                "- Sema **'Architecture'** tuchambue Regions, Availability Zones na Storage.\n"
                "- Sema **'Governance'** tuchambue Azure Policy, Resource Locks na Pricing.\n"
                "- Sema **'Quiz me'** nikupe maswali 5 ya mazoezi ya mtihani wa AZ-900!\n\n"
                "Unataka tuanzie wapi leo?"
            )
        elif lang.lower() in ["kiswahili", "swahili"]:
            return (
                "Habari! Karibu kwenye **Azure Buddy**, mwongozo wako wa kujisomea mtihani wa AZ-900.\n\n"
                "Mambo tunayoweza kufanya sasa hivi:\n"
                "- Sema **'Cloud Concepts'** au **'Shared Responsibility'** kupata maelezo na mifano halisi.\n"
                "- Sema **'Architecture'** kupata maelezo kuhusu Regions na Availability Zones.\n"
                "- Sema **'Quiz me'** au **'Start new test'** kufanya majaribio ya mtihani wa AZ-900.\n\n"
                "Je, ungependa tuanze na nini leo?"
            )
        else:
            return (
                "Habari! I'm **Azure Buddy**, your unofficial AZ-900 study partner.\n\n"
                "Here is what we can do together right now:\n"
                "- Say **'Quiz me'** or **'Start new test'** to take a fresh 5-question AZ-900 practice test!\n"
                "- Ask: *'Explain the Shared Responsibility Model'* (Market stall analogy)\n"
                "- Ask: *'Explain Availability Zones'* (M-Pesa shops analogy)\n"
                "- Ask: *'Explain IaaS vs PaaS vs SaaS'* (Cooking vs Restaurant analogy)\n"
                "- Switch language: Say *'Explain in Sheng'* or *'Kwa Kiswahili'*\n\n"
                "Which area would you like to explore?"
            )

    async def _save_assistant_reply(self, session_id: str, content: str, intent: AgentIntent, lang: str) -> Message:
        msg = Message(
            id=str(uuid.uuid4()),
            session_id=session_id,
            role=MessageRole.ASSISTANT,
            content=content,
            metadata={"intent": intent.value, "language": lang}
        )
        return await self.repo.save_message(msg)
