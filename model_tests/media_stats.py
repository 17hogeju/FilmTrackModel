import json

import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from kmodes.kmodes import KModes
from itertools import count



data = pd.read_json('../data/media.json')
data = data.explode('genres')
data = data.explode('directors')
data = data.explode('writers')

# temp = data.loc[data['tconst']=='tt0034583']

# # Create a dictionary of values for genres
# genres = set()
# for row in data.genres:
#     for genre in row:
#         genres.add(genre)
# c = count()
# genre_dict = {genre: next(c) for genre in genres}
# print(genre_dict)
# # print(genre_dict['Western'])

# # data.genres = x for x in data.genres
# # for row in data.genres:
# #     row = [genre_dict[g] for g in row]

# data.loc[:,'genres'] = genre_dict[x] for x in data.loc[:,genres]
# # for idx in data.loc[]:
# #     data.genres[idx] = [genre_dict[x] for x in data.genres[idx]]
# #     print(data.genres[idx])
# #     break
# #     # data[index]['genres'] = [genre_dict[x] for x in data[index]['genres']]


# # df.index = df['tconst']
# # print(type(df))
# # df.groupby('genres')['primaryTitle'].count()
# # print(df.head())
# # Only Murders: tt12851524: 461
# # Bullet Train: tt12593682: 445
# # The Princess Bride: tt0093779: 19

# # print(df[df.tconst.str.startswith('tt0093779')]['genres'])

# # # Elbow curve to find optimal K
# # cost = []
# K = [461, 445, 19] # Leaders are first 3 indeces of data
# # for i in K:

# # for num_clusters in list(K):
# #     kmode = KModes(n_clusters=num_clusters, init = "random", n_init = 5, verbose=1)
# #     kmode.fit_predict(data)
# #     cost.append(kmode.cost_)
    
# # plt.plot(K, cost, 'bx-')
# # plt.xlabel('No. of clusters')
# # plt.ylabel('Cost')
# # plt.title('Elbow Method For Optimal k')
# # plt.show()

# test = data.loc[:, 'genres']
# test = np.array(data).reshape(-1,1)
# print(data.shape)
# print(data.columns)

# # # Elbow curve to find optimal K
cost = []
K = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
for num_clusters in K:
    print(num_clusters)
    kmode = KModes(n_clusters=num_clusters, init = "random", n_init = 5, verbose=1)
    
    kmode.fit_predict(data)
    cost.append(kmode.cost_)
    
plt.plot(K, cost, 'bx-')
plt.xlabel('No. of clusters')
plt.ylabel('Cost')
plt.title('Elbow Method For Optimal k')
plt.show()

