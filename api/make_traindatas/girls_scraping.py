# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 2018/11/12

@author: shimakaze-git
'''
import requests
import time
from bs4 import BeautifulSoup


BASE_URL = "https://rank1-media.com/I0000207"


class GirlsScraping:
    
    def __init__(self):
        self.base_url = BASE_URL
    
    def scraping(self):
        """ scraping """
        self.rank1_scray()

    def rank1_scray(self):
        """ """
        name_list = []
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
                
                # divタグでclassがtitleのものを抽出
                if part.find("div", 'images_title') is not None:
                    title = part.find("div", 'images_title')
                    text_name = title.p.text
    
                    # 名前とランキングの抽出
                    rank, name = self.serialize(text_name)
                    girl_info = {"rank": rank, "name": name}
                    # name_list.append(name)
                    name_list.append(girl_info)

            # アクセス一行待機
            time.sleep(1)




        # print(name_list)
        for girl_info in name_list:
            print(girl_info['name']+",none,"+girl_info['rank'])

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

    def image_scray(self):
        pass

if __name__ == '__main__':
    girls = GirlsScraping()
    girls.scraping()