from sqlalchemy import Table, Column, ForeignKey, Integer, UniqueConstraint
from .base import Base

association_table = Table(
    "tag_product_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "tag_name",
        ForeignKey("tags.name"),
        nullable=False,
    ),
    Column(
        "product_id",
        ForeignKey("products.id"),
        nullable=False,
    ),
    UniqueConstraint(
        "tag_name",
        "product_id",
        name="index_unique_tag_product",
    ),
)
