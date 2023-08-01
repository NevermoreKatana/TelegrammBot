import openai
import os


TOKEN = os.environ["GPT_TOKEN"]
openai.api_key = TOKEN


def send_message(message, propmpt):
    prompt = f"Instructions:{propmpt}{message}"

    completion = openai.ChatCompletion.create(
      model='gpt-3.5-turbo',
      messages=[{'role': 'user', 'content': f'{prompt}'}],
      temperature=0
    )

    return completion['choices'][0]['message']['content']
