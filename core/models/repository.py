from pydantic import BaseModel, Field, field_validator
import re

class IngestRequest(BaseModel):
    repository_url: str = Field(
        ...,
        min_length=19,
        max_length=200,
        description="GitHub repository URL"
    )
    github_token: str | None = Field(
        None,
        min_length=4,
        max_length=200,
        description="GitHub personal access token for private repositories"
    )

    @field_validator('repository_url')
    @classmethod
    def validate_github_url(cls, v: str) -> str:
        github_pattern = r'^https://github\.com/[a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+/?$'
        if not re.match(github_pattern, v):
            raise ValueError('Must be a valid GitHub repository URL')
        return v

class ProcessingSummary(BaseModel):
    files_processed: int = Field(..., ge=0)
    processing_time_seconds: float = Field(..., ge=0)

class IngestSuccessResponse(BaseModel):
    success: bool = True
    repository_id: str = Field(
        ...,
        pattern=r'^repo-[a-f0-9]{8}$',
        description="ChromaDB collection identifier"
    )
    message: str = Field(..., min_length=1, max_length=500)
    processing_summary: ProcessingSummary

class IngestErrorResponse(BaseModel):
    success: bool = False
    error: str = Field(..., min_length=1, max_length=1000)
    error_code: str = Field(..., min_length=1, max_length=50)
