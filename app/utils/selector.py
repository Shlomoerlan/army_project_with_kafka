from app.db.database_psql import session_maker
from app.service.producers_service.explosive_producer import publish_explosive
from app.service.producers_service.hostage_producer import publish_hostage
from sqlalchemy.exc import SQLAlchemyError
from app.utils.createing_models import create_user, create_location, create_device_info, process_sentences


def save_user_to_db(session, user):
    try:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user.id
    except SQLAlchemyError as e:
        session.rollback()
        raise

def insert_user(user_data):
    try:
        with session_maker() as session:
            user = create_user(user_data)

            location = create_location(user_data['location'], user)
            user.location = location

            device_info = create_device_info(user_data['device_info'], user)
            user.device_info = device_info

            if sentences := user_data.get('sentences', []):
                process_sentences(sentences, user)

            return save_user_to_db(session, user)

    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        return None

def reorder_sentences(data):
    suspicious_keywords = ["explosi", "hostage"]
    reordered_sentences = sorted(
        data.get('sentences', []),
        key=lambda sentence: any(keyword in sentence for keyword in suspicious_keywords),
        reverse=True
    )
    data['sentences'] = reordered_sentences

def check_if_contains_suspicious_content(email):
    for sentence in email.get('sentences', []):
        print("check", sentence)
        if "explos" in sentence:
            reorder_sentences(email)
            publish_explosive(email)
            return
        elif "hostage" in sentence:
            reorder_sentences(email)
            publish_hostage(email)
            return