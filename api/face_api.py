from api.base_api import BaseApi
from requests import Request, Session
import json


class FaceApi(BaseApi):

    def __init__(self):
        BaseApi.__init__(self, '26a910afbe77422b94eaef0eed6652a4')

    def run_api(self, image_url):
        api_url = "https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false&returnFaceAttributes=age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise"
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

# face = FaceApi()

# face.run_api("https://metrouk2.files.wordpress.com/2017/08/pri_48957260.jpg")