from unittest.mock import Mock

from applications.controllers.validate_input_controller import (
    ValidateInputController,
)
from applications.dto.validate_input_dto import ValidateInputDTO
from domain.models.input_validation_result import InputValidationResult


def test_handle_returns_the_validation_result():
    validate_input = Mock()
    validate_input.execute.return_value = InputValidationResult(allowed=False, reason="out_of_scope")
    controller = ValidateInputController(validate_input)

    result = controller.handle(ValidateInputDTO(message="cake recipe"))

    validate_input.execute.assert_called_once_with("cake recipe")
    assert result == {"allowed": False, "reason": "out_of_scope"}
