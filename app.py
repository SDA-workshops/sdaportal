from db.model import Article, User
from db.session import Session


def main():
    session = Session()
    article_1 = session.query(Article).filter(Article.id == 1).one()
    print(article_1.author)

    article_2 = session.query(Article).filter(Article.id == 3).one()
    print(article_2.author)

    user = session.query(User).filter_by(id=201).one()
    print(user.articles)

    user.articles.append(
        Article(title="Cute panda #2", content="...")
    )
    session.commit()

    print(user.articles)


if __name__ == "__main__":
    main()
