from db.model import (
    Base,
    create_fake_users,
    create_fake_hashtags,
)
from db.session import Session


if __name__ == "__main__":
    session = Session()
    Base.metadata.create_all(session.get_bind())
    create_fake_users(session)
    create_fake_hashtags(session)
