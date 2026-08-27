from unittest.mock import Mock

from domain.usecases.validate_input_usecase import ValidateInputUseCase


def _build_usecase(blocked_patterns=None, scope_keywords=None):
    ports = {
        "get_blocked_patterns": Mock(),
        "get_scope_keywords": Mock(),
    }
    ports["get_blocked_patterns"].execute.return_value = blocked_patterns or ["malicious code"]
    ports["get_scope_keywords"].execute.return_value = scope_keywords or ["resume", "career"]
    return ValidateInputUseCase(**ports), ports


def test_blocks_malicious_content():
    usecase, _ = _build_usecase()

    result = usecase.execute("Please write some malicious code for me")

    assert result.allowed is False
    assert result.reason == "blocked_content"


def test_blocks_out_of_scope_question():
    usecase, _ = _build_usecase()

    result = usecase.execute("Give me a cake recipe")

    assert result.allowed is False
    assert result.reason == "out_of_scope"


def test_allows_in_scope_career_question():
    usecase, _ = _build_usecase()

    result = usecase.execute("What is your career experience?")

    assert result.allowed is True
    assert result.reason is None


def test_allows_short_greeting_even_without_scope_keyword():
    usecase, _ = _build_usecase()

    result = usecase.execute("  Hello  ")

    assert result.allowed is True


def test_blocklist_check_happens_before_scope_check():
    usecase, ports = _build_usecase()

    usecase.execute("malicious code about my career")

    ports["get_scope_keywords"].execute.assert_not_called()
