#!/usr/bin/env python

import openai
import os, sys

openai.api_key = os.environ["OPENAI_API_KEY"]
prompt=' '.join((sys.argv[1:]))


# create a chat completion
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Generate a one line Linux bash command to " + prompt.strip() + "."}]
    )

# print the chat completion
print(completion.choices[0].message.content)
