from core.models.chat import ChatRequest, ChatSuccessResponse


class ChatService:
    """Service for handling chat operations."""

    async def process_query(self, request: ChatRequest) -> ChatSuccessResponse:
        """
        Processes a natural language query through the chat agent.

        Args:
            request: Chat request with message, repository ID, and optional history

        Returns:
            ChatSuccessResponse: Agent response with file suggestions and metadata

        Raises:
            NotImplementedError: When real agent integration is pending
        """
        # TODO: Integrate with actual LangGraph chat agent
        # from agents.chat import ChatAgent
        # agent = ChatAgent()
        # return await agent.process_query(request)

        raise NotImplementedError("Chat agent integration pending")