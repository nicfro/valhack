import pickle
import json
from sklearn.decomposition import PCA
import numpy as np

userid = list(range(1, 200))
pca = PCA(n_components=1)

data = pickle.load(open("data/userStoreOutWordEmbed2.p", "rb"))

formatted_data = []
counter = 0
for index, key in enumerate(data.keys()):
    counter += 1
    info_list = data[key]

    cur_list = []
    cur_list.append(userid[index]) #user id
    age = -1
    gender = 0
    all_posts_tags = []
    all_posts_emotions = []
    for info in info_list:
        face_info = json.loads(info[4])
        cvision_info = json.loads(info[5])

        if len(info) >= 7:
            age = info[6]
            gender = info[7]

        tags = np.array(cvision_info['description']['tags'])
        [all_posts_tags.append(tag) for tag in tags]
        emotions = []
        for face in face_info:
            emotions.append(list(face_info[0]['faceAttributes']['emotion'].values()))

        if len(emotions) > 0:
            all_posts_emotions.append(emotions[0])
        else:
            all_posts_emotions.append([0 for _ in range(8)])

    mean_tags = np.mean(np.array(all_posts_tags), axis=0)
    mean_emotions = np.mean(np.array(all_posts_emotions), axis=0)

    [cur_list.append(value) for value in mean_tags]
    [cur_list.append(value) for value in mean_emotions]
    formatted_data.append(cur_list)

data = pickle.load(open("data/instagramOutWordEmbed2.p", "rb"))

for index, key in enumerate(data.keys()):
    info_list = data[key]

    cur_list = []
    cur_list.append(userid[counter]) #user id
    age = -1
    gender = 0
    all_posts_tags = []
    all_posts_emotions = []
    for info in info_list:
        face_info = json.loads(info[4])
        cvision_info = json.loads(info[5])

        if len(info) >= 7:
            age = info[6]
            gender = info[7]

        tags = np.array(cvision_info['description']['tags'])
        [all_posts_tags.append(tag) for tag in tags]
        emotions = []
        for face in face_info:
            emotions.append(list(face_info[0]['faceAttributes']['emotion'].values()))

        if len(emotions) > 0:
            all_posts_emotions.append(emotions[0])
        else:
            all_posts_emotions.append([0 for _ in range(8)])

    mean_tags = np.mean(np.array(all_posts_tags), axis=0)
    mean_emotions = np.mean(np.array(all_posts_emotions), axis=0)

    [cur_list.append(value) for value in mean_tags]
    [cur_list.append(value) for value in mean_emotions]
    formatted_data.append(cur_list)
    counter += 1


pickle.dump(formatted_data, open("data/formatted_data2.p", "wb"))
