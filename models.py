from enum import Enum

from pydantic import BaseModel, Field


class LLMRequest(BaseModel):
    instructions: str = Field(min_length=1)
    input: str = Field(min_length=1)


class Severity(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class LogAnalysis(BaseModel):
    root_cause: str = Field(min_length=1)
    severity: Severity
    confidence: float = Field(ge=0.0, le=1.0)
    error_count: int = Field(ge=0)
    recommendation: str = Field(min_length=1)
    summary: str = Field(min_length=1)
    