import re

from domain.models.output_validation_result import OutputValidationResult
from domain.ports.validate_output_port import ValidateOutputPort

# Heuristic extraction of "specific claims" likely to be fabricated if not grounded: proper-noun-like
# capitalized word sequences (e.g. "Google", "Universidade de Sao Paulo") and numbers followed by a
# duration unit (e.g. "5 anos", "10 years"). Known limitation: this is a substring/regex heuristic,
# not real NLP -- no LLM/embeddings provider is configured anywhere in this project yet (see
# tasks/guard-rails-validators).
PROPER_NOUN_PATTERN = re.compile(r"\b(?:[A-ZÀ-Ý][a-zà-ÿ]+(?:\s+[A-ZÀ-Ý][a-zà-ÿ]+)*)\b")
NUMBER_WITH_UNIT_PATTERN = re.compile(r"\b\d+\s*(?:anos?|meses?|years?|months?)\b", re.IGNORECASE)
MIN_CLAIM_LENGTH = 3

# Common sentence-starter words that would otherwise be false-positived as "proper nouns" when they
# appear capitalized at the start of a sentence.
COMMON_LEADING_WORDS = {
    "the", "a", "an", "this", "that", "these", "those", "it", "i", "in", "on", "at", "as",
    "if", "but", "and", "or", "she", "he", "they", "we", "you", "my", "your", "his", "her",
    "o", "os", "um", "uma", "ele", "ela", "eles", "elas", "eu", "voce", "você",
    "este", "esta", "isso", "aquele", "aquela",
}


class ValidateOutputUseCase(ValidateOutputPort):
    def execute(self, output: str, source_context: str) -> OutputValidationResult:
        candidates = set(PROPER_NOUN_PATTERN.findall(output))
        candidates.update(match.group() for match in NUMBER_WITH_UNIT_PATTERN.finditer(output))

        normalized_context = source_context.lower()
        flagged = sorted(
            claim
            for claim in candidates
            if len(claim) >= MIN_CLAIM_LENGTH
            and (" " in claim or claim.lower() not in COMMON_LEADING_WORDS)
            and claim.lower() not in normalized_context
        )

        return OutputValidationResult(is_grounded=not flagged, flagged_claims=flagged)
