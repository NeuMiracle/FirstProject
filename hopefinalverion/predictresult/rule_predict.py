import preparedata.load_data as ld
import csv

def PredictByRule():
    csvpath = "data/datedata/2014-12-16.csv"
    dict_suspect = ld.GetCartButNotBuy(csvpath)
    abnormal =ld.LoadAbnormal()
    f = open("result/rule_result.csv", "wb")
    write = csv.writer(f)
    write.writerow(["user_id", "item_id"])
    for key in dict_suspect:
        hour = int(dict_suspect[key])
        if hour < 17:
            continue
        user_id, item_id = key
        if abnormal.has_key(user_id):
            continue
        write.writerow([user_id,item_id])
    f.close()
