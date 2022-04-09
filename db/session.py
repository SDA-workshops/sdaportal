import configparser
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()
config.read(f"{os.getcwd()}/alembic.ini")
DB_URI = config["alembic"]["sqlalchemy.url"]

engine = create_engine(DB_URI)
Session = sessionmaker(bind=engine)
