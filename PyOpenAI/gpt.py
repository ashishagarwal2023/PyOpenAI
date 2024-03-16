import requests
import json
from uuid import uuid4

# Just to simplify
class TokenRateLimitedError(Exception):
    def __init__(self, message="The token is rate limited. Try again later.", smth=""):
        self.message = message
        super().__init__(self.message)

# The Main Class (Bot)
class Bot:
    def __init__(self, access_token: str = None): # it is optional however error without it
        self.session = requests.Session()
        self.session.headers["user-agent"] = "node"
        self.access_token = access_token
        self.conversation_id = None
    
    def get_access_token(self):
        return self.access_token
    
    def get_conv_id(self):
        return self.conversation_id

    def token(self, access_token: str):
        self.access_token = access_token
        self.conversation_id = None
    
    def reset(self):
        self.conversation_id = None
    
    def verify(self, token):
        toke = self.access_token
        self.token(token)
        try:
            self.prompt("Test message to verify token")
        except Exception as e:
            self.access_token = toke
            return False
        else:
            return True

    def prompt(self, prompt_text: str) -> str:
        body = {
            "action": "next",
            "conversation_mode": {"kind": "primary_assistant"},
            "force_paragen": False,
            "force_rate_limit": False,
            "history_and_training_disabled": True,
            "messages": [{
                "metadata": {},
                "author": {"role": "user"},
                "content": {"content_type": "text", "parts": [prompt_text]}
            }],
            "model": "text-davinci-002-render-sha",
            "parent_message_id": str(uuid4()),
            "timezone_offset_min": -330
        }

        if self.conversation_id is not None:
            try:
                body["conversation_id"] = self.conversation_id
            except:
                if self.access_token == "" or self.access_token == None:
                    raise NameError("You did not specify a token, cannot work.")
                raise TokenRateLimitedError("The token is rate limited. Try again later. From body conv id", body)

        response = self.session.post(
            url="https://chat.openai.com/backend-api/conversation",
            headers={
                "accept": "text/event-stream",
                "accept-language": "en-US",
                "authorization": f"Bearer {self.access_token}",
                "content-type": "application/json",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "Referer": "https://chat.openai.com",
                "Referrer-Policy": "strict-origin-when-cross-origin"
            },
            data=json.dumps(body)
        )

        data = {}
        for chunk in response.text.split("\n"):
            if chunk.startswith("data: {\"message\":"):
                try:
                    data = json.loads(chunk[6:])
                except json.JSONDecodeError: # Invalid JSON
                    raise Exception("Couldn't parse assistant's answer into a valid JSON. Might be a bug.")

        try:
            if data.get("conversation_id", "") != None:
                self.conversation_id = data["conversation_id"]
        except:
            if self.access_token == "" or self.access_token == None:
                raise NameError("You did not specify a token, cannot work.")
            raise TokenRateLimitedError("The token is rate limited. Try again later. From line 74", data)
            
        if data["message"]["status"] != "finished_successfully": # Recieved prompt was not complete
            raise Exception("The bot's message was not finished successfully, might be a error.")

        if data["message"]["content"]["content_type"] != "text": # Recieved output is not text
            raise Exception("The response did not gave the bot's response as text, most likely due to a bug.")

        message_parts = data["message"]["content"]["parts"]
        return "".join(message_parts)

# bot = Bot("token here")
# print(bot.prompt("Hello"))
# bot.reset()