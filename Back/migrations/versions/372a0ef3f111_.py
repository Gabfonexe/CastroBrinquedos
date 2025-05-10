"""empty message

Revision ID: 372a0ef3f111
Revises: d02b92dfd84d
Create Date: 2025-05-10 20:24:47.355746

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '372a0ef3f111'
down_revision = 'd02b92dfd84d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Users', sa.Column('default_stock', sa.Integer(), nullable=False))


def downgrade():
    op.drop_column('Users', 'default_stock')