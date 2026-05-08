from __future__ import annotations

from typing import Any


def score_signal(idea: str, audience: str, price_range: tuple[int, int]) -> dict[str, Any]:
    """Score an incoming product signal.

    Heuristics are intentionally simple for a bootstrapped MVP:
    - Higher top-end price increases expected MRR.
    - Broader audience keywords lower concentration risk.
    - Longer, specific idea descriptions increase confidence.
    """

    floor, ceiling = price_range
    idea_tokens = max(len(idea.split()), 1)

    audience_factor = 1.0
    if any(word in audience.lower() for word in ["creator", "developer", "b2b", "agency"]):
        audience_factor += 0.08

    specificity_bonus = min(idea_tokens / 20, 0.1)
    risk = max(0.05, round(0.24 - specificity_bonus - (audience_factor - 1.0), 2))

    expected_mrr = int(((floor + ceiling) / 2) * 200 * audience_factor)
    raw_score = (expected_mrr / 20000) * (1 - risk)
    score = round(max(0.0, min(0.99, raw_score)), 2)

    model = "subscription" if ceiling >= 49 else "one-time"

    return {
        "score": score,
        "expected_mrr": expected_mrr,
        "risk": risk,
        "recommended_model": model,
    }
