import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

file_path_bj = open(r'C:\Users\94506\Desktop\Files\Data analysis\pythonProject1\北京地区信息.csv',encoding = 'gbk')
file_data_bjinfo = pd.read_csv(file_path_bj)
print(file_data_bjinfo)
file_path_tj = open(r'C:\Users\94506\Desktop\Files\Data analysis\pythonProject1\天津地区信息.csv',encoding = 'gbk')
file_data_tjinfo = pd.read_csv(file_path_tj)
print('\n',file_data_tjinfo)

print()
print(file_data_bjinfo.duplicated())
print('\n',file_data_bjinfo.duplicated())

file_data_bjinfo = file_data_bjinfo.drop_duplicates()
print('\n',file_data_bjinfo)

print()
print(file_data_tjinfo.isnull())

print()
population = float("{:.2f}".format(file_data_tjinfo['常住人口（万人）'].mean()))
values = {'常住人口（万人）':population}
file_data_tjinfo = file_data_tjinfo.fillna(value = values)
print(file_data_tjinfo)

file_data_bjinfo.boxplot(column = ['行政面积（K㎡）','户籍人口（万人）','男性','女性','GDP（亿元）','常住人口（万人）'])
plt.show()
file_data_tjinfo.boxplot(column = ['行政面积（K㎡）','户籍人口（万人）','男性','女性','GDP（亿元）','常住人口（万人）'])
plt.show()

print()
print(pd.concat([file_data_bjinfo,file_data_tjinfo],ignore_index = True))