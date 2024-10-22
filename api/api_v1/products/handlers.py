from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.db_helper import db_helper

from . import crud
from .dependencies import get_products_by_id
from .schemas import Product, ProductCreate, ProductUpdate, ProductUpdatePartial

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_products(session: Annotated["AsyncSession", Depends(db_helper.get_session)]):
    return await crud.get_products(session=session)


@router.get("/{product_id}", response_model=Product)
async def get_product_handler(product: Annotated[AsyncSession, Depends(get_products_by_id)]):
    return product


@router.post(
    "/",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
)
async def create_product_handler(
    product_in: ProductCreate,
    session: Annotated["AsyncSession", Depends(db_helper.get_session)],
):
    return await crud.create_product(product_in=product_in, session=session)


@router.put("/{product_id}", response_model=Product)
async def update_product(
    product: Annotated[Product, Depends(get_products_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.get_session)],
    product_update: ProductUpdate,
) -> Product:
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
    )


@router.patch("/{product_id}", response_model=Product)
async def update_product_partial(
    product: Annotated[Product, Depends(get_products_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.get_session)],
    product_update_partial: ProductUpdatePartial,
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update_partial,
    )


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product: Annotated[Product, Depends(get_products_by_id)],
    session: Annotated[AsyncSession, Depends(db_helper.get_session)],
) -> None:
    return await crud.delete_product(session=session, product=product)
