from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.db.database_psql import session_maker
from app.db.models import User
from sqlalchemy.orm import Session
from collections import Counter
from app.db.models import HostageSentence, ExplosiveSentence


def get_user_by_email(email: str):
    with session_maker() as session:
        return session.query(User).options(
            joinedload(User.device_info),
            joinedload(User.location),
            joinedload(User.hostage_sentences),
            joinedload(User.explosive_sentences)
        ).filter(User.email == email).first()



def get_most_common_words():
    with session_maker() as session:
        hostage_sentences = session.query(HostageSentence.sentence_text).all()
        explosive_sentences = session.query(ExplosiveSentence.sentence_text).all()

        all_sentences = [sentence.sentence_text for sentence in hostage_sentences + explosive_sentences]

        words = []
        for sentence in all_sentences:
            words.extend(sentence.lower().split())

        words_rank = Counter(words).most_common()

        return words_rank
