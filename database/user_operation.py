from Amplitude.send_events import send_event
from database.database_models import User

FOR_REGISTERED = 'Вы уже зарегестрированны!'
GREETINGS = ("Привет! Это бот Character.AI! Ты можешь создать своего персонажа, "
             "который будет со всеми характеристиками как ты хочешь! "
             "Он сможет помогать тебе в творчестве или ведении текстовой ролевой игры!")


def add_new_user(message, session):
    existing_user = session.query(User).filter_by(user_id=message.from_user.id).first()
    if existing_user:
        return FOR_REGISTERED
    else:
        existing_user = User(
            user_id=message.from_user.id,
            username=message.from_user.username,
            name=message.from_user.first_name,
            surname=message.from_user.last_name,
            time=message.date
        )

        data = [{
                "event_type": "register",
                "user_id": message.from_user.id,
                "username": message.from_user.username,
                "name": message.from_user.first_name,
                "surname": message.from_user.last_name,
                }]

        send_event(data)

        session.add(existing_user)
        session.commit()
        session.close()
        return GREETINGS
