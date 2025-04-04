"""made 

Revision ID: 70fe643ab71a
Revises: a71932dc7b51
Create Date: 2025-04-01 01:56:26.363976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70fe643ab71a'
down_revision = 'a71932dc7b51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('indexed_file', schema=None) as batch_op:
        batch_op.drop_constraint('indexed_file_filepath_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('indexed_file', schema=None) as batch_op:
        batch_op.create_unique_constraint('indexed_file_filepath_key', ['filepath'])

    # ### end Alembic commands ###
