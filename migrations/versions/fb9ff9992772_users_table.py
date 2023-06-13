"""users table

Revision ID: fb9ff9992772
Revises: b999e41da3fe
Create Date: 2023-06-14 01:31:18.504093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb9ff9992772'
down_revision = 'b999e41da3fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('username', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_User_username'), 'User', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_User_username'), table_name='User')
    op.drop_column('User', 'username')
    # ### end Alembic commands ###
