"""address

Revision ID: 72121fb7eb12
Revises: de7fa945c55d
Create Date: 2023-07-19 17:30:13.445525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72121fb7eb12'
down_revision = 'de7fa945c55d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "address",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("area", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("state", sa.String(), nullable=False),
        sa.Column("pincode", sa.String(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user.id"], name="address_user_id_fkey", ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("address")
