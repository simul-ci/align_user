"""
Action selection prompt (after screening).
"""

from __future__ import annotations


ACTION_SELECTION_PROMPT = """You are simulating a user interacting with a recommender system (platform: {platform}).

[CURRENT STATE]
{state_t}

[CURRENT PERSONA]
{persona}

[RECENT HISTORY]
{history_t}

[RETRIEVED CONTEXT]
{retrieved_context}

[CLICK CANDIDATES FROM SCREENING]
{candidates}

[VALID ACTIONS]
{available_actions}

Instruction: Think step by step about what a careful user with this persona would do next, considering their goals, preferences, and the future consequences of each action.

Guidance:
- Use the persona + recent history to keep behavior consistent across the session.
- Use the retrieved context about similar items is provided, use it to inform your decision.
- If there are good candidates to click, prefer clicking one candidate item.
- If none of the items look appealing, consider navigating to the next page, searching, or exiting — but only if realistic.
- Avoid erratic behavior (e.g., clicking random items, exiting too early without reason).

End with a single line of the form:
BEST-ACTION: <action_token>
RATIONALE: <rationale>
"""


def build_action_selection_prompt(
    platform: str,
    state_t: str,
    persona: str,
    history_t: str,
    candidates: str,
    available_actions: str,
    retrieved_context: str = "",
) -> str:
    """
    Build ACTION_SELECTION_PROMPT with safe default for retrieved_context.

    For AlignUSER (no KG retrieval), pass retrieved_context="" or omit it.
    For AlignUSER+, pass the retrieved evidence string.
    """
    return ACTION_SELECTION_PROMPT.format(
        platform=platform,
        state_t=state_t,
        persona=persona,
        history_t=history_t,
        candidates=candidates,
        available_actions=available_actions,
        retrieved_context=retrieved_context.strip() or "(none)",
    )
