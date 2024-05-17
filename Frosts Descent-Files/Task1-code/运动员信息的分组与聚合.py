import pandas as pd
file_path = open('运动员信息表.csv')
df = pd.read_csv(file_path)
print(df)

data_group = df.groupby('项目')
df_basketball = dict([x for x in data_group])['篮球']
print(df_basketball)

print()
sex = df_basketball[["年龄（岁）","身高(cm)","体重(kg)"]].groupby(df_basketball["性别"])
print(sex.mean())

print()
info = sex.transform('mean')
print(info)

print()
sex = df_basketball.groupby(df["性别"])
basketball_male=dict([x for x in sex])['男']
print(basketball_male)

def range_data_group(arr):
    return arr.max()-arr.min()
print()
print(basketball_male.agg({"年龄（岁）":range_data_group,
                           "身高(cm)":range_data_group,
                           "体重(kg)":range_data_group}))

print()
df_basketball['体质指数'] = 0
print(df_basketball)

def outer(num):
    def ath_bmi(sum_bmi):
        weight = df_basketball["身高(cm)"]
        height = df_basketball["体重(kg)"]
        sum_bmi = weight / (height / 100) ** 2
        return num + sum_bmi
    return ath_bmi

all_bmi = df_basketball["体质指数"]
df_basketball["体质指数"] = df_basketball[["体质指数"]].apply(outer(all_bmi))
print()
print(df_basketball)




