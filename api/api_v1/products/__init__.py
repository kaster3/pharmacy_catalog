from fastapi import APIRouter

from .handlers import router as products_router

router = APIRouter()

for r in (products_router,):
    router.include_router(router=r)
