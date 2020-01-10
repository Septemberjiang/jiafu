"""empty message

Revision ID: 68d308c922b4
Revises: b418d4ff56d1
Create Date: 2020-01-07 14:57:54.450494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68d308c922b4'
down_revision = 'b418d4ff56d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'tb_camera', ['unique_camera_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tb_camera', type_='unique')
    # ### end Alembic commands ###