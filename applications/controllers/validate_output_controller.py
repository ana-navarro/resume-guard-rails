from applications.dto.validate_output_dto import ValidateOutputDTO
from domain.ports.validate_output_port import ValidateOutputPort


class ValidateOutputController:
    def __init__(self, validate_output: ValidateOutputPort) -> None:
        self._validate_output = validate_output

    def handle(self, dto: ValidateOutputDTO) -> dict:
        result = self._validate_output.execute(dto.output, dto.source_context)
        return {"is_grounded": result.is_grounded, "flagged_claims": result.flagged_claims}
