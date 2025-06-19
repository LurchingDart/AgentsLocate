from fastapi import FastAPI

from apps.api.routes.health import router as health_router
from apps.api.routes.ingestion import router as ingestion_router
from apps.api.routes.chat import router as chat_router


# --- FastAPI Application ---
app = FastAPI(
    title="Agents Locate API",
    description="Stateless HTTP interface for AI-powered repository navigation and concept location workflows. Serves as the communication layer between client applications and the underlying multi-agent system.",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

# Register routers
app.include_router(health_router)
app.include_router(ingestion_router, prefix="/api", tags=["Repository Ingestion"])
app.include_router(chat_router, prefix="/api", tags=["Chat Interaction"])