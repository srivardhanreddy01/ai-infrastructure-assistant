from pydantic import BaseModel, Field


class LLMRequest(BaseModel):
    instructions: str = Field(min_length=1)
    input: str = Field(min_length=1)