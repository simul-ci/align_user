"""
src/prompts — Prompt templates for AlignUSER / AlignUSER+.

This package contains all prompt strings used in the AlignUSER paper implementation:
- World-model next-state prediction
- Counterfactual action generation + reflection (trajectory and item-level)
- Page-level screening ([WATCH]/[SKIP]) + action selection
- AlignUSER+ causal validation (optionally using retrieved KG-memory evidence)
- Post-interview satisfaction scoring
- Believability + evaluator prompts used for analysis
- Persona formatting and matching prompts
- Page/state format templates
- Memory entry format templates
- KG retrieval query generation
"""

from __future__ import annotations

# Persona
from .persona import (
    PERSONA_PROMPT,
    build_persona_prompt,
)

# Page formats
from .page_formats import (
    PAGE_FORMAT_RECOMMENDATION,
    PAGE_ITEM_FORMAT_RECOMMENDATION,
    build_page_recommendation,
    PAGE_FORMAT_OPERA,
    PAGE_PRODUCT_FORMAT_OPERA,
    build_page_opera,
)

# Memory entry formats
from .memory_formats import (
    MEMORY_ENTRY_LIKED,
    MEMORY_ENTRY_DISLIKED,
    MEMORY_ENTRY_NEUTRAL,
    build_memory_entry,
)

# Core prompts
from .world_model import WORLD_MODEL_NEXT_STATE_PROMPT
from .counterfactual_action_generation import COUNTERFACTUAL_ACTION_GENERATION_PROMPT
from .counterfactual_reflection import COUNTERFACTUAL_REFLECTION_PROMPT
from .item_level_counterfactual_reflection import ITEM_LEVEL_COUNTERFACTUAL_REFLECTION_PROMPT
from .item_screening import ITEM_SCREENING_PROMPT, build_item_screening_prompt
from .action_selection import ACTION_SELECTION_PROMPT, build_action_selection_prompt
from .causal_validation import CAUSAL_VALIDATION_PROMPT
from .post_interview_satisfaction import (
    POST_INTERVIEW_SATISFACTION_PROMPT,
    build_post_interview_satisfaction_prompt,
)
from .believability import BELIEVABILITY_RECOMMENDED_LIST_PROMPT
from .llm_evaluator import LLM_EVALUATOR_PROMPT

# Persona matching
from .persona_generation import PERSONA_GENERATION_PROMPT
from .persona_matching import PERSONA_MATCHING_PROMPT

# KG retrieval (AlignUSER+)
from .kg_query_generation import KG_QUERY_GENERATION_PROMPT

# Parsers
from .parsers import (
    parse_best_action,
    parse_final_action,
    parse_post_interview_satisfaction,
)

# Registry
from .registry import PROMPT_REGISTRY

__all__ = [
    # Persona
    "PERSONA_PROMPT",
    "build_persona_prompt",
    # Page formats
    "PAGE_FORMAT_RECOMMENDATION",
    "PAGE_ITEM_FORMAT_RECOMMENDATION",
    "build_page_recommendation",
    "PAGE_FORMAT_OPERA",
    "PAGE_PRODUCT_FORMAT_OPERA",
    "build_page_opera",
    # Memory formats
    "MEMORY_ENTRY_LIKED",
    "MEMORY_ENTRY_DISLIKED",
    "MEMORY_ENTRY_NEUTRAL",
    "build_memory_entry",
    # Core prompts
    "WORLD_MODEL_NEXT_STATE_PROMPT",
    "COUNTERFACTUAL_ACTION_GENERATION_PROMPT",
    "COUNTERFACTUAL_REFLECTION_PROMPT",
    "ITEM_LEVEL_COUNTERFACTUAL_REFLECTION_PROMPT",
    "ITEM_SCREENING_PROMPT",
    "build_item_screening_prompt",
    "ACTION_SELECTION_PROMPT",
    "build_action_selection_prompt",
    "CAUSAL_VALIDATION_PROMPT",
    "POST_INTERVIEW_SATISFACTION_PROMPT",
    "build_post_interview_satisfaction_prompt",
    "BELIEVABILITY_RECOMMENDED_LIST_PROMPT",
    "LLM_EVALUATOR_PROMPT",
    # Persona matching
    "PERSONA_GENERATION_PROMPT",
    "PERSONA_MATCHING_PROMPT",
    # KG retrieval
    "KG_QUERY_GENERATION_PROMPT",
    # Parsers
    "parse_best_action",
    "parse_final_action",
    "parse_post_interview_satisfaction",
    # Registry
    "PROMPT_REGISTRY",
]
