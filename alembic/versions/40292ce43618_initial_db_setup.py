"""Initial db setup

Revision ID: 40292ce43618
Revises: 
Create Date: 2022-04-09 13:39:54.768393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40292ce43618'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'hashtags',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table(
        'subscriptions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=100), nullable=False),
        sa.Column('last_name', sa.String(length=100), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False),
        sa.Column('reg_date', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    op.create_table(
        'articles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=200), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('publication_date', sa.DateTime(), nullable=False),
        sa.Column('author_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('title')
    )
    op.create_table(
        'articles_hashtags',
        sa.Column('article_id', sa.Integer(), nullable=False),
        sa.Column('hashtag_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
        sa.ForeignKeyConstraint(['hashtag_id'], ['hashtags.id'], ),
        sa.PrimaryKeyConstraint('article_id', 'hashtag_id')
    )


def downgrade():
    op.drop_table('articles_hashtags')
    op.drop_table('articles')
    op.drop_table('users')
    op.drop_table('subscriptions')
    op.drop_table('hashtags')
