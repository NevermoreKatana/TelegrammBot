from database.database_models import Greeting


def get_greeting_by_character_name(character_name, session):
    greeting = session.query(Greeting).filter_by(character_name=character_name).first()
    session.close()
    return greeting.greeting_text
