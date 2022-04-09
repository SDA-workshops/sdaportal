from db.model import Article, Hashtag
from db.session import Session


def main():
    session = Session()
    article = session.query(Article).filter_by(id=14).one()

    print(
        f"The following hashtags have been used in {article.title}:"
    )
    for hashtag in article.hashtags:
        print(f"#{hashtag.name}")

    hashtag = session.query(Hashtag).filter_by(id=1).one()
    print(
        f"Hashtag #{hashtag.name} have been used in the following articles"
    )
    for article in hashtag.articles:
        print(article.title)


if __name__ == "__main__":
    main()
