import csv
import os

dict_feature1 = {}
dict_feature2 = {}
dict_abnormal = {}
f1 = open("features/Ratio_cart_user.csv")
userdata = csv.reader(f1)
userdata.next()
for row in userdata:
    dict_feature1[row[0]] = float(row[1])
f1.close()

f2 = open("features/Ratio_cart_item.csv")
itemdata = csv.reader(f2)
itemdata.next()
for row in itemdata:
    dict_feature2[row[0]] = float(row[1])
f2.close()

f3 = open("data/abnormaldata/abnormal_user.csv")
abnormaldata = csv.reader(f3)
abnormaldata.next()
for row in abnormaldata:
    dict_abnormal[row[0]] = True
f3.close()

def GetData(csvpath):
    dict_cart = {}
    dict_buy = {}
    f = open(csvpath)
    datedata = csv.reader(f)
    datedata.next()
    for row in datedata:
        user_id = row[0]
        item_id = row[1]
        b_type = row[2]
        if b_type == '3':
            dict_cart[(user_id, item_id)] = True
        if b_type == '4':
            dict_buy[(user_id, item_id)] = True
    f.close()

    dict_data = {}
    for key in dict_cart:
        if dict_buy.has_key(key):
            continue
        user_id, item_id = key
        if not dict_feature1.has_key(user_id):
            continue
        if not dict_feature2.has_key(item_id):
            continue
        if dict_abnormal.has_key(user_id):
            continue
        dict_data[key] = [dict_feature1[user_id],dict_feature2[item_id]]
    return dict_data

def GetLabel(csvpath):
    dict_buy = {}
    f = open(csvpath)
    datedata = csv.reader(f)
    datedata.next()
    for row in datedata:
        user_id = row[0]
        item_id = row[1]
        b_type = row[2]
        if b_type == '4':
            dict_buy[(user_id, item_id)] = True
    f.close()
    return dict_buy

def ProduceTrainset():
    w_f1 = open("data/traindata/trainset_p.csv", 'wb')
    write1 = csv.writer(w_f1)
    write1.writerow(["user_id", "item_id", "user_ratio", "item_ratio"])


    w_f2 = open("data/traindata/trainset_n.csv", 'wb')
    write2 = csv.writer(w_f2)
    write2.writerow(["user_id", "item_id", "user_ratio", "item_ratio"])


    datecsvlist = os.listdir("data/datedata/")
    datecsvlist.sort()
    for i in range(28):
        print 'now process ' + str((i + 1) * 2) + ' datecsv'
        csv_1 = datecsvlist[i]
        csv_2 = datecsvlist[i + 1]
        date_1 = csv_1.split('.')[0]
        date_2 = csv_2.split('.')[0]
        if date_1 == '2014-12-12' or date_2 == '2014-12-12':
            continue
        csvpath_1 = "data/datedata/" + csv_1
        csvpath_2 = "data/datedata/" + csv_2
        dict_data = GetData(csvpath_1)
        dict_buy = GetLabel(csvpath_2)
        for key in dict_data:
            user_id, item_id = key
            if dict_buy.has_key(key):
                write1.writerow([user_id,item_id,dict_data[key][0],dict_data[key][1]])
            else:
                write2.writerow([user_id, item_id, dict_data[key][0], dict_data[key][1]])
    w_f1.close()
    w_f2.close()


