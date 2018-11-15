# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 2018/11/13

@author: shimakaze-git
'''
from sklearn.cluster import KMeans

K = 2


class KMeansClustering:

    def __init__(self, cluster=None):
        """ """
        if cluster is None:
            self.k_means = KMeans(n_clusters=K)
        else:
            self.k_means = KMeans(n_clusters=cluster)

    def clustering(self, reduced_features):
        """ 実際にクラスタリングを行う """

        k_means = self.k_means.fit(reduced_features)
        return k_means.predict(reduced_features)