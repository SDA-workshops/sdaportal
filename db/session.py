import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URI = os.getenv("DB_URI")
engine = create_engine(DB_URI)

Session = sessionmaker(bind=engine)
