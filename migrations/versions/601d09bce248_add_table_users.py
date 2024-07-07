"""add table users

Revision ID: 601d09bce248
Revises: 177d7012c6d2
Create Date: 2024-06-23 16:53:04.593078

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '601d09bce248'
down_revision: Union[str, None] = '177d7012c6d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('contacts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'contacts', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contacts', type_='foreignkey')
    op.drop_column('contacts', 'user_id')
    op.drop_table('users')
    # ### end Alembic commands ###
