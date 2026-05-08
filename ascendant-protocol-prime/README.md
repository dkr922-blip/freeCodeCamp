# Ascendant Protocol Prime

Build → Launch → Measure → Score → Kill or Scale → Repeat.

Ascendant Protocol Prime is a modular, FastAPI-based orchestration system for evaluating product signals, simulating profitability, and deciding whether to execute, scale, or terminate initiatives.

## Core lifecycle

1. **Discover** opportunities from incoming signals.
2. **Simulate** expected outcomes and risk.
3. **Build** plans and product candidates.
4. **Launch** with monetization hooks.
5. **Measure** performance and ROI.
6. **Optimize** using feedback loops.
7. **Scale or Kill** based on policy thresholds.

## API example

### POST `/v1/signal`

```json
{
  "idea": "AI content clipping SaaS",
  "audience": "creators",
  "price_range": [19, 99]
}
```

```json
{
  "score": 0.82,
  "expected_mrr": 14700,
  "risk": 0.18,
  "verdict": "EXECUTE",
  "recommended_model": "subscription"
}
```
