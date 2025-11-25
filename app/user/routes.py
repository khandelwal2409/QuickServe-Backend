from fastapi import APIRouter
from .menu_data import MENU

user_router = APIRouter(prefix="/api/user")


@user_router.get("/menu")
async def get_full_menu():
    """Return the dummy restaurant menu loaded from `menu_data.py`."""
    return {"menu": MENU}
