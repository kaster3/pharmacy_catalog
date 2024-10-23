from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .tag_product_association import association_table

if TYPE_CHECKING:
    from .products import Product


class Tag(Base):
    name: Mapped[str] = mapped_column(String(30), primary_key=True)
    # Связываем 2 модели, чтобы с тегов можно было обратиться на их продукты
    products: Mapped[list["Product"]] = relationship(
        back_populates="tags",
        secondary=association_table,
    )
