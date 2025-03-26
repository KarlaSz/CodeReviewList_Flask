"""Add priority column to Task model

Revision ID: 6d8a5df04b4f
Revises:
Create Date: 2025-03-25 20:46:29.367898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d8a5df04b4f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('priority', sa.String(), nullable=False, server_default='low'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_column('priority')

    # ### end Alembic commands ###