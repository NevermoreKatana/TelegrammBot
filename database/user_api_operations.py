from database.database_models import UserRequest, Character
from openAi import send_message
from Amplitude.send_events import send_event
from database.prompts_operation import get_prompt


def save_request_response(request, session, user_id):
    existing_request = session.query(UserRequest).filter_by(user_id=user_id,
                                                            request=request).first()

    prompt_character = session.query(Character).filter_by(user_id=user_id).first()
    prompt = get_prompt(session, prompt_character.name)
    print(prompt)

    response = send_message(request, propmpt=prompt)

    data = [{
            "event_type": "API request",
            "user_id": user_id,
            "request": str(request)
            }]

    send_event(data)

    if existing_request:
        existing_request.response = response
    else:

        new_request = UserRequest(user_id=user_id, request=request, response=response)

        data = [{
                "event_type": "API response",
                "user_id": user_id,
                "response": str(response)
                }]

        send_event(data)
        session.add(new_request)

    session.commit()

    session.close()
    return response
