from core.models.repository import IngestRequest, IngestSuccessResponse


class IngestionService:
    """Service for handling repository ingestion operations."""

    async def process_repository(self, request: IngestRequest) -> IngestSuccessResponse:
        """
        Processes a GitHub repository through the ingestion agent.

        Args:
            request: Repository ingestion request with URL and optional token

        Returns:
            IngestSuccessResponse: Processing results and repository ID

        Raises:
            NotImplementedError: When real agent integration is pending
        """
        # TODO: Integrate with actual LangGraph ingestion agent
        # from agents.ingestion import IngestionAgent
        # agent = IngestionAgent()
        # return await agent.process_repository(request)

        raise NotImplementedError("Ingestion agent integration pending")
