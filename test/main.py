from requests import RequestException
import ChatPyGPT
# import time

token = "YOUR_ACCESS_TOKEN_HERE"
gpt = ChatPyGPT.Bot(token)
response = ""
mode = "conv"

def prompt_advanced(query):
    if mode == "conv":
        r = None
        try:
            r = gpt.prompt(query)
        except ChatPyGPT.gpt.TokenRateLimitedError:
            print("Either you provided a invalid token or you are rate limited ")
        except RequestException.exceptions.RequestException:
            print("Request failed to fetch. Try unblocking Python from your firewall list. You might need to fix your WiFi also.")
        except:
            print("Unknown error occured. Cannot get response.")
        return r
    if mode == "gen":
        r = None
        try:
            r = gpt.prompt(query)
        except ChatPyGPT.gpt.TokenRateLimitedError:
            print("Either you provided a invalid token or you are rate limited ")
        except RequestException.exceptions.RequestException:
            print("Request failed to fetch. Try unblocking Python from your firewall list. You might need to fix your WiFi also.")
        except:
            print("Unknown error occured. Cannot get response.")
        gpt.reset()
        if(r == None):
            return "No response received, this is typically because you didn't gave a valid token."
        return r


while True:
    action = input("0 to exit\n1 to prompt\n2 to change token\n3 to go generative\n4 to go conversative\n5 to give token\n6 to give conversation ID\n7 to verify current token\n8 for help\nYour Input: ")
    if action == "0":
        print("Exitting...")
        exit()
    if action == "1":
        p = input("User Prompt: ")
        response = prompt_advanced(p)
        print(f"ChatGPT: {response}")
    if action == "2":
        p = input("New token: ")
        if(gpt.verify(p)):
            print("The token is valid.")
            gpt.token(p)
            print("Changed token!")
        else:
            print("Invalid token provided or it is rate limited.")
            print("Token not changed.")
    if action == "3":
        mode = "gen"
        print("Changing chat mode to: Generative")
    if action == "4":
        mode = "conv"
        print("Changing chat mode to: Conversation")
    if action == "5":
        print(f"Your current token (DO NOT LEAK): {gpt.get_access_token()}")
    if action == "6":
        print(f"Current conversation ID: {gpt.get_conv_id()}")
    if action == "7":
        print("Verifying current token, please wait...")
        if(gpt.verify(gpt.get_access_token())):
            print("Current token is valid.")
        else:
            print("The current specificed token is invalid or rate limited.")
    if action == "8":
        print("Get help at my GitHub project! You can make a issue to get help, or report bugs.")
        print("You are also allowed to contribute! Make a PR and come on!")
        print("GitHub: github.com/ashishagarwal2023/pyopenai")
    # print("Continuing in 3 seconds...")
    # time.sleep(3)
