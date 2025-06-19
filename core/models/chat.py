from pydantic import BaseModel, Field, field_validator

class ConversationEntry(BaseModel):
    role: str = Field(..., pattern=r'^(user|agent)$')
    content: str = Field(..., min_length=1, max_length=5000)

class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=5000,
        description="User's natural language query"
    )
    repository_id: str = Field(
        pattern=r'^repo-[a-f0-9]{8}$',
        description="Repository identifier from ingestion"
    )
    conversation_history: list[ConversationEntry] | None = Field(
        None,
        max_items=10,
        description="Previous conversation context"
    )

    @field_validator('conversation_history')
    @classmethod
    def validate_conversation_history(cls, v: list | None) -> list | None:
        if v is not None and len(v) > 10:
            raise ValueError('Conversation history limited to 10 entries')
        return v

class FileSuggestion(BaseModel):
    file_name: str = Field(..., min_length=1, max_length=255)
    file_path: str = Field(..., min_length=1, max_length=1000)
    github_url: str = Field(..., min_length=1, max_length=2000)
    description: str = Field(..., min_length=1, max_length=5000)
    relevance_score: float = Field(..., ge=0.0, le=1.0)

class ChatMetadata(BaseModel):
    processing_time_ms: int = Field(..., ge=0)
    search_strategy: str = Field(..., min_length=1, max_length=100)

class ChatSuccessResponse(BaseModel):
    response: str = Field(..., min_length=1, max_length=10000)
    file_suggestions: list[FileSuggestion] = Field(
        ...,
        max_items=20,
        description="Ranked list of relevant files"
    )
    metadata: ChatMetadata

class ChatErrorResponse(BaseModel):
    success: bool = False
    error: str = Field(..., min_length=1, max_length=1000)
    error_code: str = Field(..., min_length=1, max_length=50)
