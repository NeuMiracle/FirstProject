# _*_ coding: utf-8 _*_
import csv
import os
import matplotlib.pyplot as plt

#find that behavior count increase after 17:00
def BehaviorChangeByHour():
    x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    datecsvlist = os.listdir("data/hourdata/")
    datecsvlist.sort()
    for eachcsv in datecsvlist:
        click_count = 0
        look_count = 0
        cart_count = 0
        buy_count = 0
        file = open("data/hourdata/" + eachcsv)
        datedata = csv.reader(file)
        datedata.next()
        for row in datedata:
            b_type = row[2]
            if b_type == '1':
                click_count += 1
            if b_type == '2':
                look_count += 1
            if b_type == '3':
                cart_count += 1
            if b_type == '4':
                buy_count += 1
        hour = eachcsv.split(".")[0]
        x.append(hour)
        y1.append(click_count)
        y2.append(look_count)
        y3.append(cart_count)
        y4.append(buy_count)
        print hour
        print str(click_count) + " " + str(look_count) + " " + str(cart_count) + " " + str(buy_count)
        file.close()
    plt.xlabel('hour')
    plt.ylabel('count')
    plt.title('behavior changes by hour')
    plt.xticks(range(len(x)),x)
    plt.plot(range(len(x)), y1, label='click')
    plt.plot(range(len(x)), y2, label='look')
    plt.plot(range(len(x)), y3, label='cart')
    plt.plot(range(len(x)), y4, label='buy')
    plt.legend(loc='upper center')
    plt.savefig('picture/behavior_hour.png')
    plt.show()


