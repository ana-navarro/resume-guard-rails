import pytest
from pydantic import ValidationError

from applications.dto.validate_input_dto import ValidateInputDTO


def test_valid_message_passes_validation():
    dto = ValidateInputDTO(message="What is your experience?")
    assert dto.message == "What is your experience?"


def test_rejects_empty_message():
    with pytest.raises(ValidationError):
        ValidateInputDTO(message="   ")
