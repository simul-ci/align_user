"""
Light parsers used by the pipeline.
"""

from __future__ import annotations

import re
from typing import Any, Dict


def parse_best_action(text: str) -> str:
    """
    Extract the action token after 'BEST-ACTION:'.
    """
    m = re.search(r"BEST-ACTION:\s*(.+)", text)
    if not m:
        raise ValueError("Could not find 'BEST-ACTION:' in model output.")
    return m.group(1).strip()


def parse_final_action(text: str) -> str:
    """
    Extract the action token after 'FINAL-ACTION:'.
    """
    m = re.search(r"FINAL-ACTION:\s*(.+)", text)
    if not m:
        raise ValueError("Could not find 'FINAL-ACTION:' in model output.")
    return m.group(1).strip()


def parse_post_interview_satisfaction(text: str) -> Dict[str, Any]:
    """
    Parse:
      RATING: <int 1-10>
      REASON: <text>
    """
    rating_match = re.search(r"RATING:\s*([0-9]+)", text)
    reason_match = re.search(r"REASON:\s*(.*)", text, flags=re.S)

    if not rating_match:
        raise ValueError("Could not parse RATING from post-interview output.")
    rating = int(rating_match.group(1))

    reason = ""
    if reason_match:
        reason = reason_match.group(1).strip()

    return {"rating": rating, "reason": reason}
