import pandas as pd
from datetime import datetime
#使用parse_date将成交时间转化为时间格式
data=pd.read_csv("/Users/zhouya/Desktop/testData/sales.csv",encoding='gbk',parse_dates=['成交时间'])
# print(data.info())
# print(data.head())
#计算月销售额，客流量（通过订单id计算），客单价格
def get_month_report(data,datetime1,datetime2):
    # 选取一个月的数据
    month_data = data[(data["成交时间"] >= datetime1) & (data["成交时间"] <= datetime2)]
    sale=(month_data['单价']*month_data['销量']).sum()
    traffic=month_data['订单ID'].drop_duplicates().count()
    personSale=sale/traffic
    return(sale,traffic,personSale)


if __name__=="__main__":
    #本月
    sale1,traffic1,personSale1=get_month_report(data,datetime(2018,2,1),datetime(2018,2,28))
    #上月
    sale2,traffic2,personSale2=get_month_report(data,datetime(2018,1,1),datetime(2018,1,31))
    #去年本月
    sale3,traffic3,personSale3=get_month_report(data,datetime(2017,2,1),datetime(2017,2,28))
    report=pd.DataFrame([[sale1,sale2,sale3],[traffic1,traffic2,traffic3],[personSale1,personSale2,personSale3]],columns=['本月累计','上月同期','去年同期'],index=['销售额','客流量','客单价'])
    report['同比']=report['本月累计']/report['去年同期']-1
    report['环比']=report['本月累计']/report['上月同期']-1
    print(report)
    #讲数据导到本地
    report.to_csv('/Users/Desktop/testData/saleReport.csv',sep='\t')


