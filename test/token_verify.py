# Test token and set it if it works.
import ChatPyGPT

gpt = ChatPyGPT.Bot("YOUR_TOKEN_HERE")
new_token = "MY_NEW_TOKEN" # The token we want to test and set

if(gpt.verify(new_token)): # True
    print("new_token is working and not rate limited")
    gpt.token(new_token)
else: # False
    print("new_token is not working or is rate limited")
    # If it has failed the test, do not use it if you want to not error.