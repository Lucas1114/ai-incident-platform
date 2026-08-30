"""Application entry point."""

from fastapi import FastAPI, HTTPException

from app.llm_service import investigate_incident
from app.models import InvestigationRequest, InvestigationResult

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/investigate", response_model=InvestigationResult)
def investigate(request: InvestigationRequest):
    try:
        return investigate_incident(request.incident)
    except Exception:
        raise HTTPException(
            status_code=502,
            detail="LLM service temporarily unavailable",
        ) from None
