'''SQLAlchemy engine for DB'''
from os import getenv
from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


db_uri = getenv('DATABASE_URL')
if 'postgresql' not in db_uri:
    db_uri = db_uri.replace('postgres', 'postgresql')

engine = create_engine(db_uri, echo=False)
LocalSession = sessionmaker(bind=engine)
Base = declarative_base()

# db session
def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
