# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 2018/11/13

@author: shimakaze-git
'''
import cv2
import numpy as np
import configparser


class FaceExtraction:
    """ 顔画像抽出クラス """

    inifile = configparser.ConfigParser()
    inifile.read('../config.ini')

    # 入力画像ディレクトリのパス。最後はスラッシュで終わる必要あり。
    in_dir = inifile.get('extraction', 'in')
    # 出力先ディレクトリのパス。最後はスラッシュで終わる必要あり。
    out_dir = inifile.get('extraction', 'out')
    # カスケードファイルのパス。
    cascade_file = inifile.get('extraction', 'cascade')

    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier(self.cascade_file)

    def save_image(self, file):
        """ 顔部分を抽出して画像にして保存 """

        # grayscale化
        img = cv2.imread(self.in_dir + '/faces/' + file, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 顔部分抽出
        face = self.detect(gray)

        if len(face) is not 0:
            for rect in face:
                x = rect
                cv2.rectangle(
                    gray,
                    tuple(rect[0:2]),
                    tuple(rect[0:2]+rect[2:4]),
                    (0, 0,255),
                    thickness=2
                )

            # 画像のリサイズ
            resized_image = self.resize(gray)

            # grayscale化して顔部分の保存
            save_path = self.out_dir + '/gray_faces/' + 'gray_' + file +'.jpg'
            cv2.imwrite(save_path, gray)

    def detect(self, img):
        """ 顔部分の検出 """
        face = self.faceCascade.detectMultiScale(img, 1.1, 3)
        # face = self.faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
        
        return face

    def resize(self, img):
        """ 画像を128x128もリサイズ """

        # 128x128ピクセルにリサイズ
        image_resized = cv2.resize(img, (128, 128))

        return image_resized


if __name__ == '__main__':

    file = ""
    obj = FaceExtraction()
    obj.save_image(file)

# http://peaceandhilightandpython.hatenablog.com/entry/2016/02/18/194303
# https://qiita.com/syoyo/items/5277906d29b2dd49e3a2#%E5%AD%A6%E7%BF%92%E3%81%97%E3%81%9F%E3%81%84