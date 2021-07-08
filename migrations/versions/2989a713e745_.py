"""empty message

Revision ID: 2989a713e745
Revises: 
Create Date: 2021-07-02 18:34:58.854589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2989a713e745'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###