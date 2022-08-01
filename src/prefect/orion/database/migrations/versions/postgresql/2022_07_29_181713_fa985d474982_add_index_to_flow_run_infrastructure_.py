"""add-index-to-flow-run-infrastructure_document_id

Revision ID: fa985d474982
Revises: add97ce1937d
Create Date: 2022-07-29 18:17:13.174765

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "fa985d474982"
down_revision = "add97ce1937d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        op.f("ix_flow_run__infrastructure_document_id"),
        "flow_run",
        ["infrastructure_document_id"],
        unique=False,
        postgresql_concurrently=True,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_flow_run__infrastructure_document_id"), table_name="flow_run"
    )
    # ### end Alembic commands ###
