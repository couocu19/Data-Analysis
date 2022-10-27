import pandas as pd


def getYeastAreas():
    #df = pd.read_table("D:\python-study\DataAnalysis\data\mf4257-ftl.csv")
    df = pd.read_table("D:\\python-study\\DataAnalysis\\data\\new-covered.csv")


   # print(df)
    classify1 = df.groupby(by = ['chrName','rank'])
    #输出groupby的具体内容
    # for key,value in classify1:
    #     print(key)
    #     print(value)
    classify = df.groupby(by = ['chrName'])
    L1 = [[0 for _ in range (6)] for _ in range (17)]
    L2 = [[0 for _ in range (10)] for _ in range (17)]
    i = 0
    for key,value in classify:
        #print(value)
        max = value["length"].max()
        #print(max)
        min = value["length"].min()
        avg = value["length"].mean() # 均值
        median = value["length"].median() #中位数
        sk = value["length"].skew() #偏态系数
        md = value["rank"].mode() #众数
        #print(max,min,median,sk,sep=' ')
        #print(i)
        L1[i][0] = max
        L1[i][1] = min
        L1[i][2] = avg
        L1[i][3] = median
        L1[i][4] = sk
        L1[i][5] = md
        #print(i)
        #print(L1[i][0], L1[i][1], L1[i][2], L1[i][3], sep=' ')
        i = i+1


    for a in L1:
        # print(a[0],a[1],'%.3f'%a[2],a[3],'%.3f'%a[4],sep='  ')
         print(a[5])
    #     #print(a[0],a[1],a[2],a[3],sep=' ' )

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


    # for i in L2:
    #     print(i)







if __name__ == '__main__':
    getYeastAreas()