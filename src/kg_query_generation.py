"""
Retrieval prompt (AlignUSER+ KG-memory): query generation.
"""

from __future__ import annotations


KG_QUERY_GENERATION_PROMPT = """You are simulating a user interacting with a {platform} recommender system.

To make a good decision, you want to recall relevant information from your memory about past interactions, preferences, and similar items.

Given the current state, persona, and recent history, propose up to 3 short retrieval queries that would help you decide what to do next.

Rules:
- Queries should be short (5-12 words), concrete, and directly useful.
- Focus on your preferences/constraints, item attributes on the current page, and past patterns.
- Do NOT answer the queries; only output the queries.

[CURRENT STATE]
{state_t}

[CURRENT PERSONA]
{persona}

[RECENT HISTORY]
{history_t}

Output format (JSON only):
{{"queries": ["...", "...", "..."]}}
"""
