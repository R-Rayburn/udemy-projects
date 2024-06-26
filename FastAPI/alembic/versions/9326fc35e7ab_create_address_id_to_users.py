"""create address id to users

Revision ID: 9326fc35e7ab
Revises: 5d44c0040688
Create Date: 2023-01-31 08:28:55.842726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9326fc35e7ab'
down_revision = '5d44c0040688'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'users',
        sa.Column(
            'address_id',
            sa.Integer(),
            nullable=True))
    op.create_foreign_key(
        'address_users_fk',
        source_table='users',
        referent_table='address',
        local_cols=['address_id'],
        remote_cols=['id'],
        ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint(
        'address_users_fk',
        table_name='users')
    op.drop_column(
        'users',
        'address_id')
