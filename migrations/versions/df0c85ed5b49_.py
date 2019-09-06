"""empty message

Revision ID: df0c85ed5b49
Revises: 
Create Date: 2019-09-06 18:26:39.247874

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'df0c85ed5b49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('modulelog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('app_name', sa.String(), nullable=False),
    sa.Column('state', sa.Enum('STARTED', 'FINISHED', 'ERROR', name='job_states'), nullable=False),
    sa.Column('timestamp', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='modulelog'
    )
    op.create_index(op.f('ix_modulelog_modulelog_job_id'), 'modulelog', ['job_id'], unique=False, schema='modulelog')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_modulelog_modulelog_job_id'), table_name='modulelog', schema='modulelog')
    op.drop_table('modulelog', schema='modulelog')
    # ### end Alembic commands ###