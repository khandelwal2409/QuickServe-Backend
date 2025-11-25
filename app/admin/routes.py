from fastapi import APIRouter

admin_router = APIRouter(prefix="/api/admin")


@admin_router.get("/health")
async def admin_health():
    """Simple admin health endpoint."""
    return {"admin_status": "ok"}
