from fastapi import APIRouter

from applications.controllers.validate_input_controller import (
    ValidateInputController,
)
from applications.controllers.validate_output_controller import (
    ValidateOutputController,
)
from applications.dto.validate_input_dto import ValidateInputDTO
from applications.dto.validate_output_dto import ValidateOutputDTO
from domain.usecases.validate_input_usecase import ValidateInputUseCase
from domain.usecases.validate_output_usecase import ValidateOutputUseCase
from infra.adapters.get_blocked_patterns_adapter import GetBlockedPatternsAdapter
from infra.adapters.get_scope_keywords_adapter import GetScopeKeywordsAdapter

router = APIRouter()

_validate_input_usecase = ValidateInputUseCase(
    get_blocked_patterns=GetBlockedPatternsAdapter(),
    get_scope_keywords=GetScopeKeywordsAdapter(),
)
_validate_input_controller = ValidateInputController(_validate_input_usecase)

_validate_output_usecase = ValidateOutputUseCase()
_validate_output_controller = ValidateOutputController(_validate_output_usecase)


@router.post("/validate-input")
def validate_input(payload: ValidateInputDTO):
    return _validate_input_controller.handle(payload)


@router.post("/validate-output")
def validate_output(payload: ValidateOutputDTO):
    return _validate_output_controller.handle(payload)
