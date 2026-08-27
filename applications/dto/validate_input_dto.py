from pydantic import BaseModel, field_validator


class ValidateInputDTO(BaseModel):
    message: str

    @field_validator("message")
    @classmethod
    def validate_message(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("O campo message não pode ser vazio.")
        return value
