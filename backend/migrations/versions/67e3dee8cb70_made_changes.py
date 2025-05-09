"""made changes

Revision ID: 67e3dee8cb70
Revises: 7a06b2cd6b95
Create Date: 2025-03-30 02:43:16.898086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67e3dee8cb70'
down_revision = '7a06b2cd6b95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cloud_storage_account', schema=None) as batch_op:
        batch_op.alter_column('access_token',
               existing_type=sa.VARCHAR(length=1000),
               type_=sa.String(length=20000),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cloud_storage_account', schema=None) as batch_op:
        batch_op.alter_column('access_token',
               existing_type=sa.String(length=20000),
               type_=sa.VARCHAR(length=1000),
               existing_nullable=False)

    # ### end Alembic commands ###
