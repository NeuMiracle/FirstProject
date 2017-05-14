import csv

def LoadAbnormal():
    abnormal = {}
    f = open("data/abnormaldata/abnormal_user.csv")
    abnormaldata = csv.reader(f)
    abnormaldata.next()
    for row in abnormaldata:
        abnormal[row[0]] = True
    return abnormal

def GetCartButNotBuy(datecsvpath):
    dict_cart = {}
    dict_buy = {}
    dict_result = {}
    f = open(datecsvpath)
    datedata = csv.reader(f)
    datedata.next()
    for row in datedata:
        user_id = row[0]
        item_id = row[1]
        b_type = row[2]
        hour = row[5]
        if b_type == '3':
            dict_cart[(user_id, item_id)] = hour
        if b_type == '4':
            dict_buy[(user_id, item_id)] = hour
    f.close()
    for key in dict_cart:
        if dict_buy.has_key(key):
            continue
        else:
            dict_result[key] = dict_cart[key]
    return dict_result

def GetTrainset(p_num,n_num):
    x = []
    y = []
    f1 = open("data/traindata/trainset_p.csv")
    trainset_p = csv.reader(f1)
    trainset_p.next()
    p_count = 0
    for row in trainset_p:
        p_count += 1
        if p_count > p_num:
            break
        x_i = [float(row[2]),float(row[3])]
        x.append(x_i)
        y.append(1)
    f1.close()

    f2 = open("data/traindata/trainset_n.csv")
    trainset_n = csv.reader(f2)
    trainset_n.next()
    n_count = 0
    for row in trainset_n:
        n_count += 1
        if n_count > n_num:
            break
        x_i = [float(row[2]), float(row[3])]
        x.append(x_i)
        y.append(-1)
    f2.close()
    return x,y

def GetNeedtest():
    needtest_key = []
    needtest_data = []
    f = open("data/needtestdata/needtest.csv")
    needtest = csv.reader(f)
    needtest.next()
    for row in needtest:
        key = [row[0],row[1]]
        data = [float(row[2]),float(row[3])]
        needtest_key.append(key)
        needtest_data.append(data)
    return needtest_key,needtest_data

