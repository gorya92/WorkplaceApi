"""add new parametrs1

Revision ID: ad110a1059d9
Revises: a54ff1c1edea
Create Date: 2024-05-22 16:54:11.945940

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad110a1059d9'
down_revision: Union[str, None] = 'a54ff1c1edea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('device_token', sa.String(), nullable=True))
    op.add_column('workplace', sa.Column('title', sa.Integer(), nullable=False))
    op.add_column('workplace', sa.Column('alert_period', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('workplace', 'alert_period')
    op.drop_column('workplace', 'title')
    op.drop_column('user', 'device_token')
    # ### end Alembic commands ###
