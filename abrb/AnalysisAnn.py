import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_table("newGeneAndAnn.csv",header=None,names=['chrName', 'start', 'end' ,'annTypes'])
print(df.shape[0])
#去除重复列
#DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
#subset设置为None的时候，默认所有列，意思是所有列同时（即：完全一样的两行）为重复的时候才删除
#df1 = df.drop_duplicates(subset=None, keep='first', inplace=False)
#print(df1.shape[0])
#df1.to_csv('newAnn_dropdup.csv', sep='\t', index=False)

#将表格按照注释区域的类型进行分类
group_df = df.groupby('annTypes').size().reset_index(name = 'count')
print(group_df)


#sns.set_style(style="whitegrid")
#sns.set_palette([sns.color_palette("PuBu",n_colors=10)[5]])
#绘制基因注释功能类型对应的数量分布直方图  displot
#sns.displot(df1["annTypes"],bins=10,kde=False)
#plt.ylim(0,40000)
#plt.title("Histogram of the distribution of the number of gene types annotated")
#plt.legend()
#plt.show()

#绘制每条染色体上的不同功能的注释基因的数量计数柱状图  countplot
#sns.countplot(x="chrName",hue = "annTypes",data = df1)
#plt.title("Statistical plot of the number of different kinds of genes detected on each chromosome")
#plt.legend()
#plt.show()

#合并每个区间的所有基因注释信息
#grouped = df1.groupby(['chrName','start', 'end'])  #先按照start和end进行分组
#merged_col = grouped['annTypes'].apply(lambda x: ','.join(x)).reset_index() #合并每个分组
#merged_df = pd.merge(df1.drop('annTypes', axis=1), merged_col, on=['chrName','start', 'end']).drop_duplicates() #将合并后的分组和原表格合并
#merged_df.to_csv('merged_type_data.csv', index=False)

#合并重复类型行
#合并相同超类的行，最后将合并为8个类型：
#replace_dict = {'gene,similarity,cds,exon':'cds,exon,gene,similarity','intron,cds,exon,gene,similarity ':'cds,exon,gene,similarity,intron','gene,similarity,intron,cds,exon':'cds,exon,gene,similarity,intron','intron,gene,similarity,cds,exon':'cds,exon,gene,similarity,intron','gene,similarity,cds,exon,intron':'cds,exon,gene,similarity,intron','cds,exon,intron,gene,similarity':'cds,exon,gene,similarity,intron','intron,gene,similarity':'gene,similarity,intron','splice3,splice5':'splice5,splice3','cds,exon,intron':'intron,cds,exon','intron,cds,exon,gene,similarity':'cds,exon,gene,similarity,intron'}
#merged_df.loc[:,'annTypes'] = merged_df['annTypes'].replace(replace_dict)
#可视化
#统计合并每个区域类型后不同类型的统计图
#sns.countplot(x="chrName",hue = "annTypes",data = merged_df)
#sns.displot(merged_df["annTypes"],kde = False,bins=12)
#merge_group = merged_df.groupby("annTypes").size().reset_index(name = 'counts')
#merge_group = merge_group.sort_values(by='counts', ascending=False) #按照counts排序
#print(merge_group)
#plt.xticks(rotation=45)
#plt.ylim(0,110000)
#plt.legend()
#plt.show()

#查看 splice3，splice5的区域
#res = merged_df[merged_df['annTypes'] == 'splice5,splice3']
#print(res)