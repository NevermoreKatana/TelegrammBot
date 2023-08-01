from database.database_models import Prompt


def get_prompt(session, name):
    prompt_result = session.query(Prompt).filter_by(character_name=name).first()
    return prompt_result.prompt
