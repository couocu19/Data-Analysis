import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#df = pd.read_table("D:\python-study\DataAnalysis\data\mf4257-ftl.csv")
df = pd.read_table("D:\python-study\DataAnalysis\data\mf4257-new-ftl.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

len = df["length"].value_counts().sort_index()
print(len)

#改变样式
#sns.set_style(style="whitegrid")
sns.set_style(style="darkgrid")
sns.set_palette([sns.color_palette("RdBu",n_colors=7)[6]]) #颜色,官网有很多例子


plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


sns.displot(df["length"],bins=500,kde=True)
#plt.xlim(0,5000)
#plt.xticks(np.arange(1000,21000,step=2000))
#plt.ylim(0,4)
#plt.yticks([0,1,2,3,4])
#ax.set_xticks([0,200,400,600,1000])

plt.xlabel("failedAreaLen")
plt.ylabel("failedAreaNum")
plt.title("Distribution diagram of the number of matching failure interval areas-R64-(0~5000)")
#fig.set_xticklabels(1,1000)  todo：改

#plt.hist(df["length"],200)


plt.show()
