"""
Post-interview satisfaction prompt (session-level scalar).
"""

from __future__ import annotations


POST_INTERVIEW_SATISFACTION_PROMPT = """You are scoring the overall satisfaction of a simulated user session.

You will be given the user's persona and a concise session summary/transcript. Rate the user's satisfaction with the session outcome.

Guidance:
- Consider whether the session achieved the user's implicit goal, how coherent the behavior was,
  and whether the browsing/purchasing pattern looks realistic for the persona.
- Use the full 1-10 scale.

[PERSONA]
{persona}

[SESSION SUMMARY]
{session_summary}

Output format (exactly 2 lines, no extra text):
RATING: <integer 1-10>
REASON: <1-2 sentences>
"""


def build_post_interview_satisfaction_prompt(
    session_summary: str,
    persona: str = "",
) -> str:
    """
    Build POST_INTERVIEW_SATISFACTION_PROMPT with safe default for persona.

    If persona is not available, pass persona="" and it will display "(not provided)".
    """
    return POST_INTERVIEW_SATISFACTION_PROMPT.format(
        session_summary=session_summary,
        persona=persona.strip() or "(not provided)",
    )
