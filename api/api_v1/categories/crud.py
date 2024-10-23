from sqlalchemy import select

from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.categories.schemas import CategoryCreate
from core.database.models import Category


async def get_categories(session: AsyncSession) -> list[Category]:
    stmt = select(Category).order_by(Category.id)
    result: Result = await session.execute(stmt)
    categories = result.scalars().all()
    # products = await session.scalars(stmt)
    return list(categories)


async def create_category(
    session: AsyncSession,
    category_in: CategoryCreate,
) -> Category:
    category = Category(**category_in.model_dump())
    session.add(category)
    await session.commit()
    await session.refresh(category)
    return category
