#-*- coding:utf-8 -*-
import pandas as pd
import sys
import os
import csv

import pymysql
import base64
import requests


#Preprocessing
data = pd.read_csv('Electronics_sample.csv', encoding ='utf-8')
review = data.iloc[:,15:24] #review 항목
item1 = data.iloc[:,:15]
item2 = data.iloc[:, 25:] #Source URL 너무 커서 일단 뺌
item = pd.concat([item1, item2], axis=1) #item 항목

items = item.drop_duplicates() #중복을 제거한 item 항목(50개)
#items.info()
items.fillna("-1", inplace=True) #결측치 제거
#items.info()
items = items.values
#print(items.shape)
#print(items)

#AWS connection
host = "graduate-project.c9rpxmt946al.ap-northeast-2.rds.amazonaws.com"
port = 3306
username = "admin"
database = "graduatedb"
password = "hyrecproject16"

conn = pymysql.connect(host=host, port=port, db=database, user=username, passwd = password, use_unicode=True, charset ='utf8')
cursor = conn.cursor()

#item insert
#id asins	brand	categories	colors	dateAdded	dateUpdated	dimension	ean	imageURLs	keys	manufacturer	manufacturerNumber	name	primaryCategories	sourceURLs  upc	weight
for i in range(items.shape[0]):
    query = "INSERT INTO test_items VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    Img_URL = ""
    for c in items[i][9]:
        if c != ",":
            Img_URL += c
        else:
            break
    cursor.execute(query, (items[i][0], items[i][1], items[i][2], items[i][3], items[i][4], items[i][5], items[i][6], items[i][7], items[i][8], Img_URL, items[i][10], items[i][11], items[i][12], items[i][13], items[i][14], items[i][15], items[i][16]))
    conn.commit()

#cursor.execute(query)
#conn.commit()

