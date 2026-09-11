"""Tests for application data models."""

import unittest

from pydantic import ValidationError

from app.models import InvestigationRequest, InvestigationResult, Severity


class InvestigationResultTests(unittest.TestCase):
    def test_rejects_incident_over_4000_characters(self) -> None:
        with self.assertRaises(ValidationError):
            InvestigationRequest(incident="x" * 4001)

    def test_uses_investigation_schema(self) -> None:
        result = InvestigationResult(
            summary="Requests are timing out.",
            severity=Severity.high,
            leading_hypothesis="The upstream service may be overloaded.",
            evidence=["Request latency exceeded 30 seconds."],
            recommended_next_action="Inspect upstream service saturation metrics.",
        )

        self.assertEqual(
            set(result.model_dump()),
            {
                "summary",
                "severity",
                "leading_hypothesis",
                "evidence",
                "recommended_next_action",
            },
        )

    def test_rejects_old_investigation_schema(self) -> None:
        with self.assertRaises(ValidationError):
            InvestigationResult(
                summary="Requests are timing out.",
                severity=Severity.high,
                possible_causes=["The upstream service is overloaded."],
                recommended_next_step="Inspect upstream metrics.",
            )


if __name__ == "__main__":
    unittest.main()
