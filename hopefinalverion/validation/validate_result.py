import csv
import random

f = open("result/real_result.csv")
realdata = csv.reader(f)
realdata.next()
answerset = set()
for row in realdata:
    key = (row[0],row[1])
    answerset.add(key)
f.close()

rule_predictset = set()
sksvm_predictset = set()
skbayes_predictset = set()
mysvm_predictset = set()
mybayes_predictset = set()

def TestRule():
    print "execute the TestRule"
    f1 = open("result/rule_result.csv")
    ruledata = csv.reader(f1)
    ruledata.next()
    for row in ruledata:
        key = (row[0], row[1])
        rule_predictset.add(key)
    f1.close()
    joinset = rule_predictset & answerset
    j_num = len(joinset)
    a_num = len(answerset)
    p_num = len(rule_predictset)
    precision = 1.0 * j_num / p_num * 100
    recall = 1.0 * j_num / a_num * 100
    F1 = 2.0 * precision * recall / (precision + recall)
    print "rule prediction precision is " + str(precision) + "%"
    print "rule prediction recall is " + str(recall) + "%"
    print "rule prediction F1 is " + str(F1) + "%"
    print "TestRule is ok"

def TestSkSvm():
    print "execute the TestSkSvm"
    f2 = open("result/sk_svm_result.csv")
    sksvmdata = csv.reader(f2)
    sksvmdata.next()
    for row in sksvmdata:
        key = (row[0], row[1])
        sksvm_predictset.add(key)
    f2.close()
    joinset = sksvm_predictset & answerset
    j_num = len(joinset)
    a_num = len(answerset)
    p_num = len(sksvm_predictset)
    precision = 1.0 * j_num / p_num * 100
    recall = 1.0 * j_num / a_num * 100
    F1 = 2.0 * precision * recall / (precision + recall)
    print "sk_svm prediction precision is " + str(precision) + "%"
    print "sk_svm prediction recall is " + str(recall) + "%"
    print "sk_svm prediction F1 is " + str(F1) + "%"
    print "TestSkSvm is ok"

def TestSkBayes():
    print "execute the TestSkBayes"
    f2 = open("result/sk_bayes_result.csv")
    skbayesdata = csv.reader(f2)
    skbayesdata.next()
    for row in skbayesdata:
        key = (row[0], row[1])
        skbayes_predictset.add(key)
    f2.close()
    joinset = skbayes_predictset & answerset
    j_num = len(joinset)
    a_num = len(answerset)
    p_num = len(skbayes_predictset)
    precision = 1.0 * j_num / p_num * 100
    recall = 1.0 * j_num / a_num * 100
    F1 = 2.0 * precision * recall / (precision + recall)
    print "sk_bayes prediction precision is " + str(precision) + "%"
    print "sk_bayes prediction recall is " + str(recall) + "%"
    print "sk_bayes prediction F1 is " + str(F1) + "%"
    print "TestSkBayes is ok"

def TestMySvm():
    print "execute the TestMySvm"
    f2 = open("result/my_svm_result.csv")
    mysvmdata = csv.reader(f2)
    mysvmdata.next()
    for row in mysvmdata:
        key = (row[0], row[1])
        mysvm_predictset.add(key)
    f2.close()
    joinset = mysvm_predictset & answerset
    j_num = len(joinset)
    a_num = len(answerset)
    p_num = len(mysvm_predictset)
    precision = 1.0 * j_num / p_num * 100
    recall = 1.0 * j_num / a_num * 100
    F1 = 2.0 * precision * recall / (precision + recall)
    print "my_svm prediction precision is " + str(precision) + "%"
    print "my_svm prediction recall is " + str(recall) + "%"
    print "my_svm prediction F1 is " + str(F1) + "%"
    print "TestMySvm is ok"

def TestMyBayes():
    print "execute the TestMyBayes"
    f2 = open("result/my_bayes_result.csv")
    mybayesdata = csv.reader(f2)
    mybayesdata.next()
    for row in mybayesdata:
        key = (row[0], row[1])
        mybayes_predictset.add(key)
    f2.close()
    joinset = mybayes_predictset & answerset
    j_num = len(joinset)
    a_num = len(answerset)
    p_num = len(mybayes_predictset)
    precision = 1.0 * j_num / p_num * 100
    recall = 1.0 * j_num / a_num * 100
    F1 = 2.0 * precision * recall / (precision + recall)
    print "my_bayes prediction precision is " + str(precision) + "%"
    print "my_bayes prediction recall is " + str(recall) + "%"
    print "my_bayes prediction F1 is " + str(F1) + "%"
    print "TestMyBayes is ok"

def TestAll():
    print "execute the TestAll"
    predictset = rule_predictset | (sksvm_predictset & skbayes_predictset & mysvm_predictset & mybayes_predictset)
    joinset = predictset & answerset
    j_num = len(joinset)
    a_num = len(answerset)
    p_num = len(predictset)
    precision = 1.0 * j_num / p_num * 100
    recall = 1.0 * j_num / a_num * 100
    F1 = 2.0 * precision * recall / (precision + recall)
    print "combine prediction precision is " + str(precision) + "%"
    print "combine prediction recall is " + str(recall) + "%"
    print "combine prediction F1 is " + str(F1) + "%"
    print "TestAll is ok"