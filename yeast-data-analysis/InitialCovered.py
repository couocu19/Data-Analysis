import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#绘制酵母个体SRR4074257和新旧基因组比对后的mapping率柱状图
#plt.style.use('science')
#sns.set_style(style="whitegrid")
#sns.set_palette([sns.color_palette("pastel",n_colors=10)[1]]) #颜色,官网有很多例子
#sns.set_palette(sns.color_palette("tab20c"))
#sns.set_palette(sns.color_palette("Set2"))
sns.set_palette(sns.color_palette("RdPu"))
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

#去掉顶部和右边边框
fig, ax = plt.subplots()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

#data = [0.34,0.71]
#data = [0.203,0.163]
data = [0.87,0.57]
x_data = ['old','new']
#sns.barplot(x=x_data,y=data)
plt.bar(x_data,data,width=0.7)
#plt.ylabel("Rate of coverage")
plt.ylabel("Mapping rate")
plt.xlabel("Yeast genome version")
plt.ylim(0,1)

plt.show()

