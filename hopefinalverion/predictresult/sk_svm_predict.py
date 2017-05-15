from sklearn import svm
import preparedata.load_data as ld
import csv
import numpy as np

def PredictBySkSVM():
    original_x,original_y = ld.GetSvmTrainset(10000,10000)
    x = np.array(original_x)
    y = np.array(original_y)
    clf = svm.SVC()
    clf.fit(x, y)
    needtest_key,needtest_data = ld.GetSvmNeedtest()
    f = open("result/sk_svm_result.csv", "wb")
    write = csv.writer(f)
    write.writerow(["user_id", "item_id"])
    for i in range(len(needtest_key)):
        judge = clf.predict(needtest_data[i])
        if judge[0] == 1:
            write.writerow([needtest_key[i][0],needtest_key[i][1]])
    f.close()