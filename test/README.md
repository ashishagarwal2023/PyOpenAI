# ~/tests
This folder contains some files related to testing the package. If all files are working without error, it is sure that the package is working.
> Note: some of files here require your access token, you need to use it to test it. And, debug the files by inputting invalid tokens also.

`main.py` - advanced example, a command-line tool that will let you prompt, change token, go generative or conversative, see your token and see your conversation ID, with error handling, combining literally all the concepts of the PyOpenAI package.

`conversation.py` - example of how to reset conversation and get conversation ID

`generative.py` - example of how you can use reset conversation with prompt in a function to define your personal *generative_prompt* function which does not remember anything upon new prompt.

`prompt.py` - example of how to use prompt method (also with initialized bot), in the first complex, inline way and second, modern way.

`token_verify.py` - example of how you can use Bot.verify method to verify a token, then set it manually and confirm its working.

`tokens.py` - example of how you can change token using Bot.token method and also get the current access token with Bot.get_access_token method.

`with_error_handling.py` - example of how you can handle exceptions if invalid token, rate limited or any requests module error. You can also add more exceptions to handle even further.