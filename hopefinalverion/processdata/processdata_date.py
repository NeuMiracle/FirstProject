# -*-coding:utf-8-*-

import csv
import os

#split data by date
date_dictionary = {}

def writeByDate(date, words):
    file_name =  "data/datedata/" + date + ".csv"
    if not date_dictionary.has_key(date):
        date_dictionary[date] = True
        f = open(file_name, 'a')
        write = csv.writer(f)
        write.writerow(['user_id', 'item_id', 'behavior_type', 'user_geohash', 'item_category', 'hour'])
        write.writerow(words)
        f.close()
    else:
        f = open(file_name, 'a')
        write = csv.writer(f)
        write.writerow(words)
        f.close()

def splitByDate():
    os.mkdir('data/datedata')
    f = open("data/rawdata/dutir_tianchi_mobile_recommend_train_user_train.csv")
    rows = csv.reader(f)
    rows.next()
    for row in rows:
        date = row[-1].split(" ")[0]
        hour = row[-1].split(" ")[1]
        words = row[0:-1]
        words.append(hour)
        writeByDate(date, words)