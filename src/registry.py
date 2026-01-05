"""
Prompt registry for easy lookup by name.
"""

from __future__ import annotations

from typing import Dict

from .persona import PERSONA_PROMPT
from .page_formats import (
    PAGE_FORMAT_RECOMMENDATION,
    PAGE_ITEM_FORMAT_RECOMMENDATION,
    PAGE_FORMAT_OPERA,
    PAGE_PRODUCT_FORMAT_OPERA,
)
from .memory_formats import (
    MEMORY_ENTRY_LIKED,
    MEMORY_ENTRY_DISLIKED,
    MEMORY_ENTRY_NEUTRAL,
)
from .world_model import WORLD_MODEL_NEXT_STATE_PROMPT
from .counterfactual_action_generation import COUNTERFACTUAL_ACTION_GENERATION_PROMPT
from .counterfactual_reflection import COUNTERFACTUAL_REFLECTION_PROMPT
from .item_level_counterfactual_reflection import ITEM_LEVEL_COUNTERFACTUAL_REFLECTION_PROMPT
from .item_screening import ITEM_SCREENING_PROMPT
from .action_selection import ACTION_SELECTION_PROMPT
from .causal_validation import CAUSAL_VALIDATION_PROMPT
from .post_interview_satisfaction import POST_INTERVIEW_SATISFACTION_PROMPT
from .believability import BELIEVABILITY_RECOMMENDED_LIST_PROMPT
from .llm_evaluator import LLM_EVALUATOR_PROMPT
from .persona_generation import PERSONA_GENERATION_PROMPT
from .persona_matching import PERSONA_MATCHING_PROMPT
from .kg_query_generation import KG_QUERY_GENERATION_PROMPT


PROMPT_REGISTRY: Dict[str, str] = {
    # Core AlignUSER / AlignUSER+
    "world_model_next_state": WORLD_MODEL_NEXT_STATE_PROMPT,
    "counterfactual_action_generation": COUNTERFACTUAL_ACTION_GENERATION_PROMPT,
    "counterfactual_reflection": COUNTERFACTUAL_REFLECTION_PROMPT,
    "item_level_counterfactual_reflection": ITEM_LEVEL_COUNTERFACTUAL_REFLECTION_PROMPT,
    "item_screening": ITEM_SCREENING_PROMPT,
    "action_selection": ACTION_SELECTION_PROMPT,
    "causal_validation": CAUSAL_VALIDATION_PROMPT,
    "post_interview_satisfaction": POST_INTERVIEW_SATISFACTION_PROMPT,
    "believability_recommended_list": BELIEVABILITY_RECOMMENDED_LIST_PROMPT,
    "llm_evaluator": LLM_EVALUATOR_PROMPT,

    # Page formats (appendix "Simulation Environment")
    "page_format_recommendation": PAGE_FORMAT_RECOMMENDATION,
    "page_item_format_recommendation": PAGE_ITEM_FORMAT_RECOMMENDATION,
    "page_format_opera": PAGE_FORMAT_OPERA,
    "page_product_format_opera": PAGE_PRODUCT_FORMAT_OPERA,

    # Memory entry formats (appendix "Preferences")
    "memory_entry_liked": MEMORY_ENTRY_LIKED,
    "memory_entry_disliked": MEMORY_ENTRY_DISLIKED,
    "memory_entry_neutral": MEMORY_ENTRY_NEUTRAL,

    # Persona + retrieval (appendix / AlignUSER+)
    "persona_prompt": PERSONA_PROMPT,
    "persona_generation": PERSONA_GENERATION_PROMPT,
    "persona_matching": PERSONA_MATCHING_PROMPT,
    "kg_query_generation": KG_QUERY_GENERATION_PROMPT,
}
