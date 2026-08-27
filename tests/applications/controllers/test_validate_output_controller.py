from unittest.mock import Mock

from applications.controllers.validate_output_controller import (
    ValidateOutputController,
)
from applications.dto.validate_output_dto import ValidateOutputDTO
from domain.models.output_validation_result import OutputValidationResult


def test_handle_returns_the_validation_result():
    validate_output = Mock()
    validate_output.execute.return_value = OutputValidationResult(
        is_grounded=False, flagged_claims=["Acme Corp"]
    )
    controller = ValidateOutputController(validate_output)

    result = controller.handle(
        ValidateOutputDTO(output="worked at Acme Corp", source_context="worked as engineer")
    )

    validate_output.execute.assert_called_once_with("worked at Acme Corp", "worked as engineer")
    assert result == {"is_grounded": False, "flagged_claims": ["Acme Corp"]}
