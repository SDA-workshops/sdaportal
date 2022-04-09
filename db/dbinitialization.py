from itertools import product

from db.model import (
    Base,
    create_fake_users,
    create_fake_hashtags,
    User,
    Article,
    Hashtag,
    ArticleHashtag
)
from db.session import Session


if __name__ == "__main__":
    session = Session()

    print("Create db tables...")
    Base.metadata.create_all(session.get_bind())

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
