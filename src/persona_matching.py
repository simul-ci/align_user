"""
Persona matching prompt.
"""

from __future__ import annotations


PERSONA_MATCHING_PROMPT = """Pretend to be a {candidate_persona}.

Here is a list of {item_type} you like and dislike:

Liked Items:
{liked_items}

Disliked Items:
{disliked_items}

Here is a summary of your tastes:
{taste}

On a scale of 1 to 10 (1 = least likely, 10 = most likely), rate how likely you are to like and dislike similar {item_type}
in the future, based on your own taste. Explain the reason for your rating.

Response Format:
Rating: <integer 1-10>
Reason: <1-3 sentences>
"""
