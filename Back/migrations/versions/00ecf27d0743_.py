"""alter products table to make 'type' unique and keep primary key on 'id'

Revision ID: 00ecf27d0743
Revises: 6b0ec4a654e8
Create Date: 2025-05-09 20:02:35.708076
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '00ecf27d0743'
down_revision = '6b0ec4a654e8'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('Products', schema=None) as batch_op:
        # Garante que a coluna 'type' seja única
        batch_op.create_unique_constraint('uq_products_type', ['type'])


def downgrade():
    with op.batch_alter_table('Products', schema=None) as batch_op:
        # Remove a restrição de unicidade da coluna 'type'
        batch_op.drop_constraint('uq_products_type', type_='unique')
