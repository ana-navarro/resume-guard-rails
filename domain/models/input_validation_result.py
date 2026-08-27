from dataclasses import dataclass


@dataclass(frozen=True)
class InputValidationResult:
    allowed: bool
    reason: str | None = None
