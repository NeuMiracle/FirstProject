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
    num1 = 0
    for data in traindate_p:
        num1 += 1
        x1.append(float(data[2]))
        y1.append(float(data[3]))
    num2 = 0
    for data in traindate_n:
        num2 += 1
        if num2 > num1:
            break
        x2.append(float(data[2]))
        y2.append(float(data[3]))
    plt.xlabel('feature1')
    plt.ylabel('feature2')
    plt.title('trainset distribution')
    plt.scatter(x1, y1, c='r', marker='o',label='buy')
    plt.scatter(x2, y2, c='g', marker='o', label='not buy')
    plt.legend()
    plt.savefig('picture/trainset_distribution.png')
    plt.show()
    f1.close()
    f2.close()