import pandas as pd
import numpy as np
df_obj = pd.read_excel(r'C:\Users\94506\Desktop\Files\Data analysis\pythonProject1\scores.xlsx',header=[0,1])
print(df_obj)

sorted_obj = df_obj.sort_index(ascending = False)
# print(sorted_obj)

print('\n')
print(sorted_obj.max())
print(sorted_obj.min())
result1 = sorted_obj['一本分数线','文科']
result1 = np.ptp(result1,axis = 0)
print(result1)
result2 = sorted_obj['一本分数线','理科']
result2 = np.ptp(result2,axis = 0)
print(result2)
result3 = sorted_obj['二本分数线','文科']
result3 = np.ptp(result3,axis = 0)
print(result3)
result4 = sorted_obj['二本分数线','理科']
result4 = np.ptp(result4,axis = 0)
print(result4)

print('\n')
ser_obj1 = sorted_obj['一本分数线','文科']
print(ser_obj1[0] - ser_obj1[1])
ser_obj2 = sorted_obj['一本分数线','理科']
print(ser_obj2[0] - ser_obj2[1])
ser_obj3 = sorted_obj['二本分数线','文科']
print(ser_obj3[0] - ser_obj3[1])
ser_obj4 = sorted_obj['二本分数线','文科']
print(ser_obj4[0] - ser_obj4[1])

print('\n')
print(sorted_obj.describe())