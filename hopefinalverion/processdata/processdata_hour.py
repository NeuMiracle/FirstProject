#-*-coding:utf-8-*-
import os
import csv

#split data by hour
hour_dictionary = {}

def writeByHour(hour,words):
    file_name = "data/hourdata/" + hour + ".csv"
    if not hour_dictionary.has_key(hour):
        hour_dictionary[hour] = True
        f = open(file_name,'a')
        write = csv.writer(f)
        write.writerow(['user_id','item_id','behavior_type','user_geohash','item_category','date'])
        write.writerow(words)
        f.close()
    else:
        f = open(file_name,'a')
        write = csv.writer(f)
        write.writerow(words)
        f.close()


def splitByHour():
    os.mkdir("data/hourdata")
    datecsvlist = os.listdir("data/userdata/")
    datecsvlist.sort()
    for eachcsv in datecsvlist:
        user_id = eachcsv.split('.')[0]
        f = open("data/userdata/" + eachcsv)
        rows = csv.reader(f)
        rows.next()
        for row in rows:
            hour = row[5]
            words = [user_id,row[1],row[2],row[3],row[4],row[0]]
            writeByHour(hour,words)
