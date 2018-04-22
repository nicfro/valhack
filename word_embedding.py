import gensim
import pickle
import json
from scipy import stats
import numpy as np


class WordEmbed:

    def __init__(self):
        self.model = gensim.models.KeyedVectors.load_word2vec_format('model.bin', binary=True)

    def embed(self, word):
        try:
            return self.model[word]
        except KeyError:
            return None

    def main(self):
        data = pickle.load(open("data/userStoreOut2.p", "rb"))

        for key in data.keys():
            info_list = data[key]

            ages = []
            genders = []
            age = -1
            gender = 0
            for info in info_list:
                face_info = json.loads(info[4])

                if len(face_info) > 0:
                    for face in face_info:
                        ages.append(face['faceAttributes']['age'])
                        if face['faceAttributes']['gender'] == 'female':
                            genders.append(1)
                        else:
                            genders.append(0)

                if len(ages) > 0:
                    age = stats.mode(ages)[0][0]
                if len(genders) > 0:
                    gender = stats.mode(genders)[0][0]

            for info in info_list:
                face_info = json.loads(info[4])
                cvision_info = json.loads(info[5])

                tags = []
                for tag in cvision_info['description']['tags']:
                    result = self.embed(tag)
                    if result is not None:
                        tags.append(list(result.astype('float64')))

                cvision_info['description']['tags'] = tags

                if len(face_info) > 0:
                    for face in face_info:
                        ages.append(face['faceAttributes']['age'])
                        if face['faceAttributes']['gender'] == 'female':
                            genders.append(1)
                        else:
                            genders.append(0)

                info[4] = json.dumps(face_info)
                info[5] = json.dumps(cvision_info)
                info.append(age)
                info.append(gender)

        pickle.dump(data, open("data/userStoreOutWordEmbed2.p", "wb"))

WordEmbed().main()
