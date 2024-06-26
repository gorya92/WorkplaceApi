"""add worker url no data

Revision ID: 9c3eac3743ca
Revises: 8ebee59a6465
Create Date: 2024-05-25 13:50:05.619038

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c3eac3743ca'
down_revision: Union[str, None] = '8ebee59a6465'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('worker',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('workplace_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['workplace_id'], ['workplace.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('worker')
    # ### end Alembic commands ###
