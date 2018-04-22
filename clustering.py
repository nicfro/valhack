from scipy.spatial.distance import pdist, squareform
import pickle

data = pickle.load(open("data/formatted_data.p", "rb"))

result = squareform(pdist(data, 'euclidean'))

print("hello")