"""Criando tabela Assinatura

Revision ID: da6584a98556
Revises: c6486b53534c
Create Date: 2025-04-12 21:13:39.764468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da6584a98556'
down_revision = 'c6486b53534c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Assinatura',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_usuario', sa.Integer(), nullable=False),
    sa.Column('tipo_assinatura', sa.String(length=40), nullable=False),
    sa.Column('data_inicio', sa.Date(), nullable=False),
    sa.Column('data_fim', sa.Date(), nullable=False),
    sa.Column('status', sa.String(length=40), nullable=False),
    sa.Column('preco_assinatura', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['id_usuario'], ['Usuario.id'], name='fk_assinatura_usuario', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Assinatura')
    # ### end Alembic commands ###
