

class Configuration:

    api_key = None
    api_url = "https://api.dashamail.ru/"

    @staticmethod
    def configure(api_key):
        Configuration.api_key = api_key
