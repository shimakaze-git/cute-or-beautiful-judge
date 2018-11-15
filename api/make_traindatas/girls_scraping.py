# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 2018/11/12

@author: shimakaze-git
'''
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup

BASE_SITE = "https://rank1-media.com"
BASE_URL = BASE_SITE + "/I0000207"


class GirlsScraping:
    
    def __init__(self):
        self.base_site = BASE_SITE
        self.base_url = BASE_URL
    
    def scraping(self):
        """ scraping """
        self.rank1_scray()

    def rank1_scray(self):
        """ """
        name_list = []
        c = 0
        for i in range(3):
            if i is not 0:
                url = self.base_url+"/&page="+str(i)
                request_object = requests.get(url)
            else:
                request_object = requests.get(self.base_url)

            soup = BeautifulSoup(
                request_object.content,
                "html.parser"
            )
    
            # 名前部分の抽出処理
            part_starts = soup.select('div.part_start')
            for part in part_starts:
                
                # print(part)
                # divタグでclassがtitleのものを抽出
                if part.find("div", 'images_title') is not None:
                    images_title = part.find("div", 'images_title')
                    text_name = images_title.p.text
    
                    # 名前とランキングの抽出
                    rank, name = self.serialize(text_name)
                    girl_info = {"rank": rank, "name": name}
                    # name_list.append(name)
                    name_list.append(girl_info)

                    # 画像の保存
                    img = part.find("img")
                    img_src = img['src']
                    
                    # id = "a_"+rank
                    # self.image_scray(img_src, id)

                # print("=-------------------------------------=")
            # アクセス一行待機
            # time.sleep(1)

        # girls_csv = "../girls.csv"
        # girls_info = pd.read_csv(girls_csv)
        # print(girls_info)
        print(name_list)

        to_csv_list = []
        for girl_info in name_list:
            name = girl_info['name']
            id = "a_"+str(int(girl_info['rank']))
            to_csv_list.append([name, "none", id])

        print(to_csv_list)

        df = pd.DataFrame(to_csv_list, columns=["name", "type", "id"])
        print(type(df))
        # print(type(girls_info))
        # girls_info.append(df)

        # print(girls_info)
        df.to_csv("../girls.csv")



    def serialize(self, text_name):
        """ 名前を正規化 """

        # ランキング抽出
        rank, name = self.slice_name(text_name)
        return rank, name

    def slice_name(self, text_name):
        """ 名前をスライスしてフルネームに変換 """
        
        rank = text_name[:text_name.find('位')]
        slice_name = text_name[text_name.find('位')+2:]
        name = slice_name[:-2]
        return rank, name

    def image_scray(self ,img_path, id):
        """ 画像のスクレイピング """
        url = self.base_site + "/" + img_path
        print(url)
        req = requests.get(url)
        img_dir = '../images/faces/'
        with open(str(img_dir)+str(id)+str('.jpg'),'wb') as file:
            # file.write(req.content)
            print(req.content)

    def to_csv(self):
        """ girls.csvの更新 """
        pass
        # # ラベル付けを行っていく
        # girls_csv = "../girls.csv"
        # girls_info = pd.read_csv(girls_csv)
        # # print(girls_info)
        # # print(type(girls_info))
        # # for girl_info in girls_info.iteritems():
        # for index, row in girls_info.iterrows():
    
            
        #     # data = data[data.column1 == 'hoge']
        #     # print(row.name == '新垣結衣')
        #     # print(row['name'] == '新垣結衣')
        #     print(index)
        #     print(row['name'])
        #     print("---------------------------")
            
        # # to_csv

if __name__ == '__main__':
    girls = GirlsScraping()
    girls.scraping()