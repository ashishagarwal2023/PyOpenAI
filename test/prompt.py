import PyOpenAI

# Bot(token=Null: str): Initialize a bot, token is optional but you need it to do prompts.
# Bot.prompt(prompt_text: str)
# response = PyOpenAI.Bot("YOUR_TOKEN_HERE").prompt("Hello there, GPT!")
# Like this, you can consider to do one-lined bot initializing, prompting and responsing.

gpt = PyOpenAI.Bot("YOUR_ACCESS_TOKEN")
response = gpt.prompt("Hello there, GPT!")
# Modern way

print(response)
