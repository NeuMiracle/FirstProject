#-*-coding:utf-8-*-
import os
import csv

#split data by user
user_dictionary = {}



def writeByUser(user_id,words):
    file_name = "data/userdata/" + user_id + ".csv"
    if not user_dictionary.has_key(user_id):
        user_dictionary[user_id] = True
        f = open(file_name,'a')
        write = csv.writer(f)
        write.writerow(['date','item_id','behavior_type','user_geohash','item_category','hour'])
        write.writerow(words)
        f.close()
    else:
        f = open(file_name,'a')
        write = csv.writer(f)
        write.writerow(words)
        f.close()


def splitByUser():
    os.mkdir('data/userdata')
    datecsvlist = os.listdir("data/datedata/")
    datecsvlist.sort()
    for eachcsv in datecsvlist:
        f = open("data/datedata/" + eachcsv)
        rows = csv.reader(f)
        rows.next()
        for row in rows:
            user_id = row[0]
            words = [eachcsv.split('.')[0]]
            words.extend(row[1:])
            writeByUser(user_id,words)
