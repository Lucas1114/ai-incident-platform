"""Small in-memory rate limiter for the single-instance public demo."""

from collections import defaultdict, deque
from math import ceil
from threading import Lock
from time import monotonic


class RateLimiter:
    """Limit requests per client over a sliding time window."""

    def __init__(self, max_requests: int, window_seconds: int) -> None:
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._requests: dict[str, deque[float]] = defaultdict(deque)
        self._lock = Lock()

    def retry_after(self, client: str, now: float | None = None) -> int:
        """Record an allowed request, or return seconds until the next one."""
        current_time = monotonic() if now is None else now
        cutoff = current_time - self.window_seconds

        with self._lock:
            requests = self._requests[client]
            while requests and requests[0] <= cutoff:
                requests.popleft()

            if len(requests) >= self.max_requests:
                return max(1, ceil(requests[0] + self.window_seconds - current_time))

            requests.append(current_time)
            return 0
