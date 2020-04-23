"""added usersinfo table

Revision ID: 5791dfeb3c8a
Revises: cef223b62db9
Create Date: 2020-04-23 20:51:16.324670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5791dfeb3c8a'
down_revision = 'cef223b62db9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usersinfo',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.add_column('users', sa.Column('email', sa.String(length=80), nullable=False))
    op.add_column('users', sa.Column('password_hash', sa.Text(), nullable=False))
    op.create_unique_constraint(None, 'users', ['email'])
    op.drop_column('users', 'first_name')
    op.drop_column('users', 'last_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_name', sa.TEXT(), nullable=False))
    op.add_column('users', sa.Column('first_name', sa.TEXT(), nullable=False))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    op.drop_table('usersinfo')
    # ### end Alembic commands ###
