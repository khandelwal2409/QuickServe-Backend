from fastapi import FastAPI
from .routes import router
from .admin.routes import admin_router
from .user.routes import user_router

app = FastAPI(title="QuickServe Dummy API", version="0.1.0")

app.include_router(router)
app.include_router(user_router)
app.include_router(admin_router)


@app.get("/")
async def root():
    return {"message": "QuickServe Dummy API. Navigate to /docs for OpenAPI UI or /api/health for a quick check."}
