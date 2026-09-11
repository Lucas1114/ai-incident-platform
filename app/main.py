"""Application entry point."""

from fastapi import FastAPI, HTTPException, Request

from app.llm_service import investigate_incident
from app.models import InvestigationRequest, InvestigationResult
from app.rate_limit import RateLimiter

app = FastAPI()
investigation_rate_limiter = RateLimiter(max_requests=5, window_seconds=3600)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/investigate", response_model=InvestigationResult)
def investigate(request: InvestigationRequest, http_request: Request):
    forwarded_for = http_request.headers.get("x-forwarded-for")
    client = forwarded_for.split(",", 1)[0].strip() if forwarded_for else None
    if not client and http_request.client:
        client = http_request.client.host

    retry_after = investigation_rate_limiter.retry_after(client or "unknown")
    if retry_after:
        raise HTTPException(
            status_code=429,
            detail="Investigation request limit exceeded",
            headers={"Retry-After": str(retry_after)},
        )

    try:
        return investigate_incident(request.incident)
    except Exception:
        raise HTTPException(
            status_code=502,
            detail="LLM service temporarily unavailable",
        ) from None
