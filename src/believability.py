"""
Believability on recommended list prompt (macro-level).
"""

from __future__ import annotations


BELIEVABILITY_RECOMMENDED_LIST_PROMPT = """You are evaluating whether a recommended list looks believable for a persona.

You will be given:
- A persona description
- A list of recommended {item_type}
- (Optionally) a short taste summary

Rate believability: how well the list matches the persona and looks like a real recommendation response.

[PERSONA]
{persona}

[TASTE SUMMARY (optional)]
{taste_summary}

[RECOMMENDED LIST]
{recommended_list}

Output format (exactly 2 lines, no extra text):
RATING: <integer 1-10>
REASON: <1-2 sentences>
"""
