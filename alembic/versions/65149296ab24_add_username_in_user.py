"""add username in user

Revision ID: 65149296ab24
Revises: 72121fb7eb12
Create Date: 2023-07-19 17:39:53.672069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65149296ab24'
down_revision = '72121fb7eb12'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'users',
        sa.Column("username", sa.String)
        )


def downgrade() -> None:
    op.drop_column('users',"username")
