"""initial

Revision ID: 01fe99da5716
Revises:
Create Date: 2018-03-20 10:29:28.864971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "01fe99da5716"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "asset_type",
        sa.Column("name", sa.String(length=80), nullable=False),
        sa.Column("is_consumer", sa.Boolean(), nullable=False),
        sa.Column("is_producer", sa.Boolean(), nullable=False),
        sa.Column("can_curtail", sa.Boolean(), nullable=False),
        sa.Column("can_shift", sa.Boolean(), nullable=False),
        sa.Column("daily_seasonality", sa.Boolean(), nullable=False),
        sa.Column("weekly_seasonality", sa.Boolean(), nullable=False),
        sa.Column("yearly_seasonality", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("name"),
    )
    op.create_index(
        op.f("ix_asset_type_can_curtail"), "asset_type", ["can_curtail"], unique=False
    )
    op.create_index(
        op.f("ix_asset_type_can_shift"), "asset_type", ["can_shift"], unique=False
    )
    op.create_table(
        "asset",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("asset_type_name", sa.String(length=80), nullable=False),
        sa.Column("name", sa.String(length=80), nullable=True),
        sa.Column("display_name", sa.String(length=80), nullable=True),
        sa.Column("capacity_in_mw", sa.Float(), nullable=False),
        sa.Column("latitude", sa.Float(), nullable=False),
        sa.Column("longitude", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(["asset_type_name"], ["asset_type.name"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("display_name"),
        sa.UniqueConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("asset")
    op.drop_index(op.f("ix_asset_type_can_shift"), table_name="asset_type")
    op.drop_index(op.f("ix_asset_type_can_curtail"), table_name="asset_type")
    op.drop_table("asset_type")
    # ### end Alembic commands ###
