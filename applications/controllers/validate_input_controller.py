from applications.dto.validate_input_dto import ValidateInputDTO
from domain.ports.validate_input_port import ValidateInputPort


class ValidateInputController:
    def __init__(self, validate_input: ValidateInputPort) -> None:
        self._validate_input = validate_input

    def handle(self, dto: ValidateInputDTO) -> dict:
        result = self._validate_input.execute(dto.message)
        return {"allowed": result.allowed, "reason": result.reason}
