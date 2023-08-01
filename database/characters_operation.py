from sqlalchemy.orm.exc import NoResultFound
from database.database_models import Character
from Amplitude.send_events import send_event
from sqlalchemy.dialects.postgresql import insert


def add_or_replace_character(user_id, name, time, session):
    character_query = insert(Character).values(name=name, time=time,
                                               user_id=user_id)

    character_query = character_query.on_conflict_do_update(
        index_elements=['user_id'],
        set_={'name': name, 'time': time}
    )

    try:
        session.execute(character_query)
        session.commit()
        print("Запись успешно добавлена или обновлена.")
    except Exception as e:
        session.rollback()
        print(f"Произошла ошибка: {e}")
    finally:
        session.close()


def add_new_character_to_user(message, character_name, session):
    user_id = message.from_user.id
    username = message.from_user.username
    name = message.from_user.first_name
    surname = message.from_user.last_name
    time = message.date
    add_or_replace_character(user_id, character_name, time, session)

    data = [{
            "event_type": "choose character",
            "user_id": user_id,
            "username": username,
            "name": name,
            "surname": surname,
            "character_name": character_name
            }]

    send_event(data)


def character_exists(user_id, session):
    try:
        session.query(Character).filter(Character.user_id == user_id).one()
    except NoResultFound:
        return False
    except Exception as e:
        print("Ошибка при обработке запроса:", e)
        session.rollback()
    else:
        return True
    session.close()
