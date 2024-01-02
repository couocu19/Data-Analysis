import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import turtle

##以染色体为单位统计未覆盖区域的中位数、均值以及偏态系数
def getYeastAreas():
    df = pd.read_table("D:\python-study\DataAnalysis\data\\fm160-ftl.csv")
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    #df = pd.read_table("D:\\python-study\\DataAnalysis\\data\\new-covered.csv")
    #print(df.loc[1])
   # print(df)
    classify1 = df.groupby(by = ['chrName','rank'])
    #输出groupby的具体内容
    # for key,value in classify1:
    #     print(key)
    #     print(value)
    classify = df.groupby(by = ['chrName'])
    L1 = [[0 for _ in range (8)] for _ in range (17)]
    L2 = [[0 for _ in range (10)] for _ in range (17)]
    i = 0
    for key,value in classify:
        #print(value)
        max = value["length"].max()
        #print(max)
        min = value["length"].min()
        avg = value["length"].mean() # 均值
        median = value["length"].median() #中位数
        qu = value["length"].quantile(q=0.75)
        sk = value["length"].skew() #偏态系数
        md = value["rank"].mode() #众数
        sum = value["length"].sum()
        #print(max,min,median,sk,sep=' ')
        #print(i)
        L1[i][0] = max
        L1[i][1] = min
        L1[i][2] = avg
        L1[i][3] = median
        L1[i][4] = qu
        L1[i][5] = sk
        L1[i][6] = md
        L1[i][7] = sum
        #print(i)
        #print(L1[i][0], L1[i][1], L1[i][2], L1[i][3], sep=' ')
        i = i+1

    for a in L1:
         print(a[0],a[1],'%.3f'%a[2],a[3],'%.3f'%a[5],a[7],sep='  ')
         #print(a[5])
        #print(a[0],a[1],a[2],a[3],sep=' ' )

    j = 0
    k = 0
    for key,value in classify1:
        #print(len(value))
        L2[j][k] = len(value)
        k = k+1
        if(j == 17):
            break
        if(k == 10):
            j = j+1
            k = 0

#统计未覆盖区域整体的中位数、平均十和偏态系数
def analysisAllFailedArea():
    #新基因组--old
    df1 = pd.read_table("D:\python-study\DataAnalysis\data\\mf4257-new-ftl.csv")
    #新基因组--new
    df2 = pd.read_table("D:\python-study\DataAnalysis\data\\fm160-ftl.csv")
    #旧基因组
    df = pd.read_table("D:\python-study\DataAnalysis\data\\mf4257-ftl.csv")
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)

    df = df[df["length"]>0]
    max = df["length"].max()
    min = df["length"].min()
    avg = df["length"].mean()  # 均值
    median = df["length"].median()  # 中位数
    sk = df["length"].skew()  # 偏态系数


    print(max,min,avg,median,sk)



#  creatAreadistribution(L2)


    # for i in L2:
    #      print(i)


def creatAreadistribution(data):
    x_data = ['区域1','区域2','区域3','区域4','区域5','区域6','区域7','区域8','区域9','区域10']
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False
    cololrs = ['red','#FF8C00','green','blue','pink','orange','brown','#008080','#DEB887','#8B008B','#000080','#32CD32','#708090','#4682B4','#7CFC00','#800080','#D2691E']
    i = 0
    for a in data:
        y = a
        b = i+1
        plt.plot(x_data, y, color=cololrs[i],marker='o', linestyle='-', label='chr%d'%b)
        #break
        i = i+1

    plt.legend()
    plt.xlabel("每条染色体的分割区域")  # X轴标签
    plt.ylabel("当前区域上的新区域区域的个数")  # Y轴标签
    plt.ylim(0,700)
    plt.show()


if __name__ == '__main__':
    #getYeastAreas()
    analysisAllFailedArea()