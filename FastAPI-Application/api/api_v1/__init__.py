from fastapi import APIRouter
from core.config import settings
from .users import router as user_router

router = APIRouter(
    tags=["Users"],
)

router.include_router(
    user_router,
    prefix="/users",
)
