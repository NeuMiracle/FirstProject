import csv

def ProduceNeedtest():
    dict_user = {}
    dict_item = {}
    dict_abnormal = {}
    f1 = open("features/Basefeature_user.csv")
    userdata = csv.reader(f1)
    userdata.next()
    for row in userdata:
        dict_user[row[0]] = float(row[3])
    f1.close()

    f2 = open("features/Basefeature_item.csv")
    itemdata = csv.reader(f2)
    itemdata.next()
    for row in itemdata:
        dict_item[row[0]] = float(row[3])
    f2.close()

    f3 = open("data/abnormaldata/abnormal_user.csv")
    abnormaldata = csv.reader(f3)
    abnormaldata.next()
    for row in abnormaldata:
        dict_abnormal[row[0]] = True
    f3.close()

    dict_cart = {}
    dict_buy = {}
    f = open("data/datedata/2014-12-16.csv")
    datedata = csv.reader(f)
    datedata.next()
    for row in datedata:
        user_id = row[0]
        item_id = row[1]
        b_type = row[2]
        if b_type == '3':
            dict_cart[(user_id,item_id)] = True
        if b_type == '4':
            dict_buy[(user_id,item_id)] = True
    f.close()

    w_f = open("data/needtestdata/needtest.csv", 'wb')
    write = csv.writer(w_f)
    write.writerow(["user_id", "item_id", "feature1", "feature2"])
    for key in dict_cart:
        if dict_buy.has_key(key):
            continue
        user_id,item_id = key
        if not dict_user.has_key(user_id):
            continue
        if not dict_item.has_key(item_id):
            continue
        if dict_abnormal.has_key(user_id):
            continue
        write.writerow([user_id,item_id,dict_user[user_id],dict_item[item_id]])
    w_f.close()