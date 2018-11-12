# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 2018/11/12

@author: shimakaze-git

SVMを用いて学習を行う
'''
from sklearn.externals import joblib
from sklearn import svm


class LearnClass:
    """ 学習用クラス """

    def __init__(self, datas, lables):
        self.datas = datas
        self.lables = lables

    def svm_learn(self):
        """ SVMによる学習 """
        clf = svm.LinearSVC()
        clf.fit(self.datas, self.lables)
        return clf

    def output_pickle(self, clf, path):
        """ モデルをpickle化する """
        joblib.dump(clf, path)
        joblib.dump(clf, "pkls/beauty.pkl")
