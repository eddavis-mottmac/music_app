"""Initial Model Setup

Revision ID: 2c5ba9a66b42
Revises: 
Create Date: 2023-03-10 11:10:48.280661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c5ba9a66b42'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Components',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('component_type', sa.String(length=120), nullable=True),
    sa.Column('datasheet_link', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Components')
    # ### end Alembic commands ###
