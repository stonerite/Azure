"""
Knowledge base modules for Azure Buddy AI.
"""

from .questions import QUESTIONS
from .analogies import ANALOGIES, get_concept_explanation, list_concept_topics
from .syllabus import SYLLABUS, EXAM_FACTS, get_area_summary

__all__ = [
    "QUESTIONS",
    "ANALOGIES",
    "get_concept_explanation",
    "list_concept_topics",
    "SYLLABUS",
    "EXAM_FACTS",
    "get_area_summary"
]
