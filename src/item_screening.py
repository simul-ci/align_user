"""
Page-level screening ([WATCH]/[SKIP]) before acting.
"""

from __future__ import annotations


ITEM_SCREENING_PROMPT = """You are simulating a user interacting with a recommender system (platform: {platform}).

Your job is to look at the items currently visible in the state and do a quick internal screening:
- For each item on the current page, decide [WATCH] (interested, would consider clicking) or [SKIP] (not interested) based on the persona and history.
- Then shortlist up to {max_candidates} candidate items that you would be willing to click for more details.

Important:
- Use ONLY the items that appear in the CURRENT STATE.
- Use the item identifiers exactly as written in the state (e.g., ITEM_3, id=..., etc.).
- Be consistent with the persona and recent history.
- If retrieved context about similar items is provided, use it to inform your decisions.

[CURRENT STATE]
{state_t}

[CURRENT PERSONA]
{persona}

[RECENT HISTORY]
{history_t}

[RETRIEVED CONTEXT]
{retrieved_context}

Output format:
ITEM-DECISIONS:
- <item_id>: [WATCH] <short reason>
- <item_id>: [SKIP] <short reason>
CANDIDATES: <comma-separated item_ids (max {max_candidates}) OR NONE>
"""


def build_item_screening_prompt(
    platform: str,
    state_t: str,
    persona: str,
    history_t: str,
    max_candidates: int,
    retrieved_context: str = "",
) -> str:
    """
    Build ITEM_SCREENING_PROMPT with safe default for retrieved_context.

    For AlignUSER (no KG retrieval), pass retrieved_context="" or omit it.
    For AlignUSER+, pass the retrieved evidence string.
    """
    return ITEM_SCREENING_PROMPT.format(
        platform=platform,
        state_t=state_t,
        persona=persona,
        history_t=history_t,
        max_candidates=max_candidates,
        retrieved_context=retrieved_context.strip() or "(none)",
    )
