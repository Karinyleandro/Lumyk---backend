"""add frete to Estado

Revision ID: 2ffd7efe1d47
Revises: 3d5109fc0110
Create Date: 2025-05-02 14:14:43.873981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ffd7efe1d47'
down_revision = '3d5109fc0110'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Estado', schema=None) as batch_op:
        batch_op.add_column(sa.Column('taxa_frete', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Estado', schema=None) as batch_op:
        batch_op.drop_column('taxa_frete')

    # ### end Alembic commands ###
