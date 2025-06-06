"""empty message

Revision ID: d99adf5071f8
Revises: 
Create Date: 2025-05-29 21:50:34.592956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd99adf5071f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Calendar',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('day_quantity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Date Unavailable',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('reason', sa.String(length=120), nullable=True),
    sa.Column('product', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Dates',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('total_amount', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Products',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('type', sa.Enum('PULA_PULA_MEDIO', 'PULA_PULA_GRANDE', 'CASA_BOLINHA_PEQUENA', 'CASA_BOLINHA_GRANDE', 'TOBOGA_INFLAVEL', 'FUTEBOL_SABAO_INFLAVEL', 'GUERRA_COTONETE_INFLAVEL', 'CASTELINHO_INFLAVEL', 'PEBOLIM', 'FLIPERAMA', 'TORO_MECANICO', name='types_products'), nullable=False),
    sa.Column('description', sa.String(length=180), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('is_available', sa.Boolean(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('image', sa.String(length=250), nullable=True),
    sa.Column('lost_quantity', sa.Integer(), nullable=True),
    sa.Column('static_quantity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('type')
    )
    op.create_table('leads',
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('number', sa.String(length=30), nullable=True),
    sa.Column('is_confirmed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('number', sa.String(length=30), nullable=True),
    sa.Column('message', sa.String(length=700), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('budget', sa.Float(), nullable=True),
    sa.Column('is_confirmed', sa.Boolean(), nullable=True),
    sa.Column('is_checked', sa.Boolean(), nullable=True),
    sa.Column('is_dayli_confirmed', sa.Boolean(), nullable=True),
    sa.Column('products', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_products',
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('product_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['Products.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'product_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_products')
    op.drop_table('users')
    op.drop_table('leads')
    op.drop_table('Products')
    op.drop_table('Dates')
    op.drop_table('Date Unavailable')
    op.drop_table('Calendar')
    # ### end Alembic commands ###
