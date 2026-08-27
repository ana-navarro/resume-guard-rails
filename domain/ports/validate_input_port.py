from abc import ABC, abstractmethod

from domain.models.input_validation_result import InputValidationResult


class ValidateInputPort(ABC):
    @abstractmethod
    def execute(self, message: str) -> InputValidationResult:
        raise NotImplementedError
