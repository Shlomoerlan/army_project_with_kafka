from sqlalchemy.orm import sessionmaker, Session, declarative_base
from app.settings.config import DB_URL
from sqlalchemy import create_engine

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


    with session_maker() as session:

        session.commit()




