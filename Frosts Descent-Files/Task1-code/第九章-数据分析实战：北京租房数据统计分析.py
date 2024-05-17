# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


class LngLat:
    def get_data(self):
        house_names = file_data['位置']
        house_names = house_names.tolist()
        return house_names

    def get_url(self):
        url_temp = "http://api.map.baidu.com/geocoder/v2/?address={}"\
                   "&output = json" \
                   "&ak = gfRHhpMyINfZkCEni0t5Vu05p24QfxMB" \
                   "&callback = showLocation"
        house_names = self.get_data()
        return [url_temp.format(i) for i in house_names]

    def parse_url(self, url):
        while 1:
            try:
                r = requests.get(url)
            except requests.exceptions.ConnectionError:
                time.sleep(2)
                continue
            return r.content.decode('UTF-8')

    def run(self):
        li = []
        urls = self.get_url()
        for url in urls:
            data = self.parse_url(url)
            str = data.split("{")[-1].split("}")[0]
            try:
                lng = float(str.split(",")[0].split(":")[1])
                lat = float(str.split(",")[1].split(":")[1])
            except ValueError:
                continue
            dict_data = dict(lng=lng, lat=lat, count=1)
            li.append(dict_data)
        f = open(r'C:\Users\94506\Desktop\Files\Data analysis\pythonProject1\经纬度信息.txt', 'w')
        f.write(json.dumps(li))
        f.close()
        print('正在写入...')
        print('写入成功！')

file_path = open('链家北京租房数据.csv')
file_data = pd.read_csv(file_path)
print(file_data)
print(file_data.duplicated())
file_data = file_data.drop_duplicates()
print(file_data)

file_data = file_data.dropna()
print(file_data)

data_new = np.array([])
data = file_data['面积(㎡)'].values
for i in data:
    data_new = np.append(data_new, np.array(i[:-2]))
data = data_new.astype(np.float64)
file_data.loc[:, '面积(㎡)'] = data
print(file_data)

housetype_data = file_data['户型']
temp_list = []
for i in housetype_data:
    new_info = i.replace('房间', '室')
    temp_list.append(new_info)
file_data.loc[:, '户型'] = temp_list
print(file_data)

new_df = pd.DataFrame({'区域': file_data['区域'].unique(), '数量': [0] * 13})
print(new_df)

print()
groupby_area = file_data.groupby(by='区域').count()
new_df['数量'] = groupby_area.values
print(new_df)
print('\n', new_df.sort_values(by='数量', ascending=False))

file_data['位置'] = '北京市' + file_data['区域'].values + '区' + file_data['小区名称'].values
print(file_data)

# coding = utf-8
import requests
import time
import json
execute = LngLat()
execute.run()

# def all_house(arr):
#     arr = np.array(arr)
#     key = np.unique(arr)
#     result = {}
#     for k in key:
#         mask = (arr == k)
#         arr_new = arr[mask]
#         v = arr_new.size
#         result[k] = v
#     return result
#
# house_array = file_data['户型']
# house_info = all_house(house_array)
# print(house_info)
#
# house_type = dict((key,value) for key,value in house_info.items() if value > 50)
# show_houses = pd.DataFrame({'户型':[x for x in house_type.keys()],'数量':[x for x in house_type.values()]})
# print(show_houses)
#
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# matplotlib.rcParams['axes.unicode_minus'] = False
# house_type = show_houses['户型']
# house_type_num = show_houses['数量']
# plt.barh(range(11),house_type_num,height = 0.7,color = 'steelblue',alpha = 0.8)
# plt.yticks(range(11),house_type)
# plt.xlim(0,2500)
# plt.xlabel('数量')
# plt.ylabel('户型种类')
# plt.title("北京地区各户型房屋数量")
# for x,y in enumerate(house_type_num):
#     plt.text(y + 0.2,x - 0.1,'%s' %y)
# plt.show()
#
# df_all = pd.DataFrame({'区域':file_data['区域'].unique(),
#                        '房屋总金额':[0] * 13,
#                        '总面积(㎡)':[0] * 13})
# print(df_all)
# sum_price = file_data['价格(元/月)'].groupby(file_data['区域']).sum()
# sum_area = file_data['面积(㎡)'].groupby(file_data['区域']).sum()
# df_all['房屋总金额'] = sum_price.values
# df_all['总面积(㎡)'] = sum_area.values
# print(df_all)
#
# df_all['每平方千米租金（元）'] = round(df_all['房屋总金额'] / df_all['总面积(㎡)'],2)
# print(df_all)
#
# df_merge = pd.merge(new_df,df_all)
# print(df_merge)
#
# import matplotlib.ticker as mtick
# from matplotlib.font_manager import FontProperties
# num = df_merge['数量']
# price = df_merge['每平方千米租金（元）']
# l = [i for i in range(13)]
# plt.rcParams['font.sans-serif'] = ['SimHei']
# lx = df_merge['区域']
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax1.plot(l,price,'or-',label = '价格')
# for i,(_x,_y) in enumerate(zip(l,price)):
#     plt.text(_x,_y,price[i],color = 'black',fontsize = 10)
# ax1.set_ylim([0,200])
# ax1.set_ylabel('价格')
# plt.legend(prop = {'family':'SimHei','size':8},loc = 'upper left')
# ax2 = ax1.twinx()
# plt.bar(l,num,alpha = 0.3,color = 'green',label = '数量')
# ax2.set_ylabel('数量')
# ax2.set_ylim([0,2000])
# plt.legend(prop = {'family':'SimHei','size':8},loc = 'upper right')
# plt.xticks(l,lx)
# plt.show()
#
# print('房屋最大面积是%d平方米'%(file_data['面积(㎡)'].max()))
# print('房屋最小面积是%d平方米'%(file_data['面积(㎡)'].min()))
# print('房屋最高价格为%d元'%(file_data['价格(元/月)'].max()))
# print('房屋最低价格为%d元'%(file_data['价格(元/月)'].min()))
#
# area_divide = [1,30,50,70,90,120,140,160,1200]
# area_cut = pd.cut(list(file_data['面积(㎡)']),area_divide)
# area_cut_data = area_cut.describe()
# print(area_cut_data)
#
# area_percentage = (area_cut_data['freqs'].values) * 100
# np.set_printoptions(precision = 2)
# labels = ['30平方米以下','30-50平方米','50-70平方米','70-90平方米',
#           '90-120平方米','120-140平方米','140-160平方米','160平方米以上',]
# plt.axes(aspect = 1)
# plt.pie(x = area_percentage,labels = labels,autopct = "%.2f %%",
#         shadow = True,labeldistance = 1.2,startangle = 90,pctdistance = 0.7)
# plt.legend(loc = 'upper right')
# plt.show()
