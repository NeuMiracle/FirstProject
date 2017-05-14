import csv
import os

dict_user = {}
usercsvlist = os.listdir("data/userdata/")
usercsvlist.sort()
count = 0
for eachcsv in usercsvlist:
    count += 1
    print "now process the " + str(count) + "th csv"
    user_id = eachcsv.split('.')[0]
    dict_click = {}
    dict_look = {}
    dict_cart = {}
    dict_buy = {}
    f = open("data/userdata/" + eachcsv)
    rows = csv.reader(f)
    rows.next()
    for row in rows:
        date = row[0]
        if date == '2014-12-12' or date == '2014-12-17':
            continue
        item_id = row[1]
        b_type = row[2]
        if not dict_user.has_key(user_id):
            if b_type == '1':
                dict_user[user_id] = [1, 0, 0, 0, 0, 0, 0, 0]
                dict_click[item_id] = True
            if b_type == '2':
                dict_user[user_id] = [0, 1, 0, 0, 0, 0, 0, 0]
                dict_look[item_id] = True
            if b_type == '3':
                dict_user[user_id] = [0, 0, 1, 0, 0, 0, 0, 0]
                dict_cart[item_id] = True
            if b_type == '4':
                dict_user[user_id] = [0, 0, 0, 1, 0, 0, 0, 0]
                dict_buy[item_id] = True
        else:
            if b_type == '1':
                dict_user[user_id][0] += 1
                dict_click[item_id] = True
            if b_type == '2':
                dict_user[user_id][1] += 1
                dict_look[item_id] = True
            if b_type == '3':
                dict_user[user_id][2] += 1
                dict_cart[item_id] = True
            if b_type == '4':
                dict_user[user_id][3] += 1
                dict_buy[item_id] = True
    for key in dict_click:
        dict_user[user_id][4] += 1
    for key in dict_look:
        dict_user[user_id][5] += 1
    for key in dict_cart:
        dict_user[user_id][6] += 1
    for key in dict_buy:
        dict_user[user_id][7] += 1
    f.close()

def CollectMeanvalue_click():
    dict_clickmeanvalue = {}
    for key in dict_user:
        if dict_user[key][0] > 0:
            meanvalue = 1.0 * dict_user[key][0] / dict_user[key][4]
            dict_clickmeanvalue[key] = meanvalue
    w_f = open("features/Meanvalue_click_user.csv", 'wb')
    write = csv.writer(w_f)
    write.writerow(["user_id", "click_meanvalue"])
    for key in dict_clickmeanvalue:
        write.writerow([key,dict_clickmeanvalue[key]])
    w_f.close()
    print "CollectMeanvalue_click is ok"


def CollectMeanvalue_look():
    dict_lookmeanvalue = {}
    for key in dict_user:
        if dict_user[key][1] > 0:
            meanvalue = 1.0 * dict_user[key][1] / dict_user[key][5]
            dict_lookmeanvalue[key] = meanvalue
    w_f = open("features/Meanvalue_look_user.csv", 'wb')
    write = csv.writer(w_f)
    write.writerow(["user_id", "look_meanvalue"])
    for key in dict_lookmeanvalue:
        write.writerow([key, dict_lookmeanvalue[key]])
    w_f.close()
    print "CollectMeanvalue_look is ok"

def CollectMeanvalue_cart():
    dict_cartmeanvalue = {}
    for key in dict_user:
        if dict_user[key][2] > 0:
            meanvalue = 1.0 * dict_user[key][2] / dict_user[key][6]
            dict_cartmeanvalue[key] = meanvalue
    w_f = open("features/Meanvalue_cart_user.csv", 'wb')
    write = csv.writer(w_f)
    write.writerow(["user_id", "cart_meanvalue"])
    for key in dict_cartmeanvalue:
        write.writerow([key, dict_cartmeanvalue[key]])
    w_f.close()
    print "CollectMeanvalue_cart is ok"

def CollectMeanvalue_buy():
    dict_buymeanvalue = {}
    for key in dict_user:
        if dict_user[key][3] > 0:
            meanvalue = 1.0 * dict_user[key][3] / dict_user[key][7]
            dict_buymeanvalue[key] = meanvalue
    w_f = open("features/Meanvalue_buy_user.csv", 'wb')
    write = csv.writer(w_f)
    write.writerow(["user_id", "buy_meanvalue"])
    for key in dict_buymeanvalue:
        write.writerow([key, dict_buymeanvalue[key]])
    w_f.close()
    print "CollectMeanvalue_buy is ok"