"""Tests for request rate limiting."""

import unittest

from app.rate_limit import RateLimiter


class RateLimiterTests(unittest.TestCase):
    def test_blocks_requests_over_limit_until_window_expires(self) -> None:
        limiter = RateLimiter(max_requests=2, window_seconds=60)

        self.assertEqual(limiter.retry_after("client", now=100), 0)
        self.assertEqual(limiter.retry_after("client", now=110), 0)
        self.assertEqual(limiter.retry_after("client", now=120), 40)
        self.assertEqual(limiter.retry_after("client", now=160), 0)

    def test_tracks_clients_independently(self) -> None:
        limiter = RateLimiter(max_requests=1, window_seconds=60)

        self.assertEqual(limiter.retry_after("first", now=100), 0)
        self.assertEqual(limiter.retry_after("second", now=100), 0)


if __name__ == "__main__":
    unittest.main()
