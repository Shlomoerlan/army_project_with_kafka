from app.db.database_psql import session_maker
from app.db.models import User, Location, DeviceInfo, HostageSentence, ExplosiveSentence


def insert_user_data(data: dict, sen: str):
    with session_maker() as session:
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
        if sen == "h":
            for sentence_text in sentences:
                sentence = HostageSentence(user_id=user.id, sentence_text=sentence_text)
                session.add(sentence)

        if sen == "e":
            for sentence_text in sentences:
                sentence = ExplosiveSentence(user_id=user.id, sentence_text=sentence_text)
                session.add(sentence)
        session.commit()



