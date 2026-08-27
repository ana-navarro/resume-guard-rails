import pytest
from pydantic import ValidationError

from applications.dto.validate_output_dto import ValidateOutputDTO


def test_valid_output_passes_validation():
    dto = ValidateOutputDTO(output="some answer", source_context="some context")
    assert dto.output == "some answer"


def test_rejects_empty_output():
    with pytest.raises(ValidationError):
        ValidateOutputDTO(output="   ", source_context="some context")
