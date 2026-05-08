from app.intelligence.opportunity_engine import score_signal
from app.orchestration.kill_scale_engine import decide_verdict


def test_score_signal_bounds() -> None:
    result = score_signal("AI content clipping SaaS", "creators", (19, 99))
    assert 0 <= result["score"] <= 0.99
    assert result["expected_mrr"] > 0
    assert result["recommended_model"] == "subscription"


def test_decide_verdict_execute() -> None:
    assert decide_verdict(0.82, 0.18) == "EXECUTE"
