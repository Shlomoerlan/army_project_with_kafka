from sqlalchemy.orm import joinedload
from app.db.database_psql import session_maker
from app.db.models import User
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
        most_common_word, highest_frequency = max(words_rank, key=lambda x: x[1])
        return most_common_word

def create_user(user):
    user_data = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "ip_address": user.ip_address,
        "created_at": user.created_at,
        "device_info": {
            "os": user.device_info.os,
            "browser": user.device_info.browser
        } if user.device_info else None,
        "location": {
            "city": user.location.city,
            "country": user.location.country,
            "latitude": user.location.latitude,
            "longitude": user.location.longitude
        } if user.location else None,
        "hostage_sentences": [sentence.sentence_text for sentence in user.hostage_sentences],
        "explosive_sentences": [sentence.sentence_text for sentence in user.explosive_sentences]
    }
    return user_data