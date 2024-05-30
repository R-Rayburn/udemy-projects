"""create address table

Revision ID: 5d44c0040688
Revises: 437119cdf0b3
Create Date: 2023-01-31 08:20:56.283793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d44c0040688'
down_revision = '437119cdf0b3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'address',
        sa.Column(
            'id',
            sa.Integer(),
            nullable=False,
            primary_key=True),
        sa.Column(
            'address1',
            sa.String(),
            nullable=False
        ),
        sa.Column(
            'address2',
            sa.String(),
            nullable=False
        ),
        sa.Column(
            'city',
            sa.String(),
            nullable=False
        ),
        sa.Column(
            'state',
            sa.String(),
            nullable=False
        ),
        sa.Column(
            'country',
            sa.String(),
            nullable=False
        ),
        sa.Column(
            'postalcode',
            sa.String(),
            nullable=False
        )
    )


def downgrade() -> None:
    op.drop_table('address')
