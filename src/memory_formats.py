"""
Memory entry format templates.
"""

from __future__ import annotations


MEMORY_ENTRY_LIKED = "I liked {item_name} based on my review score of {score}."
MEMORY_ENTRY_DISLIKED = "I disliked {item_name} based on my review score of {score}."
MEMORY_ENTRY_NEUTRAL = "I felt neutral about {item_name} based on my review score of {score}."


def build_memory_entry(item_name: str, score: int, liked_threshold: int = 4, disliked_threshold: int = 2) -> str:
    """
    Build a memory entry string based on the score.

    Per paper: scores >= liked_threshold -> liked, <= disliked_threshold -> disliked, else neutral.
    """
    if score >= liked_threshold:
        return MEMORY_ENTRY_LIKED.format(item_name=item_name, score=score)
    elif score <= disliked_threshold:
        return MEMORY_ENTRY_DISLIKED.format(item_name=item_name, score=score)
    else:
        return MEMORY_ENTRY_NEUTRAL.format(item_name=item_name, score=score)
