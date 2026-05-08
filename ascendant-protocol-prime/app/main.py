from __future__ import annotations

from fastapi import FastAPI, Request

from app.api.routes_opportunities import router as opportunity_router

app = FastAPI(title="Ascendant Protocol Prime", version="0.1.0")
app.include_router(opportunity_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/webhook/stripe")
async def stripe_webhook(_request: Request) -> dict[str, str]:
    # Placeholder webhook hook for integration wiring.
    return {"status": "ok"}
