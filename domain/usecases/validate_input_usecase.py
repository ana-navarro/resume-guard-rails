from domain.models.input_validation_result import InputValidationResult
from domain.ports.validate_input_port import ValidateInputPort
from infra.ports.get_blocked_patterns_port import GetBlockedPatternsPort
from infra.ports.get_scope_keywords_port import GetScopeKeywordsPort

GREETINGS = {
    "oi",
    "ola",
    "olá",
    "hello",
    "hi",
    "hey",
    "obrigado",
    "obrigada",
    "thanks",
    "thank you",
    "tchau",
    "bye",
    "goodbye",
    "bom dia",
    "boa tarde",
    "boa noite",
    "good morning",
    "good afternoon",
    "good evening",
}


class ValidateInputUseCase(ValidateInputPort):
    def __init__(
        self,
        get_blocked_patterns: GetBlockedPatternsPort,
        get_scope_keywords: GetScopeKeywordsPort,
    ) -> None:
        self._get_blocked_patterns = get_blocked_patterns
        self._get_scope_keywords = get_scope_keywords

    def execute(self, message: str) -> InputValidationResult:
        normalized = message.strip().lower()

        for pattern in self._get_blocked_patterns.execute():
            if pattern.lower() in normalized:
                return InputValidationResult(allowed=False, reason="blocked_content")

        if normalized in GREETINGS:
            return InputValidationResult(allowed=True)

        for keyword in self._get_scope_keywords.execute():
            if keyword.lower() in normalized:
                return InputValidationResult(allowed=True)

        return InputValidationResult(allowed=False, reason="out_of_scope")
