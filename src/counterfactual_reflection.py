"""
Counterfactual reflection prompt (trajectory datasets, e.g., OPeRA).
"""

from __future__ import annotations


COUNTERFACTUAL_REFLECTION_PROMPT = """You are analyzing user behavior on a {platform} recommender system.

You are given two possible actions from the same state:
1. The EXPERT action: what the human user actually did.
2. An ALTERNATIVE action: a different choice the user could have made.

Your job is to explain why the expert action is preferable *for this persona*, using the consequences
(the resulting next states) as evidence, and then extract one reusable lesson.

[CURRENT STATE]
{state_t}

[CURRENT PERSONA]
{persona}

[RECENT HISTORY]
{history_t}

[EXPERT TRANSITION]
Action: {expert_action}
Next state: {expert_next_state}

[ALTERNATIVE TRANSITION]
Action: {counterfactual_action}
Next state: {counterfactual_next_state}

Task:
1) Explain why the expert/human choice is better in the current context (reference concrete differences in the two next states).
2) Explain why the expert/human choice is more aligned with the persona and preferences.
3) Explain how the expert/human action improves future outcomes compared to the alternative.
4) Write ONE short, general lesson that would help choose better actions in similar situations.

Output format (4 lines, no extra text):
CONTEXT-ADVANTAGE: <why expert action is better in current context>
PERSONA-ALIGNMENT: <why expert action aligns better with persona/preferences>
FUTURE-OUTCOMES: <how expert action improves future outcomes vs alternative>
LESSON: <one reusable sentence>
"""
