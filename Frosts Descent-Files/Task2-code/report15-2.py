import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties



# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei'是黑体的意思
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 加载数据
file_path = r"C:\Users\27234\Desktop\AI\BIGDATA\列表网二手车列表及详情页采集.csv"
df = pd.read_csv(file_path, encoding="gbk")

# 填充缺失数据为"未知"
df.fillna("未知", inplace=True)

import jieba
import jieba.analyse
import matplotlib.pyplot as plt
import pandas as pd
import re

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei'是黑体的意思
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 加载数据
file_path = r"C:\Users\27234\Desktop\列表网二手车列表及详情页采集.csv"
df = pd.read_csv(file_path, encoding="gbk")

# 填充缺失数据为"未知"
df.fillna("未知", inplace=True)

# 根据'品牌'列进行分组，创建子数据集
grouped = df.groupby('品牌')

# 创建一个字典，用于存储按品牌分组的子数据集
brand_datasets = {brand: data.reset_index(drop=True) for brand, data in grouped}

def clean_and_extract_number(series):
    # 排除'面议'和'未知'，并提取数字，这里使用正则表达式
    return series.str.replace('面议|未知', '', regex=True).str.extract(r'(\d+\.?\d*)', expand=False).astype(float)

# 对每个品牌进行数据清洗和提取数字
for brand, data in brand_datasets.items():
    data['价格'] = clean_and_extract_number(data['价格'])
    data['年龄'] = clean_and_extract_number(data['年龄'])
    data['行驶里程'] = clean_and_extract_number(data['行驶里程'])

    # 只有当三个字段都不为空时，才能绘制箱型图
    if data['价格'].notna().any() and data['年龄'].notna().any() and data['行驶里程'].notna().any():
        # 绘制箱型图
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))  # 创建一个包含3个子图的图形
        data.boxplot(column='价格', ax=axes[0])  # 价格的箱型图
        axes[0].set_title(f'{brand} 品牌价格箱型图')
        axes[0].set_ylabel('价格')

        data.boxplot(column='年龄', ax=axes[1])  # 年龄的箱型图
        axes[1].set_title(f'{brand} 品牌年龄箱型图')
        axes[1].set_ylabel('年龄')

        data.boxplot(column='行驶里程', ax=axes[2])  # 行驶里程的箱型图
        axes[2].set_title(f'{brand} 品牌行驶里程箱型图')
        axes[2].set_ylabel('行驶里程')

        plt.suptitle(f'{brand} 品牌数据箱型图')  # 设置总标题
        plt.tight_layout(rect=[0, 0, 1, 0.95])  # 调整布局
        plt.show()  # 展示箱型图
# 假设"描述"列包含了文本信息
descriptions = df["描述"].tolist()
keywords = []

# 通过循环提取每个描述的关键字
for desc in descriptions:
    # 这里设置topK为10，表示提取每个描述中的前10个关键词
    extracted_keywords = jieba.analyse.extract_tags(desc, topK=10)
    keywords.append(extracted_keywords)

# 如果您有停用词表，可以这样使用它
# file_path = open(r"C:\Users\27234\Desktop\AI\BIGDATA\停用词表.txt", encoding="utf-8")
# stop_word = file_path.read()
# jieba.analyse.set_stop_words(stop_word)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from wordcloud import WordCloud

# 将所有关键词合并为一个长字符串，以便生成词云
all_keywords = " ".join([" ".join(kw) for kw in keywords])

# 生成词云
wordcloud = WordCloud(
    font_path=r"C:\Users\27234\AppData\Local\Microsoft\Windows\Fonts\AaErMoXingShu-2.ttf",
    width=800,
    height=400,
).generate(all_keywords)

# 绘制词云
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
