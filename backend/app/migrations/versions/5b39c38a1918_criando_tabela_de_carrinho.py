"""Criando Tabela de Carrinho

Revision ID: 5b39c38a1918
Revises: fcff2451b72b
Create Date: 2025-04-15 23:29:49.393608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b39c38a1918'
down_revision = 'fcff2451b72b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Carrinho',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('id_usuario', sa.Integer(), nullable=False),
    sa.Column('data_criacao', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['id_usuario'], ['Usuario.id'], name='fk_carrinho_usuario', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Carrinho')
    # ### end Alembic commands ###
