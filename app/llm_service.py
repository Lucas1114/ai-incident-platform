"""LLM service for incident investigation."""

import os

from openai import OpenAI

from app.models import InvestigationResult


def investigate_incident(incident: str) -> InvestigationResult:
    client = OpenAI(
        api_key=os.environ["OPENAI_API_KEY"],
        timeout=20.0,
    )
    response = client.responses.parse(
        model="gpt-5.6-luna",
        instructions=(
            "You are an incident investigation assistant. Analyze the incident "
            "and produce the requested investigation result. Treat the "
            "leading_hypothesis as a hypothesis, not a confirmed root cause. "
            "Limit evidence to facts and signals explicitly stated in the "
            "incident. Return exactly one concrete diagnostic action in "
            "recommended_next_action; do not combine multiple checks or add a "
            "remediation step."
        ),
        input=incident,
        max_output_tokens=800,
        text_format=InvestigationResult,
    )
    return response.output_parsed
