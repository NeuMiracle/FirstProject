import os
import csv


dict_item = {}
datecsvlist = os.listdir("data/datedata/")
datecsvlist.sort()
count = 0
for eachcsv in datecsvlist:
    count += 1
    print "now process the " + str(count) + "th csv"
    date = eachcsv.split('.')[0]
    if date == '2014-12-12' or date == '2014-12-17':
        continue
    f = open("data/datedata/" + eachcsv)
    rows = csv.reader(f)
    rows.next()
    for row in rows:
        item_id = row[1]
        b_type = row[2]
        int_btype = int(b_type)
        if not dict_item.has_key(item_id):
            if b_type == '1':
                dict_item[item_id] = [1, 0, 0, 0]
            if b_type == '2':
                dict_item[item_id] = [0, 1, 0, 0]
            if b_type == '3':
                dict_item[item_id] = [0, 0, 1, 0]
            if b_type == '4':
                dict_item[item_id] = [0, 0, 0, 1]
        else:
            dict_item[item_id][int_btype - 1] += 1
    f.close()

def CollectRatio_click():
    dict_clickbuyratio = {}
    for key in dict_item:
        if dict_item[key][0] > 0:
            ratio = 1.0 * dict_item[key][3] / dict_item[key][0]
            if ratio > 1.0:
                dict_clickbuyratio[key] = 1.0
            else:
                dict_clickbuyratio[key] = ratio
    w_f = open("features/Ratio_click_item.csv", 'wb')
    write = csv.writer(w_f)
    write.writerow(["item_id", "click_to_buy"])
    for key in dict_clickbuyratio:
        write.writerow([key,dict_clickbuyratio[key]])
    w_f.close()
    print "CollectRatio_click is ok"


def CollectRatio_look():
    dict_lookbuyratio = {}
    for key in dict_item:
        if dict_item[key][1] > 0:
            ratio = 1.0 * dict_item[key][3] / dict_item[key][1]
            if ratio > 1.0:
                dict_lookbuyratio[key] = 1.0
            else:
                dict_lookbuyratio[key] = ratio
    w_f = open("features/Ratio_look_item.csv", 'wb')
    write = csv.writer(w_f)
    write.writerow(["item_id", "look_to_buy"])
    for key in dict_lookbuyratio:
        write.writerow([key, dict_lookbuyratio[key]])
    w_f.close()
    print "CollectRatio_look is ok"

def CollectRatio_cart():
    dict_cartbuyratio = {}
    for key in dict_item:
        if dict_item[key][2] > 0:
            ratio = 1.0 * dict_item[key][3] / dict_item[key][2]
            if ratio > 1.0:
                dict_cartbuyratio[key] = 1.0
            else:
                dict_cartbuyratio[key] = ratio
    w_f = open("features/Ratio_cart_item.csv", 'wb')
    write = csv.writer(w_f)
    write.writerow(["item_id", "cart_to_buy"])
    for key in dict_cartbuyratio:
        write.writerow([key, dict_cartbuyratio[key]])
    w_f.close()
    print "CollectRatio_cart is ok"