import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#改变样式
sns.set_style(style="whitegrid")
sns.set_context(context="poster",font_scale=0.5) #字体
#sns.set_palette(sns.color_palette("RdBu",n_colors=7)) #颜色,官网有很多例子

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# 读取表格数据

df = pd.read_csv('E:\\pangenome\\arab\\ab-allSvCount.bed', sep='\t', header=None,names=['chrName','start','end','count'])
#df['len'] = df['end'] - df['start']

###筛选出区间长度在300以上且数量大于等于10的区间集合
df1 = df[(df['end']-df['start']>50) & (df['count']>16)]
df1['len'] = df['end'] - df['start']
#获取sv区间长度的数量分布直方图
sns.displot(df1["len"],bins=50,kde=True)
plt.xlim(100, 10000)
plt.show()
#df1.to_csv("E:\\pangenome\\sheep\\onlychr-allSvCount-50-21.txt",sep='\t',index=False,header=None)
#df1['len'] = df1.apply(df1['end'] - df1['start'])

###输出sv区间的最大值，最小值，平均值
print(len(df1))
print(df1['len'].max())
print(df1['len'].min())
#print(df['len'].mean())