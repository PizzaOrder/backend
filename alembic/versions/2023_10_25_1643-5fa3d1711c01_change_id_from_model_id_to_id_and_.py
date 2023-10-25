"""Change id from 'model_id' to 'id' and foreign keys

Revision ID: 5fa3d1711c01
Revises: e6d251b458b1
Create Date: 2023-10-25 16:43:01.359419

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5fa3d1711c01"
down_revision: Union[str, None] = "e6d251b458b1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("addresses_user_id_fkey", "addresses", type_="foreignkey")
    op.create_foreign_key(None, "addresses", "users", ["user_id"], ["id"])
    op.add_column("order_items", sa.Column("id", sa.Integer(), nullable=False))
    op.drop_constraint("order_items_pizza_id_fkey", "order_items", type_="foreignkey")
    op.drop_constraint("order_items_order_id_fkey", "order_items", type_="foreignkey")
    op.create_foreign_key(None, "order_items", "orders", ["order_id"], ["id"])
    op.create_foreign_key(None, "order_items", "pizzas", ["pizza_id"], ["id"])
    op.drop_column("order_items", "item_id")
    op.add_column("orders", sa.Column("id", sa.Integer(), nullable=False))
    op.drop_constraint("orders_promo_id_fkey", "orders", type_="foreignkey")
    op.drop_constraint("orders_user_id_fkey", "orders", type_="foreignkey")
    op.create_foreign_key(None, "orders", "promo_codes", ["promo_id"], ["id"])
    op.create_foreign_key(None, "orders", "users", ["user_id"], ["id"])
    op.drop_column("orders", "order_id")
    op.add_column("pizzas", sa.Column("id", sa.Integer(), nullable=False))
    op.drop_column("pizzas", "pizza_id")
    op.add_column("promo_codes", sa.Column("id", sa.Integer(), nullable=False))
    op.drop_column("promo_codes", "promo_id")
    op.add_column("users", sa.Column("id", sa.Integer(), nullable=False))
    op.drop_column("users", "user_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column(
            "user_id",
            sa.INTEGER(),
            server_default=sa.text("nextval('users_user_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
    )
    op.drop_column("users", "id")
    op.add_column(
        "promo_codes",
        sa.Column(
            "promo_id",
            sa.INTEGER(),
            server_default=sa.text("nextval('promo_codes_promo_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
    )
    op.drop_column("promo_codes", "id")
    op.add_column(
        "pizzas",
        sa.Column("pizza_id", sa.INTEGER(), autoincrement=True, nullable=False),
    )
    op.drop_column("pizzas", "id")
    op.add_column(
        "orders",
        sa.Column("order_id", sa.INTEGER(), autoincrement=True, nullable=False),
    )
    op.drop_constraint(None, "orders", type_="foreignkey")
    op.drop_constraint(None, "orders", type_="foreignkey")
    op.create_foreign_key(
        "orders_user_id_fkey", "orders", "users", ["user_id"], ["user_id"]
    )
    op.create_foreign_key(
        "orders_promo_id_fkey", "orders", "promo_codes", ["promo_id"], ["promo_id"]
    )
    op.drop_column("orders", "id")
    op.add_column(
        "order_items",
        sa.Column("item_id", sa.INTEGER(), autoincrement=True, nullable=False),
    )
    op.drop_constraint(None, "order_items", type_="foreignkey")
    op.drop_constraint(None, "order_items", type_="foreignkey")
    op.create_foreign_key(
        "order_items_order_id_fkey", "order_items", "orders", ["order_id"], ["order_id"]
    )
    op.create_foreign_key(
        "order_items_pizza_id_fkey", "order_items", "pizzas", ["pizza_id"], ["pizza_id"]
    )
    op.drop_column("order_items", "id")
    op.drop_constraint(None, "addresses", type_="foreignkey")
    op.create_foreign_key(
        "addresses_user_id_fkey", "addresses", "users", ["user_id"], ["user_id"]
    )
    # ### end Alembic commands ###