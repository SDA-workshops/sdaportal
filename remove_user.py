from db.model import User
from db.session import Session


def main():
    session = Session()
    user = session.query(User).filter_by(id=43).one()

    for article in user.articles:
        print(article)

    session.delete(user)
    session.commit()


if __name__ == "__main__":
    main()
