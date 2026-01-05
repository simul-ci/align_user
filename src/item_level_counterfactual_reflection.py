"""
Counterfactual reflection prompt (non-trajectory datasets; item-level ratings).
"""

from __future__ import annotations


ITEM_LEVEL_COUNTERFACTUAL_REFLECTION_PROMPT = """You are analyzing rating behavior on a {platform} recommender system.

You are given a persona and a single item. The human user provided a rating (the EXPERT rating).
An alternative rating is also provided. Each rating comes with an optional short reasoning and an observed reward/signal.

Your job is to:
- Explain why the expert rating is more faithful to the persona and the item content than the alternative rating.
- Extract ONE reusable lesson for rating decisions.

[PERSONA]
{persona}

[ITEM]
Title: {item_title}
Description: {item_description}

[EXPERT (HUMAN) RATING]
Rating (1..{rating_scale_max}): {expert_rating}
Reasoning: {expert_reasoning}
Reward/Signal: {expert_reward}

[ALTERNATIVE RATING]
Rating (1..{rating_scale_max}): {counterfactual_rating}
Reasoning: {counterfactual_reasoning}
Reward/Signal: {counterfactual_reward}

[HISTORY SUMMARY]
{history_summary}

Output format (2 lines, no extra text):
WHY: <1-3 sentences>
LESSON: <one sentence>
"""
