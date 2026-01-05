# AlignUSER

<div id="top" align="center">
<p align="center">
<img src="illustration.jpg" width="1000px" >
</p>
</div>


AlignUSER is an LLM-based user simulation framework for evaluating recommender systems by simulating realistic, policy-sensitive user interactions (browse/click/choose/rate) grounded in user context (persona + history + memory) and stabilized by alignment constraints.

It is designed to support rapid **offline what-if testing**, **segment-level analysis**, and **bias/stability evaluation** without expensive online A/B tests.

---

## Key ideas
- **World-model-based user simulation**: AlignUSER learns a predictive model of user behavior dynamics—how a user’s state evolves across recommendation pages and actions—enabling multi-step rollouts rather than isolated, one-shot decisions.
- **Aligned user policy learning**: the user policy is trained to remain faithful to real human behavior by explicitly aligning actions with persona, historical preferences, and observed decision patterns, addressing over-optimism and generic LLM behaviors.
- **Counterfactual reflection from human trajectories**: learning is driven by contrasting real user actions with plausible but suboptimal alternatives, allowing the agent to internalize *why* humans act differently under the same recommendation exposure.
- **Policy-sensitive evaluation**: because AlignUSER models user dynamics and decision logic, simulated behavior changes meaningfully across recommendation strategies, making it suitable for comparative offline evaluation and what-if analysis.
- **Bridging offline metrics and real outcomes**: AlignUSER-generated interactions can be used to estimate traditional ranking metrics and business-facing behavioral metrics, narrowing the gap between offline evaluation and real-world system performance.


---


---

## Code Structure

```
src/           
├── persona.py         # Persona template + builder
├── page_formats.py    # Page/state formats (Recommendation & OPeRA domains)
├── memory_formats.py  # Memory entry templates (liked/disliked/neutral)
├── world_model.py     # Next-state prediction prompt
├── counterfactual_action_generation.py   # Generate K alternative actions
├── counterfactual_reflection.py          # Trajectory-level reflection
├── item_level_counterfactual_reflection.py  # Item-level (rating) reflection
├── item_screening.py  # [WATCH]/[SKIP] screening + builder
├── action_selection.py # Action selection + builder
├── causal_validation.py   # AlignUSER+ self-check prompt
├── post_interview_satisfaction.py  # Session satisfaction scoring
├── believability.py   # Recommended list believability
├── llm_evaluator.py   # Human vs AI detection
├── persona_generation.py  # Infer persona from likes/dislikes
├── persona_matching.py    # Score candidate persona fit
├── kg_query_generation.py # KG memory retrieval queries (AlignUSER+)
├── parsers.py         # Output parsers (BEST-ACTION, FINAL-ACTION, RATING)
└── registry.py        # PROMPT_REGISTRY
```

## Features
- ✅ Multi-step interaction rollouts (e.g., landing → browse pages → inspect items → add-to-cart / skip → rate)
- ✅ Persona- and history-conditioned decisions with optional rationales
- ✅ Memory module (episodic + optional KG/graph memory) for long-horizon consistency
- ✅ Policy evaluation + segment reports (user groups, cohorts)

---

## Abstract
Evaluating recommender systems remains challenging due to the gap between offline metrics and real user behavior, as well as the scarcity of interaction data. Recent work explores large language model (LLM) agents as synthetic users, yet these agents typically rely on few-shot prompting, which yields a shallow understanding of the environment and limits their ability to faithfully reproduce human behavior. We introduce AlignUSER, a framework that learns world-model-driven agents from human interactions. Given rollout sequences of actions and states, we formalize world modeling as a next state prediction task that helps the agent internalize the environment. To align actions with human personas, we generate counterfactual trajectories around demonstrations and prompt the LLM to compare its decisions with human choices, identify suboptimal actions, and extract lessons. The learned policy is then used to drive the agent’s interactions with the recommender system. We evaluate \textsc{AlignUSER} across multiple datasets and demonstrate closer alignment with genuine humans than prior work, both at micro and macro levels. 





