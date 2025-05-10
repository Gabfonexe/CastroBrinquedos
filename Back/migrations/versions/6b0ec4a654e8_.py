"""empty message

Revision ID: 6b0ec4a654e8
Revises: 463836dd3763
Create Date: 2025-05-09 19:45:45.720051

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6b0ec4a654e8'
down_revision = '463836dd3763'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Products', sa.Column('description', sa.String(length=180), nullable=True))


def downgrade():
    op.drop_column('Products', 'description')
    
