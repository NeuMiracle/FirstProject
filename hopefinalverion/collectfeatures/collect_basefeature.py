import os
import csv

def CollectItemBasefeature():
    dict_item = {}
    datecsvlist = os.listdir("data/datedata/")
    datecsvlist.sort()
    count1 = 0
    for eachcsv in datecsvlist:
        count1 += 1
        print "now process the " + str(count1) + "th csv"
        date = eachcsv.split('.')[0]
        if date == '2014-12-12' or date == '2014-12-17':
            continue
        r_f = open("data/datedata/" + eachcsv)
        rows = csv.reader(r_f)
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
        r_f.close()
    w_f = open("features/Basefeature_item.csv", 'wb')
    write = csv.writer(w_f)
    write.writerow(["item_id", "click", "look", "cart", "buy"])
    for key in dict_item:
        write.writerow([key, dict_item[key][0], dict_item[key][1], dict_item[key][2], dict_item[key][3]])
    w_f.close()


def CollectUserBasefeature():
    dict_user = {}
    usercsvlist = os.listdir("data/userdata/")
    usercsvlist.sort()
    count = 0
    for eachcsv in usercsvlist:
        count += 1
        print "now process the " + str(count) + "th csv"
        user_id = eachcsv.split('.')[0]
        r_f = open("data/userdata/" + eachcsv)
        rows = csv.reader(r_f)
        rows.next()
        for row in rows:
            date = row[0]
            if date == '2014-12-12' or date == '2014-12-17':
                continue
            b_type = row[2]
            if not dict_user.has_key(user_id):
                if b_type == '1':
                    dict_user[user_id] = [1, 0, 0, 0]
                if b_type == '2':
                    dict_user[user_id] = [0, 1, 0, 0]
                if b_type == '3':
                    dict_user[user_id] = [0, 0, 1, 0]
                if b_type == '4':
                    dict_user[user_id] = [0, 0, 0, 1]
            else:
                if b_type == '1':
                    dict_user[user_id][0] += 1
                if b_type == '2':
                    dict_user[user_id][1] += 1
                if b_type == '3':
                    dict_user[user_id][2] += 1
                if b_type == '4':
                    dict_user[user_id][3] += 1
        r_f.close()
    w_f = open("features/Basefeature_user.csv", 'wb')
    write = csv.writer(w_f)
    write.writerow(["user_id", "click", "look", "cart", "buy"])
    for key in dict_user:
        write.writerow([key, dict_user[key][0], dict_user[key][1], dict_user[key][2], dict_user[key][3]])
    w_f.close()