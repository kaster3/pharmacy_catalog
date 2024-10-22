from fastapi import APIRouter

from core import settings

from .products import router as products_router
from .some_endpoint import router as endpoint

router = APIRouter(
    prefix=settings.api.v1.prefix,
)


for rout in (endpoint, products_router):
    router.include_router(
        router=rout,
    )
