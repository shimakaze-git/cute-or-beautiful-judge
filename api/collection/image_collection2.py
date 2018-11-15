# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 2018/11/12

@author: shimakaze-git
'''
import requests
import re
import os
from PIL import Image as resizer

APIKEY = ""
ENGINE = ""
API_URL = "https://www.googleapis.com/customsearch/v1?key={APIKEY} &cx={ENGINE} &q=%s &searchType=image &start=%s".format(APIKEY=APIKEY, ENGINE=ENGINE)


def main():
    
    girls_words = []
    for word in girls_words:
        print(word)
        # getImageFromCustomAPI(1, 92, word, "YES-" + word + "_")

    # resizeImages("images", "target_")


if __name__ == '__main__':
    main()
