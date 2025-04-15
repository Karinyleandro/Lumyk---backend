"""Criando tabela de Livro

Revision ID: 03f368a77f41
Revises: 0a6b359800bd
Create Date: 2025-04-13 19:24:31.339056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03f368a77f41'
down_revision = '0a6b359800bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Livro',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('id_genero', sa.Integer(), nullable=False),
    sa.Column('id_autor', sa.Integer(), nullable=False),
    sa.Column('foto', sa.Text(), nullable=False),
    sa.Column('sinopse', sa.String(length=350), nullable=False),
    sa.Column('estoque', sa.Integer(), nullable=False),
    sa.Column('preco', sa.Float(), nullable=False),
    sa.Column('formato', sa.String(length=40), nullable=False),
    sa.Column('tipo', sa.String(length=40), nullable=False),
    sa.Column('titulo', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['id_autor'], ['Autor.id'], name='fk_livro_autor', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_genero'], ['GeneroLivro.id'], name='fk_livro_genero', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Livro')
    # ### end Alembic commands ###
