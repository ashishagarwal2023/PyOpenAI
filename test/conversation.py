# Conversation Mode Example
import ChatPyGPT # Import PyOpenAI

gpt = ChatPyGPT.Bot("YOUR_TOKEN_HERE") # Initialize a bot with a token
gpt.prompt("Hey there! My name is Ashish.") # On the first success prompt, it gets a conversation ID
gpt.prompt("What's my name?") # Your name is Ashish.
# Bot remembers our name, because of the conversation.
gpt.reset()
gpt.prompt("What is my name?") # Now it has started a new conversation, no more old knowledge.

print(gpt.get_conv_id()) # Get and print the conversation ID