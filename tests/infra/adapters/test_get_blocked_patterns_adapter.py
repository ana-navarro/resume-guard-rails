from infra.adapters.get_blocked_patterns_adapter import (
    BLOCKED_PATTERNS,
    GetBlockedPatternsAdapter,
)


def test_execute_returns_the_hardcoded_blocked_patterns():
    assert GetBlockedPatternsAdapter().execute() == BLOCKED_PATTERNS


def test_blocked_patterns_cover_malicious_code_requests():
    assert any("malicious code" in pattern for pattern in BLOCKED_PATTERNS)
