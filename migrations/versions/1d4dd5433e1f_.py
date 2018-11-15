"""empty message

Revision ID: 1d4dd5433e1f
Revises: 9026b82d4d90
Create Date: 2018-11-15 17:53:44.496703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d4dd5433e1f'
down_revision = '9026b82d4d90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about_me', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'about_me')
    # ### end Alembic commands ###