"""Application data models."""

from enum import Enum

from pydantic import BaseModel, Field


class Severity(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class InvestigationRequest(BaseModel):
    incident: str = Field(min_length=1)


class InvestigationResult(BaseModel):
    summary: str
    severity: Severity
    possible_causes: list[str]
    recommended_next_step: str
