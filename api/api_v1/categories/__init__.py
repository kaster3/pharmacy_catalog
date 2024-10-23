from fastapi import APIRouter

from .handlers import router as categories_router

router = APIRouter()
router.include_router(categories_router)
