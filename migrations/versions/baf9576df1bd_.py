"""empty message

Revision ID: baf9576df1bd
Revises: 2b3d9541972a
Create Date: 2020-01-15 17:37:16.606443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'baf9576df1bd'
down_revision = '2b3d9541972a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_camera', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.add_column('tb_server', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tb_server', 'create_time')
    op.drop_column('tb_camera', 'create_time')
    # ### end Alembic commands ###