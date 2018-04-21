from api.base_api import BaseApi
from requests import Request, Session
import json


class ComputerVisionApi(BaseApi):

    def __init__(self):
        BaseApi.__init__(self, 'd3dd50fbd7184714ac5d845c6d57ba26')

    def run_api(self, image_url):
        api_url = "https://westeurope.api.cognitive.microsoft.com/vision/v1.0/analyze?visualFeatures=ImageType,Faces,Categories,Adult,Color,Tags,Description&details=Celebrities,Landmarks&language=en"
        prepared = "{'url': '" + image_url + "'}"
        headers = {'Ocp-Apim-Subscription-Key': self.api_key,
                   'Content-Type': self.content_type,
                   'Host': 'westeurope.api.cognitive.microsoft.com',
                   'Content-Length': str(len(prepared))}

        s = Session()

        request = Request(method='POST',
                          url=api_url,
                          headers=headers)

        prepped = s.prepare_request(request)
        prepped.body = prepared

        response = s.send(prepped)

        if response.status_code == 200:
            information = json.loads(response.text)
            print(json.dumps(information, indent=4, sort_keys=True))
        else:
            print("Error")
            print(response)
            print(response.text)

# cvision = ComputerVisionApi()

# cvision.run_api("https://c-lj.gnst.jp/public/article/detail/a/00/00/a0000718/img/basic/a0000718_main.jpg")