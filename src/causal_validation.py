"""
AlignUSER+ causal validation prompt (optionally uses retrieved KG memory evidence).
"""

from __future__ import annotations


CAUSAL_VALIDATION_PROMPT = """You are simulating a user interacting with a {platform} recommender system.

You have tentatively chosen an action. Before committing, do a quick consistency check:
- Ask yourself 2-4 verification questions about whether this action makes sense for your persona.
- Answer them using ONLY the information in the current state, persona, and recent history.
- Do not invent evidence.
- Decide whether to keep the tentative action or switch to a better action from VALID ACTIONS.

[CURRENT STATE]
{state_t}

[CURRENT PERSONA]
{persona}

[RECENT HISTORY]
{history_t}

[TENTATIVE ACTION]
{tentative_action}

[VALID ACTIONS]
{available_actions}

Output format (exactly 4 blocks, no extra text):
QUESTIONS:
1) ...
2) ...
ANSWERS:
1) ...
2) ...
DECISION: <KEEP or CHANGE> — <one short sentence>
FINAL-ACTION: <one action token from VALID ACTIONS>
"""
