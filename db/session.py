from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:admin@localhost:3306/portal")

Session = sessionmaker(bind=engine)
