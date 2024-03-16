import ChatPyGPT

gpt = ChatPyGPT.Bot("YOUR_ACCESS_TOKEN")

# By default it is conversation mode, gpt.reset() method would reset the conversation
# The gpt.reset() doesn't perform any extra requests and it is literally executed in no time
# You can define your own function to get generative responses on every prompt (no conversation, no remembering of things)
def generative_prompt(prompt):
    gpt.prompt(prompt)
    gpt.reset()
    
# Use the above function yourself and it will not remember anything.

# Conversation Mode: Bot remembers your past responses and prompts
# Generative Mode: every prompt it forgets everything