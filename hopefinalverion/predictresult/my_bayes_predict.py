import csv
import preparedata.load_data as ld
x,y = ld.GetBayesTrainset(1000,1000)
needtest_key, needtest_data = ld.GetBayesNeedtest()

PY_init = 0.5
PN_init = 0.5
def PT(tag,feature_i,feature):
    cnt = 0
    if tag == 1:
        for i in range(1000):
            num1 = float(x[i][feature_i])
            num2 = float(feature)
            num = num1 - num2
            if num < 0.01 and num > -0.01:
                cnt += 1
    if tag == -1:
        for i in range(1000):
            num1 = float(x[i+1000][feature_i])
            num2 = float(feature)
            num = num1 - num2
            if num < 0.01 and num > -0.01:
                cnt += 1
    result = 1.0 * cnt / 1000
    return result
def NaiveBayes(eachfeature):
    PY = PY_init
    PN = PN_init
    for i in range(2):
        PY *= 1.0 * PT(1,i,eachfeature[i])
        PN *= 1.0 * PT(-1,i,eachfeature[i])
    print str(PY) + " " + str(PN)
    if PY == 0 and PN == 0:
        P = 0.5
        return P
    else:
        P = PY / (PY + PN)
        return P

def PredictByMyBayes():
    r_f = open("result/my_bayes_result.csv", "wb")
    write = csv.writer(r_f)
    write.writerow(["user_id", "item_id"])
    for i in range(len(needtest_data)):
        print "now predict the " + str(i+1) + "th user-item"
        P = NaiveBayes(needtest_data[i])
        print P
        if P > 0.5:
            write.writerow([needtest_key[i][0], needtest_key[i][1]])
    r_f.close()
