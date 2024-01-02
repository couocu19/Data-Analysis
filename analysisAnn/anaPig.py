import pandas as pd


#猪的全基因组
#df = pd.read_table("pgsmlann.bed", header=None, delimiter='\t', names=['chrName', 'start', 'end', 'annTypes', 'annInfo'])
#猪的新区域
df = pd.read_table("E:\\complete-gene-ann\\pig\\pglasted\\pgnew-NAsml.bed", header=None, delimiter='\t', names=['chrName', 'start', 'end', 'annTypes'])
#exon
#统计时遇到的问题：exon的个数应该以exonId的数量为主还是parentID为主？
ex_df = df[df['annTypes'] =='gene']
print(ex_df.shape[0])
set = set()
#for index,row in ex_df.iterrows():
 #   idcol = row['annInfo']
 #   idlist = idcol.split(";")
 #   set.add(idlist[0])
#print(len(set))
#cds
#mRNA
#gene

#统计小鼠全基因组
#df = pd.read_table("E:\\complete-gene-ann\\\Mouse\\ms-ann1.bed", header=None, delimiter='\t', names=['chrName', 'start', 'end', 'annTypes'])
#统计新区域上的注释信息
# df = pd.read_table("E:\\complete-gene-ann\\\Mouse\\ms-NA.bed", header=None, delimiter='\t', names=['chrName', 'start', 'end', 'annTypes'])
# ex_df = df[df['annTypes'] =='gene']
# print(ex_df.shape[0])

#统计猪的旧基因组
# df = pd.read_table("pg-old-sml.bed", header=None, delimiter='\t', names=['chrName','annTypes', 'annInfo'])
# #exon
# #统计时遇到的问题：exon的个数应该以exonId的数量为主还是parentID为主？
# ex_df = df[df['annTypes'] =='CDS']
# print(ex_df.shape[0])
# set = set()
# for index,row in ex_df.iterrows():
#     idcol = row['annInfo']
#     idlist = idcol.split(";")
#     set.add(idlist[0])
# print(len(set))