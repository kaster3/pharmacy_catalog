"""create products table

Revision ID: 4caaf9a86218
Revises: a25d4aa7b16e
Create Date: 2024-10-22 16:39:37.374688

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "4caaf9a86218"
down_revision: Union[str, None] = "a25d4aa7b16e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "products",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=30), nullable=False),
        sa.Column("description", sa.Text(), server_default="", nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["categories.id"],
            name=op.f("fk_products_category_id_categories"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_products")),
        sa.UniqueConstraint("name", name=op.f("uq_products_name")),
    )


def downgrade() -> None:
    op.drop_table("products")
