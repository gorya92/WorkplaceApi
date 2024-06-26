"""add workplace_cooldoun

Revision ID: 2708028b25cc
Revises: 5ef780615173
Create Date: 2024-06-12 20:40:45.833906

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2708028b25cc'
down_revision: Union[str, None] = '5ef780615173'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('workplace', sa.Column('last_notification_sent_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('workplace', 'last_notification_sent_at')
    # ### end Alembic commands ###
