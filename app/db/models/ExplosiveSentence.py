from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db.models import Base


class ExplosiveSentence(Base):
    __tablename__ = 'explosive_sentences'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    sentence_text = Column(String, nullable=False)

    user = relationship("User", back_populates="explosive_sentences")