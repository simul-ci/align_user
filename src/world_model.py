"""
World model (next-state prediction) prompt.
"""

from __future__ import annotations


WORLD_MODEL_NEXT_STATE_PROMPT = """You are simulating environment dynamics for a recommender-system simulator (platform: {platform}).

Given the current textual state and an action token, predict the *next* textual state that would result from taking that action.

Rules:
- Be faithful to the simulator: only change what the action would change.
- Do not invent new UI elements or items not implied by the state/action.
- Output ONLY the next state text (no preamble, no labels, no explanations).

[CURRENT STATE]
{state_t}

[ACTION]
{action_t}

[NEXT STATE]
"""
