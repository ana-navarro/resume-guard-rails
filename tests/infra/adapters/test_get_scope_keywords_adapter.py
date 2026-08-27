from infra.adapters.get_scope_keywords_adapter import (
    SCOPE_KEYWORDS,
    GetScopeKeywordsAdapter,
)


def test_execute_returns_the_hardcoded_scope_keywords():
    assert GetScopeKeywordsAdapter().execute() == SCOPE_KEYWORDS


def test_scope_keywords_cover_resume_and_career_terms():
    assert "resume" in SCOPE_KEYWORDS
    assert "carreira" in SCOPE_KEYWORDS
