"""made 

Revision ID: c325eb902fa2
Revises: 70fe643ab71a
Create Date: 2025-04-01 02:05:58.383187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c325eb902fa2'
down_revision = '70fe643ab71a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('indexed_file', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['filepath'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('indexed_file', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
