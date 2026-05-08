from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.intelligence.opportunity_engine import score_signal
from app.orchestration.kill_scale_engine import decide_verdict

router = APIRouter()


class SignalRequest(BaseModel):
    idea: str = Field(..., min_length=3)
    audience: str = Field(..., min_length=2)
    price_range: tuple[int, int]


@router.post("/v1/signal")
def evaluate_signal(payload: SignalRequest) -> dict[str, object]:
    result = score_signal(payload.idea, payload.audience, payload.price_range)
    result["verdict"] = decide_verdict(result["score"], result["risk"])
    return result
