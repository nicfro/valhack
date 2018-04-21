class BaseApi:

    def __init__(self, api_key):
        self.api_key = api_key
        self.content_type = "application/json"

    def run_api(self, image_url):
        raise NotImplementedError("Not implemented")