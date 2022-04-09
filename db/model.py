from datetime import datetime

from faker import Faker
from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    reg_date = Column(DateTime, nullable=False, default=datetime.now)

    articles = relationship(
        "Article", back_populates="author",
        # cascade="all, delete, delete-orphan"
    )

    def __repr__(self):
        return f"User({self.id}, {self.first_name}, {self.last_name}, {self.email})"

    @staticmethod
    def create_fake_user():
        fake = Faker()
        return User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email()
        )

    def create_fake_article(self):
        fake = Faker()
        return Article(
            author_id=self.id,
            title=fake.paragraph(nb_sentences=1),
            content=fake.paragraph(nb_sentences=100)
        )


def create_fake_users(session, count=100):
    users_generated = 0
    while users_generated < count:
        try:
            session.add(User.create_fake_user())
            session.commit()
        except IntegrityError:
            session.rollback()
            continue
        users_generated += 1


class Hashtag(Base):
    __tablename__ = "hashtags"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    articles = relationship(
        "Article", back_populates="hashtags", secondary="articles_hashtags"
    )

    def __repr__(self):
        return f"Hashtag({self.id}, {self.name})"

    @staticmethod
    def creat_fake_hashtag():
        fake = Faker()
        return Hashtag(name=fake.word())


def create_fake_hashtags(session, count=100):
    hashtags_generated = 0
    while hashtags_generated < count:
        try:
            session.add(Hashtag.creat_fake_hashtag())
            session.commit()
        except IntegrityError:
            session.rollback()
            continue
        hashtags_generated += 1


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    publication_date = Column(DateTime, nullable=False, default=datetime.now)

    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    author = relationship(User, back_populates="articles")
    hashtags = relationship(
        Hashtag, back_populates="articles", secondary="articles_hashtags"
    )

    def __repr__(self):
        return f"Article({self.id}, {self.title})"


class ArticleHashtag(Base):
    __tablename__ = "articles_hashtags"

    article_id = Column(Integer, ForeignKey("articles.id"), primary_key=True)
    hashtag_id = Column(Integer, ForeignKey("hashtags.id"), primary_key=True)
