from fastapi import APIRouter, status
from core.models.repository import IngestRequest, IngestSuccessResponse, IngestErrorResponse
from apps.api.services.ingestion import IngestionService
from apps.api.utils.error_handlers import handle_ingestion_error

router = APIRouter()
ingestion_service = IngestionService()


@router.post(
    "/ingest",
    response_model=IngestSuccessResponse,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": IngestErrorResponse},
        status.HTTP_401_UNAUTHORIZED: {"model": IngestErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": IngestErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": IngestErrorResponse},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": IngestErrorResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": IngestErrorResponse},
        status.HTTP_501_NOT_IMPLEMENTED: {"model": IngestErrorResponse},
    },
    summary="Ingest and process a GitHub repository",
)
async def ingest_repository(request: IngestRequest):
    """
    Processes a GitHub repository for vector indexing and analysis.

    This endpoint synchronously processes the repository through the
    ingestion service, which handles cloning, file analysis, AI summarization,
    and ChromaDB storage operations.
    """
    try:
        result = await ingestion_service.process_repository(request)
        return result
    except Exception as e:
        return handle_ingestion_error(e)