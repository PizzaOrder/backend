"""fix relationship between order and order_items

Revision ID: 7df2c2bcaa12
Revises: b0b18432db57
Create Date: 2023-12-05 00:40:51.213616

"""
from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = "7df2c2bcaa12"
down_revision: Union[str, None] = "b0b18432db57"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
