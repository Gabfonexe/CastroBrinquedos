"""empty message

Revision ID: d02b92dfd84d
Revises: 781bdf35cb25
Create Date: 2025-05-10 20:21:49.644262

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd02b92dfd84d'
down_revision = '781bdf35cb25'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Products', sa.Column('default_stock', sa.String(length=180), nullable=True))


def downgrade():
    op.drop_column('Products', 'default_stock')
    
