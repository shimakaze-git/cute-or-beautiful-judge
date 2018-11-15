# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 2018/11/13

@author: shimakaze-git
'''
from PIL import Image
from skimage import data
import numpy as np
import os
import pandas as pd
# import matplotlib.pyplot as plt

from k_means import KMeansClustering
from decomposition import Decomposition
from girls_scraping import GirlsScraping


def make_traindatas():
    # 画像収集処理
    # girls = GirlsScraping()
    # girls.scraping()

    # リサイズしての顔抽出処理


    # GRAY_SCALE画像をndarray配列化
    features = np.array(
        [data.imread('../images/gray_faces/'+str(path)) for path in os.listdir('../images/gray_faces')]
    )
    # 3次元配列の画像データを2次元配列のデータに変換
    reduced_features = features.reshape(len(features), -1).astype(np.float64)

    # 次元削減処理 主成分分析(PCA)による次元削減処理
    decomposition_obj = Decomposition(n=2)
    reduced_features = decomposition_obj.transform(reduced_features)

    # クラスタリング処理
    cluster = 4
    k_mean = KMeansClustering(cluster)
    pred = k_mean.clustering(reduced_features)
    
    print(pred)

    # ラベル付けを行っていく
    girls_csv = "../girls.csv"
    girls_info = pd.read_csv(girls_csv)
    # print(girls_info)
    # print(type(girls_info))
    # for girl_info in girls_info.iteritems():
    for index, row in girls_info.iterrows():

        
        # data = data[data.column1 == 'hoge']
        # print(row.name == '新垣結衣')
        # print(row['name'] == '新垣結衣')
        print(index)
        print(row['name'])
        print("---------------------------")
        
    # to_csv


if __name__ == '__main__':
    make_traindatas()