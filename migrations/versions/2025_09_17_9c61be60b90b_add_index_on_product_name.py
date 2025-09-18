"""add index on product.name

Revision ID: 9c61be60b90b
Revises: 741b7d7ad52f
Create Date: 2025-09-17 19:23:17.690616

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c61be60b90b'
down_revision: Union[str, Sequence[str], None] = '741b7d7ad52f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_index("idx_product_name", "products", ["name"], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index("idx_product_name", table_name="products")
