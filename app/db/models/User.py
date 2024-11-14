from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.db.models import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    created_at = Column(String, nullable=False)

    device_info = relationship("DeviceInfo", back_populates="user", uselist=False)
    location = relationship("Location", back_populates="user", uselist=False)

    hostage_sentences = relationship("HostageSentence", back_populates="user")
    explosive_sentences = relationship("ExplosiveSentence", back_populates="user")
