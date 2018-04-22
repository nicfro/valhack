from scipy.spatial.distance import pdist, squareform
import pickle
import numpy as np

# data = pickle.load(open("data/formatted_data.p", "rb"))
data = np.array(pickle.load(open("data/formatted_data2.p", "rb")))

result = squareform(pdist(data[:,2:], 'euclidean'))

closest = np.argsort(result[0][1:])[:40]

aaa = data[closest]

embed = pickle.load(open("data/userStoreOutWordEmbed2.p", "rb"))

usernames = [name for name in embed.keys()]

#'United Kingdom', 'France', 'Singapore', 'New York', 'Japan', 'Amsterdam'
locations = {}
printer = {}
for post in data[closest]:
    id = int(post[0]) - 1
    post_idx = int(post[1]) - 1
    picked = embed[usernames[id]][post_idx]
    name = picked[1]
    if len(name.split(',')) > 1:
        name = name.split(',')[0].strip()
    locations[name] = locations.get(name, 0) + 1

    value = printer.get(name, [])
    value.append(picked[3])
    printer[name] = value

for key, value, picture in zip(locations.keys(), locations.values(), printer.values()):
    if value > 1 and key != 'no place':
        print("{}: {}".format(key, value))
        print("Pictures: {}".format(picture))
