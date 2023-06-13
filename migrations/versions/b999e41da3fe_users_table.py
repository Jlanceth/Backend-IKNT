"""users table

Revision ID: b999e41da3fe
Revises: 
Create Date: 2023-06-13 23:16:15.397518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b999e41da3fe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Color',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=8), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Token',
    sa.Column('value', sa.String(length=64), nullable=False),
    sa.Column('expiredAt', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('value')
    )
    op.create_table('Type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_User_login'), 'User', ['login'], unique=True)
    op.create_table('ProjectCategory',
    sa.Column('projectId', sa.Integer(), nullable=True),
    sa.Column('categoryId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoryId'], ['Category.id'], ),
    sa.ForeignKeyConstraint(['projectId'], ['Project.id'], )
    )
    op.create_table('ProjectColor',
    sa.Column('projectId', sa.Integer(), nullable=True),
    sa.Column('colorId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['colorId'], ['Color.id'], ),
    sa.ForeignKeyConstraint(['projectId'], ['Project.id'], )
    )
    op.create_table('ProjectImage',
    sa.Column('projectId', sa.Integer(), nullable=True),
    sa.Column('imageId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['imageId'], ['Image.id'], ),
    sa.ForeignKeyConstraint(['projectId'], ['Project.id'], )
    )
    op.create_table('ProjectType',
    sa.Column('projectId', sa.Integer(), nullable=True),
    sa.Column('typeId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['projectId'], ['Project.id'], ),
    sa.ForeignKeyConstraint(['typeId'], ['Type.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ProjectType')
    op.drop_table('ProjectImage')
    op.drop_table('ProjectColor')
    op.drop_table('ProjectCategory')
    op.drop_index(op.f('ix_User_login'), table_name='User')
    op.drop_table('User')
    op.drop_table('Type')
    op.drop_table('Token')
    op.drop_table('Project')
    op.drop_table('Image')
    op.drop_table('Color')
    op.drop_table('Category')
    # ### end Alembic commands ###