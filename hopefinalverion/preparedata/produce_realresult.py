import csv

def ProduceRealresult():
    f = open("result/real_result.csv", "wb")
    write = csv.writer(f)
    write.writerow(["user_id", "item_id"])

    file = open("data/datedata/2014-12-17.csv")
    rows = csv.reader(file)
    rows.next()
    total_num = 0
    for row in rows:
        user_id = row[0]
        item_id = row[1]
        b_type = row[2]
        if b_type == '4':
            write.writerow([user_id,item_id])
            total_num += 1
    file.close()

    f.close()
    print total_num