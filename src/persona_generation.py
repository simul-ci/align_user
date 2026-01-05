"""
Persona generation prompt.
"""

from __future__ import annotations


PERSONA_GENERATION_PROMPT = """You are an AI assistant specializing in analyzing human preferences and understanding personas.
You will analyze {item_type}s liked and disliked by an individual.

Task:
I will provide a list of {item_type}s that the individual liked and disliked.
Based on this information, predict the most suitable persona for this individual.

The persona includes:
- Occupation
- Age range
- Big5 personality traits (each scored from 1 to 3, where 1 is low, 2 is medium, and 3 is high)

Liked {item_type}s:
{liked_items}

Disliked {item_type}s:
{disliked_items}

Based on the preferences above, predict the most suitable persona for this individual.
Ensure the predicted persona is coherent with the liked and disliked {item_type}s, accurately reflecting the individual's tastes.

Response Format:
Occupation: [choose from <occupation list>: {occupation_list}]
Age Range: [choose from <age list>: {age_list}]
Big5 Personality Traits:
- Openness: [1-3]
- Conscientiousness: [1-3]
- Extraversion: [1-3]
- Agreeableness: [1-3]
- Neuroticism: [1-3]
"""
