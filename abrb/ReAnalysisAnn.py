import pandas as pd
import csv

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#拟南芥
#df = pd.read_table("newann-athve.bed",header=None,names=['chrName', 'start', 'end' ,'annTypes'])
#人类
#df = pd.read_table("E:\\complete-gene-ann\\human\\hmnew-sml-gff.bed",header=None,names=['chrName', 'start', 'end' ,'annTypes'])
#人类新区域上的新基因区域
#df = pd.read_table("E:\\complete-gene-ann\\human\\hm-NewAndAnn.bed",header=None,names=['chrName', 'start', 'end' ,'annTypes'])

#香蕉
#df = pd.read_table("E:\\complete-gene-ann\\banana-香蕉\\new\\bn-gff-sml.bed",header=None,names=['chrName', 'start', 'end' ,'annTypes'])
df = pd.read_table("E:\\complete-gene-ann\\banana-香蕉\\l5000\\bn-NewAndAnn.bed",header=None,names=['chrName', 'start', 'end' ,'annTypes'])
#澳洲胡桃
##

#print(df.shape[0])
#去除重复列
#DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
#subset设置为None的时候，默认所有列，意思是所有列同时（即：完全一样的两行）为重复的时候才删除
#df1 = df.drop_duplicates(subset=None, keep='first', inplace=False)
#print(df1.shape[0])
#res = df[df['annTypes'] == 'region']
#print(res)
#整体看基因信息
#fdg = df.groupby('annTypes').size().reset_index(name = 'count')
#print(fdg)
#print("==============================================")


#df1 = df[df['annTypes'] != 'region']
#df1.to_csv('hm-gff-remove-region.bed', sep='\t', index=False)

#以染色体为单位分析
# dfcpl_all_gp = df.groupby('chrName')
# for gp_name,gp_data in dfcpl_all_gp:
#     gp_df = pd.DataFrame(gp_data)
#     b = gp_df.groupby('annTypes').size().reset_index(name = 'count')
#     print(b)
#     print("------------------------------------------------")

#重新计算新区域上的基因信息
#dfcpl =  pd.read_table("new-ann-426.csv")
#fdg1 = dfcpl.groupby('annTypes').size().reset_index(name = 'count')
#print(fdg1)
#dfcpl_gp = dfcpl.groupby('chrName')
#for gp_name,gp_data in dfcpl_gp:
#    gp_df = pd.DataFrame(gp_data)
#    b = gp_df.groupby('annTypes').size().reset_index(name = 'count')
    #print(b)

#合并完全相同的区域对应的基因类型
#grouped = df1.groupby(['chrName','start', 'end'])  #先按照start和end进行分组
#merged_col = grouped['annTypes'].apply(lambda x: ','.join(x)).reset_index() #合并每个分组
#merged_df = pd.merge(df.drop('annTypes', axis=1), merged_col, on=['chrName','start', 'end']).drop_duplicates() #将合并后的分组和原表格合并
#merged_df.to_csv('naatv_merty.csv', sep='\t',index=False)
#mgf = merged_df.groupby('annTypes').size().reset_index(name = 'count')
#print(mgf)

#df1.to_csv('naatv_dropdup.csv', sep='\t', index=False)
#将表格按照注释区域的类型进行分类
#处理求了交叉区域后的注释区域中新基因的分组信息
df2 = pd.read_table("new-ann-425-1.csv")
#将表格按照注释区域的类型进行分类
group_df = df2.groupby('annTypes').size().reset_index(name = 'count')
print(group_df)

#再处理一次自己注释的文件信息
#df_own = pd.read_table("newAnnFun.bed",header=None,names=['chrName', 'start', 'end' ,'annTypes'])
#print(df_own.shape[0])
#去除重复列
#df_own1 = df_own.drop_duplicates(subset=None, keep='first', inplace=False)
#print(df_own1.shape[0])
#df_own1.to_csv('na_own_dropdup.csv', sep='\t', index=False)
#去除所有类型值为similarity的行
#df_own1 = df_own1[df_own1['annTypes']!='similarity']
#df_own1.to_csv('naow_ddup_dsi.csv', sep='\t', index=False)
#print(df_own1.shape[0])
