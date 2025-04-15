"""Criando tabela de GeneroLivro

Revision ID: 0a6b359800bd
Revises: ae980af895f9
Create Date: 2025-04-13 19:22:40.985114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a6b359800bd'
down_revision = 'ae980af895f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('GeneroLivro',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('nome', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('GeneroLivro')
    # ### end Alembic commands ###
