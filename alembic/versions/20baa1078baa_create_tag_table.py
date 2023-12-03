"""Create Tag Table

Revision ID: 20baa1078baa
Revises: f9075b0d7433
Create Date: 2023-11-23 04:10:26.947182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20baa1078baa'
down_revision: Union[str, None] = 'f9075b0d7433'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tag_title', sa.String(length=15), nullable=False),
    sa.Column('register_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['register_id'], ['registers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tags_register_id'), 'tags', ['register_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tags_register_id'), table_name='tags')
    op.drop_table('tags')
    # ### end Alembic commands ###
