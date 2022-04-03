from sqlalchemy import or_

from db.session import Session
from db.model import User


def main():
    session = Session()
    users_query = session.query(User).filter(
        or_(
            User.email == "bob.marley@gmail.com",
            User.first_name == "Robert",
            User.first_name == "Mike"
        )
    )
    for user in users_query:
        print(user)


if __name__ == "__main__":
    main()
