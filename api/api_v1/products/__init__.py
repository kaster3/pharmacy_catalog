from fastapi import APIRouter

from .handlers import router as products_router

router = APIRouter()
router.include_router(products_router)
