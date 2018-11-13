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
    pass