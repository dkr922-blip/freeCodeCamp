from __future__ import annotations


def decide_verdict(score: float, risk: float) -> str:
    if score >= 0.75 and risk <= 0.25:
        return "EXECUTE"
    if score >= 0.45:
        return "ITERATE"
    return "KILL"
