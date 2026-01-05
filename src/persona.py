"""
Persona prompt template and builder function.
"""

from __future__ import annotations

from typing import Any, Dict


PERSONA_PROMPT = """You are simulating a human user with the following persona.

Occupation: {occupation}
Age Range: {age_range}

Big5 Personality Traits (1=low, 2=medium, 3=high):
- Openness: {openness}
- Conscientiousness: {conscientiousness}
- Extraversion: {extraversion}
- Agreeableness: {agreeableness}
- Neuroticism: {neuroticism}

Pickiness (1=low, 2=medium, 3=high): {pickiness}

Habits / shopping style:
{habits}

Interaction History:
{interaction_history}

Important: Follow this persona consistently throughout the session.
"""


def build_persona_prompt(persona: Dict[str, Any], interaction_history: str = "") -> str:
    """
    Build PERSONA_PROMPT from a persona attribute dict.

    Expected keys (AlignUSER paper):
      - occupation, age_range
      - openness, conscientiousness, extraversion, agreeableness, neuroticism  (each 1..3)
      - pickiness (1..3)
      - habits (free text)

    Args:
        persona: Dict with persona attributes.
        interaction_history: Optional string of past interactions from episodic memory.

    Any missing field is rendered as 'Unknown' (or empty habits).
    """
    def _get(key: str, default: str = "Unknown") -> str:
        v = persona.get(key, default)
        return str(v) if v is not None else default

    return PERSONA_PROMPT.format(
        occupation=_get("occupation"),
        age_range=_get("age_range"),
        openness=_get("openness"),
        conscientiousness=_get("conscientiousness"),
        extraversion=_get("extraversion"),
        agreeableness=_get("agreeableness"),
        neuroticism=_get("neuroticism"),
        pickiness=_get("pickiness"),
        habits=str(persona.get("habits", "")).strip() or "Unknown",
        interaction_history=interaction_history.strip() or "None yet.",
    )
