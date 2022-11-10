import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_table("D:\python-study\DataAnalysis\data\s4257-on-window.csv")

df1 = pd.read_table("D:\python-study\DataAnalysis\data\s4257-on-window-old.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
reads=df1["readsNum"].value_counts(sort=False).sort_index()#排序输出
print(reads)
#df = df[df["readsNum"]>0]
total_len = df["areaLen"].sum()

res_rates=[] #初始化结果数组

for i in range(1,83245):
    print('计算第',i,'层')
    df = df[df["readsNum"] >= i].reset_index(drop=True)  #重新设置索引
    windows_rates = 0
    for j in range(0,len(df)):
       windows_rates += (df["rates"][j] * df["areaLen"][j])/total_len
    if(windows_rates < 0.01):
        break
    #res_rates[i-1] = windows_rates
    res_rates.append(windows_rates)

    #print(res_rates[i])

print('-----------end-----------------')

res_rates1=[]

for i in range(1,207101):
    print('计算第',i,'层')
    df1 = df1[df1["readsNum"] >= i].reset_index(drop=True)  #重新设置索引
    windows_rates1 = 0
    for j in range(0,len(df1)):
       windows_rates1 += (df1["rates"][j] * df1["areaLen"][j])/total_len
    if(windows_rates1 < 0.01):
        break
    res_rates1.append(windows_rates1)

    #print(res_rates[i])


#绘制reads层数与reads覆盖率曲线图

#改变样式
sns.set_style(style="whitegrid")
sns.set_palette(sns.color_palette("RdBu",n_colors=7)) #颜色,官网有很多例子

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

x_data = [f"≥{i}" for i in range(0, len(res_rates))]
x_data1 = [f"≥{i}" for i in range(0, len(res_rates1))]
plt.xticks(np.arange(0, len(res_rates1), step=100))
plt.xlabel("readsNum")
plt.ylabel("rates")
plt.title("Overlay graph of the number of reads layers")
plt.ylim(0, 1)

plt.plot(x_data,res_rates,marker='o',  linewidth=0.1,linestyle='-',label='GCF_000146045.2_R64_genomic.fna')
plt.plot(x_data1,res_rates1,marker='o',  linewidth=0.1,linestyle='-',label='S288C_reference_sequence_R64-3-1_20210421.fna')
plt.legend()


plt.show()





