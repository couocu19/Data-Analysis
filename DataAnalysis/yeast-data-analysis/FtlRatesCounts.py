import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_table("D:\python-study\DataAnalysis\data\mf4257-ftl.csv")
#df = pd.read_table("D:\python-study\DataAnalysis\data\mf4257-new-ftl.csv")
#df1 = pd.read_table("D:\python-study\DataAnalysis\data\\new-covered.csv")
#df = pd.read_table("D:\python-study\DataAnalysis\data\\r-covered.csv")  #新基因组二次比对的新区域

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#len = df["length"].value_counts().sort_index()
#print(len)

#改变样式
#sns.set_style(style="whitegrid")
sns.set_style(style="darkgrid")
sns.set_palette([sns.color_palette("RdBu",n_colors=7)[1]]) #颜色,官网有很多例子
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

#画图部分
# sns.displot(df["length"],bins=500,kde=True)
#plt.xlim(0,5000)
#plt.xticks(np.arange(1000,21000,step=2000))
#plt.ylim(0,4)
#plt.yticks([0,1,2,3,4])
#ax.set_xticks([0,200,400,600,1000])
# plt.xlabel("failedAreaLen")
# plt.ylabel("failedAreaNum")
#plt.title("Distribution diagram of the number of matching failure interval areas-R64-(0~5000)")
#
# plt.show()
print(len(df)) #1898
df_new = df[df["length"]<=500].sort_index()
print(len(df_new))  #1669 长度小于等于500的reads占所有区间的87％
# df_chr_grp=df_new.groupby("chrName")
# for key,value in df_chr_grp:
#     print(key)
#     print(value)


sns.countplot(x="rank",hue="chrName",data=df_new)
#sns.set_palette([sns.color_palette("RdBu",n_colors=7)[5]])

#sns.displot(df["rank"],bins=10,kde=True)
#sns.displot(df1["rank"],bins=10,kde=True)

#plt.xticks([1,2,3,4,5,6,7,8,9,10])

#plt.yticks([0,2,4,6,8,10,12,14,16,18])
#plt.title("Map of the uncovered regions on each chromosome-old")
#plt.title("Map of the distribution of the newly covered region on each chromosome-new")
#plt.title("Map of the distribution of the newly matched regions on the chromosome-old")

plt.show()

