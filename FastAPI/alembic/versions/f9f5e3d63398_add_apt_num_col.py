"""add apt num col

Revision ID: f9f5e3d63398
Revises: 9326fc35e7ab
Create Date: 2023-02-07 08:32:53.954229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9f5e3d63398'
down_revision = '9326fc35e7ab'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'address',
        sa.Column(
            'apt_num',
            sa.Integer(),
            nullable=True,
        )
    )


def downgrade() -> None:
    op.drop_column('address', 'apt_num')
