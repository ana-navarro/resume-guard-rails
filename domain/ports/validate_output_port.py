from abc import ABC, abstractmethod

from domain.models.output_validation_result import OutputValidationResult


class ValidateOutputPort(ABC):
    @abstractmethod
    def execute(self, output: str, source_context: str) -> OutputValidationResult:
        raise NotImplementedError
