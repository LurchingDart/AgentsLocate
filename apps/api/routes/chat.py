from fastapi import APIRouter, status
from core.models.chat import ChatRequest, ChatSuccessResponse, ChatErrorResponse
from apps.api.services.chat import ChatService
from apps.api.utils.error_handlers import handle_chat_error

router = APIRouter()
chat_service = ChatService()


@router.post(
    "/chat",
    response_model=ChatSuccessResponse,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ChatErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ChatErrorResponse},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": ChatErrorResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ChatErrorResponse},
        status.HTTP_501_NOT_IMPLEMENTED: {"model": ChatErrorResponse},
    },
    summary="Process a natural language query against a repository",
)
async def chat_with_repository(request: ChatRequest):
    """
    Processes a natural language query against a previously indexed repository.

    This endpoint routes requests to the chat service for conversational
    interaction, vector search, and response generation with file suggestions.
    """
    try:
        result = await chat_service.process_query(request)
        return result
    except Exception as e:
        return handle_chat_error(e)