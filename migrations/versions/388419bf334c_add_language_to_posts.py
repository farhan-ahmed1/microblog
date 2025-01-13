"""add language to posts

Revision ID: 388419bf334c
Revises: 09a905b06a0b
Create Date: 2025-01-13 17:29:04.120194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '388419bf334c'
down_revision = '09a905b06a0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    # ### end Alembic commands ###
