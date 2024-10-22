from sqlalchemy.orm import Mapped

from .base import Base
from .mixins import IntIdPkMixin


class Product(Base, IntIdPkMixin):
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
