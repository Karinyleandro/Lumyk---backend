"""Criando tabela de ItemCarrinho

Revision ID: 3caacd62ae3c
Revises: 345f136a35de
Create Date: 2025-04-13 19:28:54.030547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3caacd62ae3c'
down_revision = '345f136a35de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ItemCarrinho',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('id_carrinho', sa.Integer(), nullable=False),
    sa.Column('id_livro', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_carrinho'], ['Carrinho.id'], name='fk_itemcarrinho_carrinho', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_livro'], ['Livro.id'], name='fk_itemcarrinho_livro', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ItemCarrinho')
    # ### end Alembic commands ###
