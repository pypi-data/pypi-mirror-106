"""add asset type hover label

Revision ID: 7987667dbd43
Revises: 7113b0f00678
Create Date: 2020-06-04 11:36:42.684918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7987667dbd43"
down_revision = "7113b0f00678"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "asset_type", sa.Column("hover_label", sa.String(length=80), nullable=True)
    )
    # ### end Alembic commands ###
    op.drop_constraint(
        constraint_name="asset_asset_type_name_asset_type_fkey",
        table_name="asset",
        type_="foreignkey",
    )
    op.execute(
        "UPDATE asset_type SET name = 'one-way_evse' where name = 'charging_station'"
    )
    op.execute(
        "UPDATE asset_type SET display_name = 'one-way EVSE' where display_name = 'Charging station (uni-directional)'"
    )
    op.execute(
        "UPDATE asset SET asset_type_name = 'one-way_evse' where asset_type_name = 'charging_station'"
    )
    op.execute(
        "UPDATE asset_type SET name = 'two-way_evse' where name = 'bidirectional_charging_station'"
    )
    op.execute(
        "UPDATE asset_type SET display_name = 'two-way EVSE' where display_name = 'Charging station (bi-directional)'"
    )
    op.execute(
        "UPDATE asset SET asset_type_name = 'two-way_evse' where asset_type_name = 'bidirectional_charging_station'"
    )
    op.create_foreign_key(
        constraint_name="asset_asset_type_name_asset_type_fkey",
        source_table="asset",
        referent_table="asset_type",
        local_cols=["asset_type_name"],
        remote_cols=["name"],
    )
    op.execute(
        "UPDATE asset_type SET hover_label = 'uni-directional Electric Vehicle Supply Equipment' where name = 'one-way_evse'"
    )
    op.execute(
        "UPDATE asset_type SET hover_label = 'bi-directional Electric Vehicle Supply Equipment' where name = 'two-way_evse'"
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("asset_type", "hover_label")
    # ### end Alembic commands ###
    op.drop_constraint(
        constraint_name="asset_asset_type_name_asset_type_fkey",
        table_name="asset",
        type_="foreignkey",
    )
    op.execute(
        "UPDATE asset_type SET name = 'charging_station' where name = 'one-way_evse'"
    )
    op.execute(
        "UPDATE asset_type SET display_name = 'Charging station (uni-directional)' where display_name = 'one-way EVSE'"
    )
    op.execute(
        "UPDATE asset SET asset_type_name = 'charging_station' where asset_type_name = 'one-way_evse'"
    )
    op.execute(
        "UPDATE asset_type SET name = 'bidirectional_charging_station' where name = 'two-way_evse'"
    )
    op.execute(
        "UPDATE asset_type SET display_name = 'Charging station (bi-directional)' where display_name = 'two-way EVSE'"
    )
    op.execute(
        "UPDATE asset SET asset_type_name = 'bidirectional_charging_station' where asset_type_name = 'two-way_evse'"
    )
    op.create_foreign_key(
        constraint_name="asset_asset_type_name_asset_type_fkey",
        source_table="asset",
        referent_table="asset_type",
        local_cols=["asset_type_name"],
        remote_cols=["name"],
    )
