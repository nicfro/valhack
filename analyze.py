from api.face_api import FaceApi
from api.computer_vision_api import ComputerVisionApi
import pickle
import time


class Analyze:

    def __init__(self):
        self.faceApi = FaceApi()
        self.cvisionApi = ComputerVisionApi()

    def analyze_image(self, image_url):
        face_info = self.faceApi.run_api(image_url)
        cvision_info = self.cvisionApi.run_api(image_url)

        return face_info, cvision_info

    def main(self):
        data = pickle.load(open("data/ourInstagram.p", "rb"))
        counter = 0
        for key in data.keys():
            counter += 1
            info_list = data[key]
            print("User {}".format(counter))
            for info in info_list:
                url = info[3]
                face_info, cvision_info = self.analyze_image(url)

                info.append(face_info)
                info.append(cvision_info)
                time.sleep(3)

        pickle.dump(data, open("data/ourInstagram2.p", "wb"))


ana = Analyze()
ana.main()
