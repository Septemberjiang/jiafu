"""empty message

Revision ID: b418d4ff56d1
Revises: 85ff47c8f7bd
Create Date: 2020-01-07 13:50:35.293694

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b418d4ff56d1'
down_revision = '85ff47c8f7bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_camera', sa.Column('device_no', sa.String(length=50), nullable=True))
    op.drop_column('tb_camera', 'camera_state')
    op.add_column('tb_server', sa.Column('device_no', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tb_server', 'device_no')
    op.add_column('tb_camera', sa.Column('camera_state', mysql.VARCHAR(length=50), nullable=True))
    op.drop_column('tb_camera', 'device_no')
    # ### end Alembic commands ###
