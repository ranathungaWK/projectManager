"""add default to project create_at

Revision ID: 379b67cb9c8c
Revises: 0e6275aa4084
Create Date: 2025-12-22 15:20:06.530477

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '379b67cb9c8c'
down_revision: Union[str, Sequence[str], None] = '0e6275aa4084'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column(
        "projects",
        "create_at",
        server_default=sa.func.now(),
        existing_nullable=False,
    )

def downgrade():
    op.alter_column(
        "projects",
        "create_at",
        server_default=None,
        existing_nullable=False,
    )


