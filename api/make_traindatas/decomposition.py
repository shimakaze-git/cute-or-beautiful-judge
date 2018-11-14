# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 2018/11/13

@author: shimakaze-git
'''
from sklearn.decomposition import PCA


# features
class Decomposition:
    """ 次元削減を行う """

    def __init__(self):
        self.pca = PCA(n_components=2)

    # def print(test)

if __name__ == '__main__':
    from PIL import Image
    from skimage import data
    import numpy as np
    import os
    from sklearn.decomposition import PCA
    from sklearn.cluster import KMeans
    import matplotlib.pyplot as plt

    image = "../images/gray_faces/gray_4aa529273547b86d3521b358c1ad1e43.jpg"
    image = "gray_4aa529273547b86d3521b358c1ad1e43.jpg"
    as_arrayed_img = np.asarray(data.imread(f'../images/gray_faces/{image}'))
    # print(as_arrayed_img.shape)

    features = np.array([data.imread(f'../images/gray_faces/{path}') for path in os.listdir('../images/gray_faces')])
    features = features.reshape(len(features), -1).astype(np.float64)
    print(len(features))

    pca = PCA(n_components=2)
    pca.fit(features)
    reduced = pca.fit_transform(features)
    # print(reduced)
    # print(reduced.shape)
    # print(len(reduced))
    # reduced = features

    kmeans = KMeans(n_clusters=2).fit(reduced)
    pred_label = kmeans.predict(reduced)
    print(pred_label)
    print(reduced[0])
    print(reduced[1])
    print(reduced[2])
    print(reduced[4])
    print(reduced[5])

    # クラスタリングした結果をプロット
    x = reduced[:, 0]
    y = reduced[:, 1]
    plt.scatter(x, y, c=pred_label)
    plt.colorbar()
    plt.show()