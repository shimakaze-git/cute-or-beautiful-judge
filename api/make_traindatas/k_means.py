# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 2018/11/13

@author: shimakaze-git
'''
from sklearn.cluster import KMeans

K = 2
# kmeans = KMeans(n_clusters=K).fit(reduced)
# pred_label = kmeans.predict(reduced)
# print(pred_label) # ==> [2 0 2 1 1 1 1 2 1 ...] 


# # クラスタリングした結果をプロット
# x = reduced[:, 0]
# y = reduced[:, 1]
# plt.scatter(x, y, c=pred_label)
# plt.colorbar()
# plt.show()


class KMeansClustering:

    def __init__(self):
        """ """
        self.k_means = KMeans(n_clusters=K)

    def clustering(self, reduced_features):
        """ 実際にクラスタリングを行う """

        k_means = self.k_means.fit(reduced_features)