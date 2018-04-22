from scipy.spatial.distance import pdist, squareform
from collections import Counter
import pickle
import numpy as np
from operator import itemgetter

data = np.array(pickle.load(open("data/formatted_data2.p", "rb")))

result = squareform(pdist(data[:,1:], 'euclidean'))

np.fill_diagonal(result, 9999)

closest = np.argsort(result[77])[:5]

aaa = data[closest]

embed = pickle.load(open("data/userStoreOutWordEmbed2.p", "rb"))
embed2 = pickle.load(open("data/instagramOutWordEmbed2.p", "rb"))

usernames = [name for name in embed.keys()] + [name for name in embed2.keys()]

#'United Kingdom', 'France', 'Singapore', 'New York', 'Japan', 'Amsterdam'
most_locations = {}
most_liked_posts = []
user_location = []
for user in data[closest]:
    id = int(user[0]) - 1
    picked = None

    if id < 76:
        picked = embed[usernames[id]]
    else:
        picked = embed2[usernames[id]]

    locations = Counter([post[1] for post in picked])
    checked = False
    for _, name, value in zip(range(min(len(locations), 3)), locations.keys(), locations.values()):
        if name != 'no place' and value > 1:
            most_locations[name] = most_locations.get(name, 0) + value
            if not checked:
                user_location.append(name)
                checked = True

    for post in picked:
        if post[1] in most_locations:
            post[2] = int(post[2])
            most_liked_posts.append(post)

most_liked_posts = sorted(most_liked_posts, key=itemgetter(2), reverse=True)

for i in range(len(most_liked_posts[0:10])):
    print("Photo {}:".format(most_liked_posts[i][3]))

print("\nLocations ranked from closest user:")
[print(ll) for ll in user_location]