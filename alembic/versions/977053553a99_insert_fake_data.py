"""Insert fake data

Revision ID: 977053553a99
Revises: c415272f51df
Create Date: 2022-04-09 14:04:24.544368

"""
from itertools import product

# revision identifiers, used by Alembic.
from db.model import create_fake_users, create_fake_hashtags, ArticleHashtag, User, Article, Hashtag
from db.session import Session

revision = '977053553a99'
down_revision = 'c415272f51df'
branch_labels = None
depends_on = None


session = Session()


def create_fake_data(session):
    print("Creating fake users...")
    create_fake_users(session)

    print("Creating fake hashtags...")
    create_fake_hashtags(session)

    print("Creating fake articles...")
    for user in session.query(User):
        session.add_all([
            user.create_fake_article() for _ in range(10)
        ])
    session.commit()

    print("Connecting articles with hashtags...")
    articles = session.query(Article).limit(10)
    hashtags = session.query(Hashtag).limit(10)
    session.add_all([
        ArticleHashtag(article_id=article.id, hashtag_id=hashtag.id)
        for article, hashtag in product(articles, hashtags)
    ])
    session.commit()


def upgrade():
    create_fake_data(session)


def downgrade():
    engine = session.get_bind()
    engine.execute("TRUNCATE articles_hashtags")
    engine.execute("TRUNCATE articles")
    engine.execute("TRUNCATE hashtags")
    engine.execute("TRUNCATE users")
    engine.execute("TRUNCATE subscriptions")
