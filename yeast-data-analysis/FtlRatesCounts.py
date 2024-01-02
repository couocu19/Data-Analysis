import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



fig, ax = plt.subplots()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
df1 = pd.read_table("D:\python-study\DataAnalysis\data\\fm160-ftl.csv")
df = pd.read_table("D:\python-study\DataAnalysis\data\mf4257-ftl.csv")
#df1 = pd.read_table("D:\python-study\DataAnalysis\data\mf4257-new-ftl.csv")
dff = pd.read_table("D:\python-study\DataAnalysis\data\\new-covered.csv")
dff1 = pd.read_table("D:\python-study\DataAnalysis\data\\r-covered.csv")  #新基因组二次比对的新区域

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#maxl=df["length"].max()
#print(maxl)

#len = df["length"].value_counts().sort_index()
#print(len)

#改变样式
#sns.set_style(style="whitegrid")
#sns.set_style(style="darkgrid")
sns.set_palette([sns.color_palette("PuBu",n_colors=10)[5]]) #颜色,官网有很多例子
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

#画图部分
#sns.displot(df["length"],bins=500,kde=True)
#sns.displot(df1["length"],bins=500,kde=True)

#sns.distplot(df["length"],bins=500,hist=True,kde=False,color="#FF0000",label='old')
#sns.distplot(df1["length"],bins=800,hist=True,kde=True,color="#4169E1",label='new')

#plt.xlim(0,5000)
#plt.xticks(np.arange(5000,18825,step=2000))
#plt.ylim(0,1)
#plt.yticks([0,1])
#ax.set_xticks([0,200,400,600,1000])
#plt.xlabel("failedAreaLen")
#plt.ylabel("failedAreaNum")
#plt.title("Distribution diagram of the number of matching failure interval areas-R64(5000~18825)")
#plt.legend()
#plt.show()
#print(len(df)) #1898
#df_new = df[df["length"]>=5000]["length"].value_counts().sort_index()
#print(df_new)  #1669 长度小于等于500的reads占所有区间的87％
# df_chr_grp=df_new.groupby("chrName")
# for key,value in df_chr_grp:
#     print(key)
#     print(value)
#sns.countplot(x="rank",hue="chrName",data=df_new)
#sns.set_palette(sns.color_palette("RdBu",n_colors=7))

#value = [df["rank"],df1["rank"]]

#plt.hist([df["rank"],df1["rank"]],bins=10,stacked=True)
#plt.hist(value,bins=10,stacked=True,label=["old","new"])
fig, a = plt.subplots(figsize=(10,6))
#a=sns.displot(df["rank"],kind="hist",bins=10,kde=True,label='old')

a=sns.distplot(dff["rank"],hist=True,bins=10,kde=False,color="#87CEFA",label="old-newCoverageArea" )
a=sns.distplot(dff1["rank"],hist=True,bins=10,kde=False,color="#191970",label="new-newCoverageArea" )
a=sns.distplot(df["rank"],hist=True,bins=10,kde=False,color="#B0C4DE",label="old-uncoveredArea" )
a=sns.distplot(df1["rank"],hist=True,bins=10,kde=False,color="#4682B4",label="new-uncoveredArea" )
plt.legend()
plt.xticks([1,2,3,4,5,6,7,8,9,10])

#plt.yticks([0,2,4,6,8,10,12,14,16,18])
#plt.title("Map of the uncovered regions on each chromosome-old")
#plt.title("Map of the distribution of the newly covered region on each chromosome-new")
#plt.title("Map of the distribution of the newly matched regions on the chromosome-old")

#将图片保存为svg
#path=r'C:\Users\couco\Desktop\论文初稿\img'
#fig.savefig(path+'\\test.svg',format='svg',dpi=150)

plt.show()

