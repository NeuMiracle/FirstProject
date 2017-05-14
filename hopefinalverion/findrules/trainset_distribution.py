import csv
import matplotlib.pyplot as plt

def TrainsetDistribution():
    f1 = open("data/traindata/trainset_p.csv")
    f2 = open("data/traindata/trainset_n.csv")
    traindate_p = csv.reader(f1)
    traindate_p.next()
    traindate_n = csv.reader(f2)
    traindate_n.next()
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    num = 5000
    list1 = []
    num1 = 0
    for data in traindate_p:
        list1.append([float(data[0]), float(data[1])])
        num1 += 1
        if num1 == num:
            break
    list1.sort(lambda x, y: cmp(x[0], y[0]))
    list2 = []
    num2 = 0
    for data in traindate_n:
        list2.append([float(data[0]), float(data[1])])
        num2 += 1
        if num2 == num:
            break
    list2.sort(lambda x, y: cmp(x[0], y[0]))

    for i in range(num):
        x1.append(list1[i][0])
        y1.append(list1[i][1])
        x2.append(list2[i][0])
        y2.append(list2[i][1])

    plt.xlabel('ratio')
    plt.ylabel('time')
    plt.title('trainset distribution')
    plt.scatter(x1, y1, c='r', marker='o',label='buy')
    plt.scatter(x2, y2, c='g', marker='o', label='not buy')
    # plt.plot(x1, y1, label='buy')
    # plt.plot(x2, y2, label='not buy')
    plt.legend()
    plt.savefig('picture/trainset_distribution.png')
    plt.show()
    f1.close()
    f2.close()