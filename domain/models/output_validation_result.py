from dataclasses import dataclass, field


@dataclass(frozen=True)
class OutputValidationResult:
    is_grounded: bool
    flagged_claims: list[str] = field(default_factory=list)
