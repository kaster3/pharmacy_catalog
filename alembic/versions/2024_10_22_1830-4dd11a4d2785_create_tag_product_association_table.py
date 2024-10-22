"""create tag_product_association table

Revision ID: 4dd11a4d2785
Revises: 46b0688455be
Create Date: 2024-10-22 18:30:39.895130

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4dd11a4d2785"
down_revision: Union[str, None] = "46b0688455be"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tag_product_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("tag_name", sa.String(length=30), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.id"],
            name=op.f("fk_tag_product_association_product_id_products"),
        ),
        sa.ForeignKeyConstraint(
            ["tag_name"],
            ["tags.name"],
            name=op.f("fk_tag_product_association_tag_name_tags"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_tag_product_association")),
        sa.UniqueConstraint("tag_name", "product_id", name="index_unique_tag_product"),
    )


def downgrade() -> None:
    op.drop_table("tag_product_association")
