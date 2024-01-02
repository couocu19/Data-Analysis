import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#分析拟南芥每条染色体上的不同类型的重复区域对应的数量分布直方图
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#画图部分
#sns.displot(df["length"],bins=500,kde=True)
#sns.displot(df1["length"],bins=500,kde=True)
df2 = pd.read_table("ab-15-onlyrpt.bed",header=None,delimiter='\t',names=['chrSeq','start','end','chrName','RepeatTypes'])
#sns.set_palette([sns.color_palette("PuBu",n_colors=10)[5]]) #颜色,官网有很多例子
#plt.rcParams["font.sans-serif"] = ["SimHei"]
#plt.rcParams["axes.unicode_minus"] = False
#sns.countplot(x="ChrSeq",hue="RepeatTypes",data=df)
#sns.displot(df["RepeatTypes"],kde=False,bins=30)
#plt.xticks(rotation=45)  #设置横坐标倾斜展示
#plt.legend()
#plt.show()


#获取某一列为指定值的行
# saUnKnown = df[df['RepeatTypes'] == 'LTR/Cassandra']
# print(saUnKnown)

#获取不确定重复序列类型的数量（LINE?,DNA?,SINE/tRNA?）
# lineCount = (df['RepeatTypes'] == 'LINE?').value_counts()[True]
# DNACount = (df['RepeatTypes'] == 'DNA?').value_counts()[True]
# stCount = (df['RepeatTypes'] == 'SINE/tRNA?').value_counts()[True]
# rcCount = (df['RepeatTypes'] == 'LTR/Cassandra').value_counts()[True]
# print(lineCount)
# print(DNACount)
# print(stCount)
# print(rcCount)

#把整个表格按照重复序列类型进行分类
# 获取表格的总行数
# print(df.shape[0])
#group_df = df.groupby('RepeatTypes').size().reset_index(name = 'count')
# print(group_df)


#读取重复序列类型与其它区域的整合文件并消除异常值
#df1 = pd.read_table("repeatSort.bed",header=0)
#print(df1)
print('------------------------------------------------------------------')
#df2 = df1[df1['start'] < df1['end']]
#合并相同超类的行，最后将合并为8个类型：
dna_replace_dict = {'DNA':'DNA transposons','DNA/CMC-EnSpm':'DNA transposons','DNA/MULE-MuDR':'DNA transposons','DNA/PIF-Harbinge':'DNA transposons','DNA/TcMar-Marine':'DNA transposons','DNA/TcMar-Pogo':'DNA transposons','DNA/TcMar-Stowaw':'DNA transposons','DNA/hAT':'DNA transposons','DNA/hAT-Ac':'DNA transposons','DNA/hAT-Charlie':'DNA transposons','DNA/hAT-Tag1':'DNA transposons','DNA/hAT-Tip100':'DNA transposons','DNA?':'DNA transposons','RC/Helitron':'DNA transposons','Retroposon':'DNA transposons','Retroposon/L1-de':'DNA transposons'}
df2.loc[:,'RepeatTypes'] = df2['RepeatTypes'].replace(dna_replace_dict)

line_replace_dict = {'LINE/L1':'LINE','LINE?':'LINE'}
df2.loc[:,'RepeatTypes'] = df2['RepeatTypes'].replace(line_replace_dict)

ltr_replace = {'LTR/Cassandra':'LTR','LTR/Copia':'LTR','LTR/Gypsy':'LTR'}
df2.loc[:,'RepeatTypes'] = df2['RepeatTypes'].replace(ltr_replace)

sine_replace = {'SINE/tRNA':'SINE','SINE/tRNA?':'SINE'}
df2.loc[:,'RepeatTypes'] = df2['RepeatTypes'].replace(sine_replace)

sa_replace = {'Satellite':'Satellite','Satellite/centr':'Satellite'}
df2.loc[:,'RepeatTypes'] = df2['RepeatTypes'].replace(sa_replace)

rna_replace = {'rRNA':'RNA','snRNA':'RNA','tRNA':'RNA'}
df2.loc[:,'RepeatTypes'] = df2['RepeatTypes'].replace(rna_replace)

group_df = df2.groupby('RepeatTypes').size().reset_index(name = 'count')
print(group_df)


# 将处理后的 DataFrame 对象保存到新的文件中
df2.to_csv('ab-15-onlyrpt-sml.bed', sep='\t', index=False)
#print(df1)


#plt.show()
