import PyOpenAI

gpt = PyOpenAI.Bot("YOUR_TOKEN_HERE")

print(gpt.get_access_token()) # Gets and prints your token

gpt.token("YOUR_UPDATED_TOKEN") # Changes your token, you can get it to see difference or just ask it a question "what I just asked you?"