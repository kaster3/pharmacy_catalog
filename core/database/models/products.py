from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import IntIdPkMixin
from .tag_product_association import association_table

if TYPE_CHECKING:
    from .categories import Category
    from .tags import Tag


class Product(Base, IntIdPkMixin):
    name: Mapped[str] = mapped_column(String(30), unique=True)
    description: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    price: Mapped[int]
    # Связываем 2 таблицы
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    # Связываем 2 модели, чтобы обращаться с категории на ее продукты
    category: Mapped["Category"] = relationship(back_populates="products")
    # Связываем 2 модели, чтобы с продуктов можно было обратиться на их теги
    tags: Mapped[list["Tag"]] = relationship(
        back_populates="products",
        secondary=association_table,
    )
