"""empty message

Revision ID: 3010664e8277
Revises: 0c223d321975
Create Date: 2018-09-16 20:24:37.318640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3010664e8277'
down_revision = '0c223d321975'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('answer', 'create_time')
    # ### end Alembic commands ###
