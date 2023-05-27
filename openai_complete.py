#!/usr/bin/env python

import openai
import os, sys

openai.api_key = os.environ["OPENAI_API_KEY"]
prompt=' '.join((sys.argv[1:]))
#print(prompt.strip())

# create a chat completion
completion = openai.Completion.create(
    model="text-davinci-003", 
    prompt="Gemerate a linux bash command to " + prompt.strip() + ""
    )

# print the chat completion
print(completion.choices[0].text.strip())

