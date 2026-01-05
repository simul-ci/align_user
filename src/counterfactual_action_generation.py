"""
Counterfactual action generation prompt (K alternatives).
"""

from __future__ import annotations


COUNTERFACTUAL_ACTION_GENERATION_PROMPT = """You are analyzing a user simulation scenario on a {platform} recommender system.

Your goal: propose {k} *valid* alternative actions that a user could have taken at the current state,
which are different from the action they actually chose (the expert action).

Constraints:
- Each alternative must be one of the provided VALID ACTIONS (exact string match).
- Do NOT repeat the expert action.
- Make alternatives plausible for the given persona and recent history.
- Prefer *meaningful* alternatives (actions that could realistically change the next outcome),
  not trivial no-ops.

Context:
[CURRENT STATE]
{state_t}

[CURRENT PERSONA]
{persona}

[RECENT HISTORY]
{history_t}

[EXPERT / HUMAN ACTION]
{expert_action}

[VALID ACTIONS]
{available_actions}

Output format:
- Return EXACTLY {k} lines.
- Each line must contain ONLY an action token (no numbering, no extra text).

[ALTERNATIVE ACTIONS]
"""
