import os
import csv


def GetAbnormalUsers():
    usercsvlist = os.listdir("data/userdata/")
    usercsvlist.sort()
    count = 0
    w_f = open("data/abnormaldata/abnormal_user.csv", 'wb')
    write = csv.writer(w_f)
    write.writerow(["user_id","click","look","cart","buy"])
    total = 0
    for eachcsv in usercsvlist:
        count += 1
        print "now process the " + str(count) + "th csv"
        user_id = eachcsv.split('.')[0]
        f = open("data/userdata/" + eachcsv)
        rows = csv.reader(f)
        rows.next()
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        cnt4 = 0
        for row in rows:
            date = row[0]
            if date == '2014-12-12' or date == '2014-12-17':
                continue
            b_type = row[2]
            if b_type == '1':
                cnt1 += 1
            if b_type == '2':
                cnt2 += 1
            if b_type == '3':
                cnt3 += 1
            if b_type == '4':
                cnt4 += 1
        if cnt1 > 0 and cnt2 == 0 and cnt3 == 0 and cnt4 == 0:
            write.writerow([user_id,cnt1,cnt2,cnt3,cnt4])
            total += 1
        if cnt1 > 5000 and cnt4 < 10 and cnt4 > 0:
            write.writerow([user_id, cnt1, cnt2, cnt3, cnt4])
            total += 1
        if cnt1 == 0 and cnt2 == 0 and cnt3 == 0 and cnt4 > 0:
            write.writerow([user_id, cnt1, cnt2, cnt3, cnt4])
            total += 1
        f.close()
    w_f.close()
    print "have " + str(total) + " abnormal users"