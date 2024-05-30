"""create phone number for user col

Revision ID: 437119cdf0b3
Revises: 
Create Date: 2023-01-31 08:13:09.821513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '437119cdf0b3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'users',
        sa.Column('phone_number',
                  sa.String(),
                  nullable=True),
    )


def downgrade() -> None:
    op.drop_column(
        'users',
        'phone_number'
    )
