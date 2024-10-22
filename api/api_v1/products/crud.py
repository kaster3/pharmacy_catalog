from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.models import Product

from .schemas import ProductCreate, ProductUpdate, ProductUpdatePartial


async def get_products(
    session: AsyncSession,
) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)
    # scalars выдает значения не в картежах, all дает не генератор, а список
    products = result.scalars().all()
    return list(products)


async def get_product_by_id(
    session: AsyncSession,
    product_id: int,
) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(
    session: AsyncSession,
    product_in: ProductCreate,
) -> Product:
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    # если на стороне бд происходят какие-то изменения при сохранение объекта,
    # то данные могут стать не актуальные
    await session.refresh(product)
    return product


async def update_product(
    session: AsyncSession,
    product: Product,
    product_update: ProductUpdate | ProductUpdatePartial,
    partial: bool = False,
) -> Product:
    # exclude_unset=True - Исключить то, что не было передано
    for name, value in product_update.model_dump(exclude_unset=partial):
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(
    session: AsyncSession,
    product: Product,
) -> None:
    await session.delete(product)
    # Обычно delete автоматически сохраняется
    await session.commit()
