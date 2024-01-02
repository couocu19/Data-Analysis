import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# 读取表格数据
df = pd.read_table('E:\\complete-gene-ann\\汇总-新区域分布\\ms-AllArea-829.bed', header=None, delimiter='\t', names=['col1', 'col2', 'col3', 'col4', 'col5'])
#整体修改第四列的列名，区分人类和拟南芥
df.loc[df['col4'] == 'chr20','col4'] = 'chrX'
df.loc[df['col4'] == 'chr21','col4'] = 'chrY'
# df.loc[df['col4'] == 'f.vesca-chr3','col4'] = 'chr3'
#df.loc[df['col4'] == 'f.vesca-chr4','col4'] = 'frag.-chr4'
# df.loc[df['col4'] == 'f.vesca-chr5','col4'] = 'chr5'
# df.loc[df['col4'] == 'f.vesca-chr6','col4'] = 'chr6'
# df.loc[df['col4'] == 'f.vesca-chr7','col4'] = 'chr7'
#
#df.loc[df['col5'] == 'newArea','col5'] = 'filled region'
#df.loc[df['col5'] == 'commonArea','col5'] = 'other region'
#df1=df.loc[df['col1']!='chr7']

# data = df.apply(lambda row: (row['col2'], row['col3']), axis=1).tolist()
# data1 = []
# minv = 0
# #maxv = [151935994,144995196,43931233]
# #max = 151935994
# maxv = [248387328,99753195]
# #max = 144995196
# max=34388015
# i=0
# for a in data:
#    # if i==67952:
#     #    max = 99753195
#     #elif i== 5477:
#      #  max = 43931233
#     s = (a[0]-minv)/max
#     e = (a[1]-minv)/max
#     #print(s,e)
#     data1.append((s,e))
#     i = i+1
#
# #print(data1)
# df[['col2','col3']] = data1
# print(df)
#
df.to_csv('E:\\complete-gene-ann\\汇总-新区域分布\\ms-AllArea-829.bed',index=False,sep='\t')

#df1 = pd.read_table("hmrpt115-all.txt",header=None, delimiter='\t', names=['col1', 'col2', 'col3', 'col4', 'col5'])
#df1=df.loc[df['col2']<=df['col3']]
#df1.to_csv('E:\\complete-gene-ann\\f.vesca-草莓\\fv-new-chr4-std.txt',index=False,sep='\t')
#test=df1.loc[df['col3']>1]
#print(test)