import processdata.processdata_date as pd
pd.splitByDate()

import processdata.processdata_user as pu
pu.splitByUser()

import processdata.processdata_hour as ph
ph.splitByHour()

import processdata.abnormal_user as au
au.GetAbnormalUsers()

import findrules.behavior_date as bd
bd.BehaviorChangeByDate()

import findrules.behavior_hour as bh
bh.BehaviorChangeByHour()

import findrules.notbuy_buy_distance as nbd
nbd.click_buy_distance()
nbd.look_buy_distance()
nbd.cart_buy_distance()

import collectfeatures.collect_ratio_user as cru
cru.CollectRatio_click()
cru.CollectRatio_look()
cru.CollectRatio_cart()

import collectfeatures.collect_ratio_item as cri
cri.CollectRatio_click()
cri.CollectRatio_look()
cri.CollectRatio_cart()

import collectfeatures.collect_meanvalue_user as cmu
cmu.CollectMeanvalue_click()
cmu.CollectMeanvalue_look()
cmu.CollectMeanvalue_cart()
cmu.CollectMeanvalue_buy()

import collectfeatures.collect_basefeature as cb
cb.CollectItemBasefeature()
cb.CollectUserBasefeature()

import preparedata.produce_trainset as pt
pt.ProduceTrainset()

import findrules.trainset_distribution as td
td.TrainsetDistribution()

import preparedata.produce_needtest as pn
pn.ProduceNeedtest()

import preparedata.produce_realresult as pr
pr.ProduceRealresult()

import predictresult.rule_predict as rp
rp.PredictByRule()

import predictresult.sk_svm_predict as ssp
ssp.PredictBySkSVM()

import predictresult.sk_bayes_predict as sbp
sbp.PredictBySkBayes()

import predictresult.my_svm_predict as msp
msp.PredictByMySVM()

import predictresult.my_bayes_predict as mbp
mbp.PredictByMyBayes()

import validation.validate_result as vr
vr.TestRule()
vr.TestSkSvm()
vr.TestSkBayes()
vr.TestMySvm()
vr.TestMyBayes()
vr.TestAll()

