import os

from openai import OpenAI
import time

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")

client = OpenAI(
    api_key=API_KEY,  # This is the default and can be omitted
)

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "I, I just woke up from a dream Where you and I had to",
#         }
#     ],
#     model="gpt-4o",
#     max_completion_tokens=2,  # max tokens returned
#     n=2,  # number of chat completions
#     temperature=0,  # randomness
# )

# # print(chat_completion.to_dict())

# # print the chat completion
# print(chat_completion.choices[0].message.content)

# Lyric Completion Assistant
# initial prompt with system message and 2 task examples
messages_list = [
    {
        "role": "system",
        "content": "I am a lyric completion assistant. When given a line from a song, I will provide the next line in the song.",
    },
    {"role": "user", "content": "I'm not afraid (I'm not afraid)"},
    {"role": "assistant", "content": "Yeah"},
    {"role": "user", "content": "To take a stand (to take a stand)"},
    {"role": "assistant", "content": "It's been a ride"},
    {"role": "user", "content": "Everybody (everybody)"},
]


for i in range():
    # create a chat completion
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages_list, max_tokens=15, n=1, temperature=0
    )

    # print the chat completion
    print(chat_completion.choices[0].message.content)

    new_message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content,
    }  # append new message to message list
    messages_list.append(new_message)
    time.sleep(0.1)
