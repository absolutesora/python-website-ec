"""added follower

Revision ID: 64b4ea7754fe
Revises: 96bbb55e4cc6
Create Date: 2020-05-13 11:53:11.665953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64b4ea7754fe'
down_revision = '96bbb55e4cc6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###