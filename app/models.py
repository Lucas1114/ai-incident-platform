"""Application data models."""

from enum import Enum

from pydantic import BaseModel, Field


class Severity(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class InvestigationRequest(BaseModel):
    incident: str = Field(min_length=1, max_length=4000)


class InvestigationResult(BaseModel):
    summary: str
    severity: Severity
    leading_hypothesis: str
    evidence: list[str]
    recommended_next_action: str
