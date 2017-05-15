# -*-coding:utf-8-*-
from numpy import *
import random
import csv
import preparedata.load_data as ld

def SelectJrand(i, m):
    j = i
    while (j == i):
        j = int(random.uniform(0, m))
    return j


def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if aj < L:
        aj = L
    return aj


def Smo(dataMatIn, classLabels, C, toler, maxIter):
    dataMatrix = mat(dataMatIn);
    labelMat = mat(classLabels).transpose()
    b = 0;
    m, n = shape(dataMatrix)
    alphas = mat(zeros((m, 1)))
    iter = 0
    while (iter < maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float(multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[i, :].T)) + b
            Ei = fXi - float(labelMat[i])
            if ((labelMat[i] * Ei < -toler) and (alphas[i] < C)) or ((labelMat[i] * Ei > toler) and (alphas[i] > 0)):
                j = SelectJrand(i, m)
                fXj = float(multiply(alphas, labelMat).T * dataMatrix * dataMatrix[j, :].T) + b
                Ej = fXj - float(labelMat[j])

                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()

                if (labelMat[i] != labelMat[j]):
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L == H:
                    continue

                eta = 2.0 * dataMatrix[i, :] * dataMatrix[j, :].T - \
                      dataMatrix[i, :] * dataMatrix[i, :].T - \
                      dataMatrix[j, :] * dataMatrix[j, :].T
                if eta >= 0:
                    continue
                alphas[j] -= labelMat[j] * (Ei - Ej) / eta
                alphas[j] = clipAlpha(alphas[j], H, L)
                if (abs(alphas[j] - alphaJold) < 0.00001):
                    continue
                alphas[i] += labelMat[j] * labelMat[i] * (alphaJold - alphas[j])
                b1 = b - Ei - labelMat[i] * (alphas[i] - alphaIold) * \
                              dataMatrix[i, :] * dataMatrix[i, :].T - \
                     labelMat[j] * (alphas[j] - alphaJold) * \
                     dataMatrix[i, :] * dataMatrix[j, :].T
                b2 = b - Ej - labelMat[i] * (alphas[i] - alphaIold) * \
                              dataMatrix[i, :] * dataMatrix[j, :].T - \
                     labelMat[j] * (alphas[j] - alphaJold) * \
                     dataMatrix[j, :] * dataMatrix[j, :].T

                if (0 < alphas[i]) and (C > alphas[i]):
                    b = b1
                elif (0 < alphas[j]) and (C > alphas[j]):
                    b = b2
                else:
                    b = (b1 + b2) / 2.0
                alphaPairsChanged += 1
        if (alphaPairsChanged == 0):
            iter += 1
        else:
            iter = 0
        print 'iteration number: %d' % iter
        b = b
    return b, alphas


def PredictByMySVM():
    dataArr, labelArr = ld.GetBayesTrainset(5000,5000)
    b, alphas = Smo(dataArr, labelArr, 0.6, 0.001, 40);
    b = b.tolist()[0][0]
    w = []
    for i in range(2):
        w_i = 0
        for j in range(len(dataArr)):
            w_i += alphas[j] * labelArr[j] * dataArr[j][i]
        w.append(w_i)
    w[0] = w[0].tolist()[0][0]
    w[1] = w[1].tolist()[0][0]
    print 'w is ' + str(w)
    print 'b is ' + str(b)
    needtest_key, needtest_data = ld.GetBayesNeedtest()
    f = open("result/my_svm_result.csv", "wb")
    write = csv.writer(f)
    write.writerow(["user_id", "item_id"])
    for i in range(len(needtest_key)):
        w_x = float(w[0]) * float(needtest_data[i][0]) + float(w[1]) * float(needtest_data[i][1])
        y = w_x + b
        if y >= 1:
            write.writerow([needtest_key[i][0], needtest_key[i][1]])
    f.close()

