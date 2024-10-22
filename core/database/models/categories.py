from typing import TYPE_CHECKING
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import IntIdPkMixin

if TYPE_CHECKING:
    from .products import Product


class Category(Base, IntIdPkMixin):
    name: Mapped[str] = mapped_column(String(30), unique=True)
    description: Mapped[str] = mapped_column(Text, default="", server_default="")
    # Связываем 2 модели, чтобы с продуктов можно было обратиться на их категорию
    products: Mapped[list["Product"]] = relationship(back_populates="category")
