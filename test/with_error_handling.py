from requests import RequestException
import ChatPyGPT

token = "YOUR_TOKEN_HERE"
gpt = ChatPyGPT.Bot(token)
response = ""
try:
    response = gpt.prompt("Hey, what's up?")
except ChatPyGPT.gpt.TokenRateLimitedError:
    """
    This error would occur if:
    1. Token is rate limited: you need to wait 1 hour
    2. Invalid token: a non-working token
    Great for error handling.
    """
    print("Either you provided a invalid token or you are rate limited ")
except RequestException.exceptions.RequestException:
    """
    This error is from requests package, occurs when the request has failed to fetch.
    Refer to requests's docs to see all exceptions for advanced handling.
    """
    print("Request failed to fetch. Try unblocking Python from your firewall list. You might need to fix your WiFi also.")
finally:
    # Then you can print the output
    print(response)