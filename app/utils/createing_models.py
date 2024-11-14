from sqlalchemy.orm import Session
from app.db.models import User, Location, DeviceInfo, HostageSentence, ExplosiveSentence  # Adjust import path as needed

def insert_user_data(session: Session, data: dict):
    # Insert User
    user = User(
        username=data['username'],
        email=data['email'],
        ip_address=data['ip_address'],
        created_at=data['created_at']
    )
    session.add(user)
    session.flush()

    location_data = data.get('location', {})
    location = Location(
        user_id=user.id,
        city=location_data.get('city'),
        country=location_data.get('country'),
        latitude=location_data.get('latitude'),
        longitude=location_data.get('longitude')
    )
    session.add(location)

    device_data = data.get('device_info', {})
    device_info = DeviceInfo(
        user_id=user.id,
        os=device_data.get('os'),
        browser=device_data.get('browser')
    )
    session.add(device_info)

    sentences = data.get('sentences', [])
    for sentence_text in sentences:
        if "hostage" in sentence_text:
            sentence = HostageSentence(user_id=user.id, sentence_text=sentence_text)
            session.add(sentence)
        elif "explosive" in sentence_text:
            sentence = ExplosiveSentence(user_id=user.id, sentence_text=sentence_text)
            session.add(sentence)

    session.commit()



