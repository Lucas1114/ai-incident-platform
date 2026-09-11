"""Tests for HTTP request safeguards."""

import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app
from app.models import InvestigationResult, Severity
from app.rate_limit import RateLimiter


class InvestigationEndpointTests(unittest.TestCase):
    @patch("app.main.investigation_rate_limiter", RateLimiter(5, 3600))
    @patch("app.main.investigate_incident")
    def test_rate_limits_sixth_request(self, investigate_incident) -> None:
        investigate_incident.return_value = InvestigationResult(
            summary="Checkout is degraded.",
            severity=Severity.high,
            leading_hypothesis="The payment provider may be degraded.",
            evidence=["Payment-provider calls timed out."],
            recommended_next_action="Check payment-provider health.",
        )
        client = TestClient(app)

        for _ in range(5):
            response = client.post(
                "/investigate",
                headers={"x-forwarded-for": "203.0.113.10"},
                json={"incident": "Checkout requests are timing out."},
            )
            self.assertEqual(response.status_code, 200)

        response = client.post(
            "/investigate",
            headers={"x-forwarded-for": "203.0.113.10"},
            json={"incident": "Checkout requests are timing out."},
        )

        self.assertEqual(response.status_code, 429)
        self.assertEqual(response.headers["retry-after"], "3600")
        self.assertEqual(investigate_incident.call_count, 5)


if __name__ == "__main__":
    unittest.main()
