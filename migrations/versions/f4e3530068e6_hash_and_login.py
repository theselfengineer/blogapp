"""hash and login

Revision ID: f4e3530068e6
Revises: 54ff5f59f65c
Create Date: 2018-05-02 18:41:29.240078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4e3530068e6'
down_revision = '54ff5f59f65c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('editors', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=128), nullable=True))
        batch_op.drop_index('ix_editors_password')
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('editors', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=20), nullable=True))
        batch_op.create_index('ix_editors_password', ['password'], unique=1)
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
