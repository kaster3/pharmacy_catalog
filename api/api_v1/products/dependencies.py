from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.db_helper import db_helper
from core.database.models import Product

from . import crud


async def get_products_by_id(
    product_id: Annotated[int, Path],
    session: Annotated["AsyncSession", Depends(db_helper.get_session)],
) -> Product:
    product = await crud.get_product_by_id(product_id=product_id, session=session)
    if product is not None:
        return product
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product not found")
