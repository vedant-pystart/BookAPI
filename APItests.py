# import requests

# url = "https://randomuser.me/api"
# response = requests.get(url)
# data = response.json()

# gender = data['results'][0]['gender']

# print(gender)

import os
from openai import OpenAI


client = OpenAI(
api_key=os.environ.get("API_KEY"),  # This is the default and can be omitted
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o-mini",
)