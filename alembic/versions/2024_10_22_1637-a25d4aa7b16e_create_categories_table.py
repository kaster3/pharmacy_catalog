"""create categories table

Revision ID: a25d4aa7b16e
Revises: 
Create Date: 2024-10-22 16:37:45.645267

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "a25d4aa7b16e"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=30), nullable=False),
        sa.Column("description", sa.Text(), server_default="", nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_categories")),
        sa.UniqueConstraint("name", name=op.f("uq_categories_name")),
    )


def downgrade() -> None:
    op.drop_table("categories")
