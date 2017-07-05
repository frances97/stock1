# -*- coding: utf-8 -*-
from _future_ import division
"""
Created on Wed Oct 19 14:53:21 2016

@author: 96004
"""
####*************此处求出的是每天的情况********************************
import pandas as pd 
data=pd.read_csv('E:/szlv2trans/sz000727.csv',encoding="gb2312")
data=data[data[u'执行类型'].isin(['F'])]
print date[i],'交易总次数',len(data)
data[u'成交金额']=data[u'成交价格']*data[u'成交数量']# 给excel增加了一列买入金额

#对成交金额按照委买序号进行汇总
data0=data[[u'委买序号',u'成交金额']]
grouped_buy0=data0.groupby([u'委买序号'],sort=False).sum()
grouped_buy0=grouped_buy0.sort(columns=u'成交金额',ascending=False)
import numpy as np
a=np.percentile(np.array(grouped_buy0),95)#95%分位数
#多少算大单  #此处成交金额在前5%分位数的为大单
grouped_buy0=grouped_buy0[grouped_buy0[u'成交金额']>a] 
grouped_buy=grouped_buy0[grouped_buy0[u'成交金额']>10**6 ] #大单给了一个相对的概念。。。。大于95%分位数并且大于100万的。此处我们规定为大单买单

Main_Cash_in=grouped_buy.sum() #主力流入

#对成交金额按照委卖序号进行汇总
data1=data[[u'委卖序号',u'成交金额']]
grouped_sell0=data1.groupby([u'委卖序号'],sort=False).sum()
grouped_sell0=grouped_sell0.sort(columns=u'成交金额',ascending=False)
a1=np.percentile(np.array(grouped_sell0),95)#95%分位数
grouped_sell0=grouped_sell0[grouped_sell0[u'成交金额']>a] 
grouped_sell=grouped_sell0[grouped_sell0[u'成交金额']>10**6 ] 

Main_Cash_out=grouped_sell.sum()     #主力流出

Main_NetCash=Main_Cash_in-Main_Cash_out    #主力的净流入


#求出主力每天的建仓成本
data_main_buy=data[[u'委买序号',u'成交数量',u'成交金额']]
grouped_main_buy0=data_main_buy.groupby([u'委买序号'],sort=False).sum() 
grouped_main_buy=grouped_main_buy0[grouped_main_buy0[u'成交金额']>max(a,10**6)]
main_principle=grouped_main_buy[u'成交金额'].sum()/grouped_main_buy[u'成交数量'].sum()  #主力的建仓成本





