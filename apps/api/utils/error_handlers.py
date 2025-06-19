from fastapi import status
from fastapi.responses import JSONResponse
from core.models.repository import IngestErrorResponse
from core.models.chat import ChatErrorResponse
from apps.api.exceptions.__init___ import (
    InvalidURLError, InvalidTokenError, InsufficientPermissionsError,
    RepoTooLargeError, ProcessingFailedError, StorageError
)


def handle_ingestion_error(error: Exception) -> JSONResponse:
    """
    Handle ingestion-specific errors with appropriate HTTP status codes.

    Args:
        error: The exception that occurred

    Returns:
        JSONResponse: Formatted error response
    """
    if isinstance(error, InvalidURLError):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=IngestErrorResponse(error=str(error), error_code="INVALID_URL").dict(),
        )
    elif isinstance(error, InvalidTokenError):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=IngestErrorResponse(error=str(error), error_code="INVALID_TOKEN").dict(),
        )
    elif isinstance(error, InsufficientPermissionsError):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content=IngestErrorResponse(error=str(error), error_code="INSUFFICIENT_PERMISSIONS").dict(),
        )
    elif isinstance(error, FileNotFoundError):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=IngestErrorResponse(error=str(error), error_code="REPO_NOT_FOUND").dict(),
        )
    elif isinstance(error, PermissionError):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=IngestErrorResponse(error=str(error), error_code="PRIVATE_REPO_NO_TOKEN").dict(),
        )
    elif isinstance(error, RepoTooLargeError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=IngestErrorResponse(error=str(error), error_code="REPO_TOO_LARGE").dict(),
        )
    elif isinstance(error, ProcessingFailedError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=IngestErrorResponse(error=str(error), error_code="PROCESSING_FAILED").dict(),
        )
    elif isinstance(error, StorageError):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=IngestErrorResponse(error=str(error), error_code="STORAGE_ERROR").dict(),
        )
    elif isinstance(error, NotImplementedError):
        return JSONResponse(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            content=IngestErrorResponse(
                error="Ingestion agent not yet implemented",
                error_code="NOT_IMPLEMENTED",
            ).dict(),
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=IngestErrorResponse(
                error="An unexpected error occurred during repository processing.",
                error_code="AGENT_ERROR",
            ).dict(),
        )


def handle_chat_error(error: Exception) -> JSONResponse:
    """
    Handle chat-specific errors with appropriate HTTP status codes.

    Args:
        error: The exception that occurred

    Returns:
        JSONResponse: Formatted error response
    """
    if isinstance(error, FileNotFoundError):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=ChatErrorResponse(error=str(error), error_code="REPO_NOT_INDEXED").dict(),
        )
    elif isinstance(error, ValueError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=ChatErrorResponse(error=str(error), error_code="QUERY_PROCESSING_FAILED").dict(),
        )
    elif isinstance(error, ConnectionError):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=ChatErrorResponse(error=str(error), error_code="AGENT_UNAVAILABLE").dict(),
        )
    elif isinstance(error, NotImplementedError):
        return JSONResponse(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            content=ChatErrorResponse(
                error="Chat agent not yet implemented",
                error_code="NOT_IMPLEMENTED",
            ).dict(),
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=ChatErrorResponse(
                error="An unexpected error occurred while processing the chat request.",
                error_code="AGENT_ERROR",
            ).dict(),
        )