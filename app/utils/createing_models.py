from app.db.models import HostageSentence, ExplosiveSentence, DeviceInfo, User, Location


def create_user(data):
    return User(
        username=data['username'],
        email=data['email'],
        ip_address=data['ip_address'],
        created_at=data['created_at']
    )

def create_location(location_data, user):
    return Location(
        latitude=location_data['latitude'],
        longitude=location_data['longitude'],
        city=location_data['city'],
        country=location_data['country'],
        user_id=user.id
    )

def create_device_info(device_data, user):
    return DeviceInfo(
        browser=device_data['browser'],
        os=device_data['os'],
        user_id=user.id
    )

def process_sentences(sentences, user):
    for i, sentence in enumerate(sentences):
        if 'explos' in sentence:
            explosive_sentence = ExplosiveSentence(sentence_text=sentence, user_id=user.id)
            user.explosive_sentences.append(explosive_sentence)

            for next_sentence in sentences[i + 1:i + 3]:
                user.explosive_sentences.append(ExplosiveSentence(sentence_text=next_sentence, user_id=user.id))

        elif 'hostage' in sentence:
            hostage_sentence = HostageSentence(sentence_text=sentence, user_id=user.id)
            user.hostage_sentences.append(hostage_sentence)

            for next_sentence in sentences[i + 1:i + 3]:
                user.hostage_sentences.append(HostageSentence(sentence_text=next_sentence, user_id=user.id))

