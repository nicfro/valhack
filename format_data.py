import pickle
import json
from sklearn.decomposition import PCA
import numpy as np

userid = list(range(1, 10))
pca = PCA(n_components=1)

data = pickle.load(open("data/userStoreOutWordEmbed.p", "rb"))

formatted_data = []
for index, key in enumerate(data.keys()):
    info_list = data[key]

    for info in info_list:
        cur_list = []
        face_info = json.loads(info[4])
        cvision_info = json.loads(info[5])

        cur_list.append(userid[index])
        if len(info) >= 7:
            cur_list.append(info[6])
            cur_list.append(info[7])
        else:
            cur_list.append(-1)
            cur_list.append(0)

        tags = np.array(cvision_info['description']['tags'])
        if len(tags) > 0:
            tags = tags.transpose()
            pca.fit(tags)
            transformed = pca.transform(tags)
            [cur_list.append(value[0]) for value in transformed]
        else:
            [cur_list.append(0) for _ in range(200)]
        emotions = []
        for face in face_info:
            emotions.append(list(face_info[0]['faceAttributes']['emotion'].values()))

        if len(emotions) > 0:
            emotions = np.array(emotions).transpose()
            pca.fit(emotions)
            transformed = pca.transform(emotions)
            [cur_list.append(value[0]) for value in transformed]
        else:
            [cur_list.append(0) for _ in range(8)]

        formatted_data.append(cur_list)

pickle.dump(formatted_data, open("data/formatted_data.p", "wb"))
