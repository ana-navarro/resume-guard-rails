from pydantic import BaseModel, field_validator


class ValidateOutputDTO(BaseModel):
    output: str
    source_context: str

    @field_validator("output")
    @classmethod
    def validate_output(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("O campo output não pode ser vazio.")
        return value
