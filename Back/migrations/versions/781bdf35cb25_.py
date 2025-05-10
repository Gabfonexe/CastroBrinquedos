"""empty message

Revision ID: 781bdf35cb25
Revises: 00ecf27d0743
Create Date: 2025-05-10 18:32:33.909192

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '781bdf35cb25'
down_revision = '00ecf27d0743'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Users', sa.Column('is_checked', sa.Boolean(), nullable=False))


def downgrade():
    op.drop_column('Users', 'is_checked')