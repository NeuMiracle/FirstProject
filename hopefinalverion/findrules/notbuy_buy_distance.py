# -*-coding:utf-8-*-
import cPickle
import os
import csv
import matplotlib.pyplot as plt


#should predict the result with the yesterday's data
def click_buy_distance():
    datecsvlist = os.listdir("data/datedata/")
    datecsvlist.sort()
    data_x = [1,2,3,4,5,6,7]
    data_y = []
    for j in range(7):
        num = 0;
        for i in range(28-j):
            print 'now process ' + str((i + 1)) + ' datecsv'
            csv_1 = datecsvlist[i]
            csv_2 = datecsvlist[i + j + 1]
            date_1 = csv_1.split('.')[0]
            date_2 = csv_2.split('.')[0]
            if date_1 == '2014-12-12' or date_2 == '2014-12-12':
                continue
            file1 = open("data/datedata/" + csv_1)
            datedata = csv.reader(file1)
            datedata.next()
            dict_pre = {}
            for row in datedata:
                user_id = row[0]
                item_id = row[1]
                b_type = row[2]
                if b_type == '1':
                    key = (user_id,item_id)
                    dict_pre[key] = b_type
            file2 = open("data/datedata/" + csv_2)
            datedata = csv.reader(file2)
            datedata.next()
            for row in datedata:
                user_id = row[0]
                item_id = row[1]
                b_type = row[2]
                if b_type == '4':
                    key = (user_id, item_id)
                    if dict_pre.has_key(key):
                        num += 1
            file1.close()
            file2.close()
        print num
        data_y.append(num)
    plt.xlabel('distance')
    plt.ylabel('count')
    plt.title('click_buy_distance')
    plt.plot(data_x, data_y)
    plt.savefig('picture/click_buy_distance.png')
    # plt.show()
    plt.close()

    print 'click_buy_distance is ok'

def look_buy_distance():
    datecsvlist = os.listdir("data/datedata/")
    datecsvlist.sort()
    data_x = [1, 2, 3, 4, 5, 6, 7]
    data_y = []
    for j in range(7):
        num = 0;
        for i in range(28 - j):
            print 'now process ' + str((i + 1)) + ' datecsv'
            csv_1 = datecsvlist[i]
            csv_2 = datecsvlist[i + j + 1]
            date_1 = csv_1.split('.')[0]
            date_2 = csv_2.split('.')[0]
            if date_1 == '2014-12-12' or date_2 == '2014-12-12':
                continue
            file1 = open("data/datedata/" + csv_1)
            datedata = csv.reader(file1)
            datedata.next()
            dict_pre = {}
            for row in datedata:
                user_id = row[0]
                item_id = row[1]
                b_type = row[2]
                if b_type == '2':
                    key = (user_id, item_id)
                    dict_pre[key] = b_type
            file2 = open("data/datedata/" + csv_2)
            datedata = csv.reader(file2)
            datedata.next()
            for row in datedata:
                user_id = row[0]
                item_id = row[1]
                b_type = row[2]
                if b_type == '4':
                    key = (user_id, item_id)
                    if dict_pre.has_key(key):
                        num += 1
            file1.close()
            file2.close()
        print num
        data_y.append(num)
    plt.xlabel('distance')
    plt.ylabel('count')
    plt.title('look_buy_distance')
    plt.plot(data_x, data_y)
    plt.savefig('picture/look_buy_distance.png')
    # plt.show()
    plt.close()

    print 'look_buy_distance is ok'

def cart_buy_distance():
    datecsvlist = os.listdir("data/datedata/")
    datecsvlist.sort()
    data_x = [1, 2, 3, 4, 5, 6, 7]
    data_y = []
    for j in range(7):
        num = 0;
        for i in range(28 - j):
            print 'now process ' + str((i + 1)) + ' datecsv'
            csv_1 = datecsvlist[i]
            csv_2 = datecsvlist[i + j + 1]
            date_1 = csv_1.split('.')[0]
            date_2 = csv_2.split('.')[0]
            if date_1 == '2014-12-12' or date_2 == '2014-12-12':
                continue
            file1 = open("data/datedata/" + csv_1)
            datedata = csv.reader(file1)
            datedata.next()
            dict_pre = {}
            for row in datedata:
                user_id = row[0]
                item_id = row[1]
                b_type = row[2]
                if b_type == '3':
                    key = (user_id, item_id)
                    dict_pre[key] = b_type
            file2 = open("data/datedata/" + csv_2)
            datedata = csv.reader(file2)
            datedata.next()
            for row in datedata:
                user_id = row[0]
                item_id = row[1]
                b_type = row[2]
                if b_type == '4':
                    key = (user_id, item_id)
                    if dict_pre.has_key(key):
                        num += 1
            file1.close()
            file2.close()
        print num
        data_y.append(num)
    plt.xlabel('distance')
    plt.ylabel('count')
    plt.title('cart_buy_distance')
    plt.plot(data_x, data_y)
    plt.savefig('picture/cart_buy_distance.png')
    # plt.show()
    plt.close()

    print 'cart_buy_distance is ok'

click_buy_distance()
look_buy_distance()
cart_buy_distance()