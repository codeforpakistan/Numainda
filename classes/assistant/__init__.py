import openai


class Assistant:

    def __init__(self, openai_api_key=None):
        openai.api_key = openai_api_key

    def get_client(self):
        return openai
