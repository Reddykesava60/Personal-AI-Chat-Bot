import os
from dotenv import load_dotenv
load_dotenv()


from openai import OpenAI

client = OpenAI(api_key=os.environ["API_KEY"])

system_promt = "you are a friendly and supportive teaching assistant for Students. you ase also a Friendlytutor"

user_promt = input("What's your question? ")

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": system_promt},
        {"role": "user", "content": user_promt}
    ],
    model = "gpt-4o"
)

response_text = chat_completion.choices[0].message.content

print(response_text)
