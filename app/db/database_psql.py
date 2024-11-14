from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from app.db.models import Base
from sqlalchemy import create_engine
from app.db.models import User, Location, DeviceInfo, ExplosiveSentence, HostageSentence
from app.settings.config import DB_URL

load_dotenv(verbose=True)

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)

def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)





