import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_table("E:\\complete-gene-ann\\f.vesca-草莓\\Fragaria_vesca_v4.0a2_genome.gff3", header=None, delimiter='\t', names=['1','2','3','4','5','6','7','8','9'])
#df = pd.read_table("E:\\complete-gene-ann\\Arab\\Col-CEN_v1.2_genes.tair10.gff3\\Col-CEN_v1.2_genes.tair10.gff3", header=None, delimiter='\t', names=['1','2','3','4','5','6','7','8','9'])

#df = df[df['1']!='NC_012920.1']

#df = df[~df['1'].str.startswith('NW_')]
#总体查看所有注释类型的数量
#group_df = df.groupby('1').size().reset_index(name = 'count')
#print(group_df)

#df1 = df[(df['annTypes'] == 'five_prime_UTR') | (df['annTypes'] == 'three_prime_UTR') | (df['annTypes'] == 'CDS') | (df['annTypes'] == 'exon')]
#df1.to_csv("E:\\pangenome\\arab\\col_ann_4types.txt",header=None,sep='\t',index=False)

#准确求染色体上exon的数量 最后结果：314729
# exon_df = df[(df['annTypes']=='exon')]
# print(exon_df.shape[0])
# exon_set = set()
# for index,row in exon_df.iterrows():
#     if((row['chrName'] == 'ChrC') | (row['chrName'] == 'ChrM')):
#         exon_set.add(row['annInfo'])
#         continue
#     idcol = row['annInfo']
#     idlist = idcol.split(";")
#     #print(idlist[3])
#     if idlist[3] in exon_set:
#         print(row)
#         continue
#     exon_set.add(idlist[3])
#准确求所有染色体上gene的数量 最后结果：33296
# gene_df = df[(df['annTypes']=='gene')]
# print(gene_df.shape[0])
# exon_set = set()
# for index,row in gene_df.iterrows():
#     idcol = row['annInfo']
#     idlist = idcol.split(";")
#     if ((row['chrName'] == 'ChrC') | (row['chrName'] == 'ChrM')):
#         exon_set.add(idlist[0])
#         continue
#     if idlist[1] in exon_set:
#         #print(row)
#         continue
#     exon_set.add(idlist[1])
# print(len(exon_set))

#准确求所有染色体上mRNA的数量 最后结果：48310
# mRNA_df = df[(df['annTypes']=='mRNA')]
# print(mRNA_df.shape[0])
# exon_set = set()
# for index,row in mRNA_df.iterrows():
#     idcol = row['annInfo']
#     idlist = idcol.split(";")
#     #if ((row['chrName'] == 'ChrC') | (row['chrName'] == 'ChrM')):
#      #   exon_set.add(idlist[0])
#       #  continue
#     if idlist[0] in exon_set:
#         print(row)
#      #   continue
#     exon_set.add(idlist[0])
# print(len(exon_set))

#准确求所有染色体上protein的数量 最后结果：48310
# pt_df = df[(df['annTypes']=='protein')]
# print(pt_df.shape[0])
# exon_set = set()
# for index,row in pt_df.iterrows():
#     idcol = row['annInfo']
#     idlist = idcol.split(";")
#     if ((row['chrName'] == 'ChrC') | (row['chrName'] == 'ChrM')):
#        exon_set.add(idlist[0])
#        continue
#
#     exon_set.add(idlist[3])
# print(len(exon_set))

#准确求所有染色体上cds的数量 最后结果：
cd_df = df[(df['3']=='mRNA')]
print(cd_df.shape[0])
exon_set = set()
for index,row in cd_df.iterrows():
    idcol = row['9']
    idlist = idcol.split(";")
#    if ((row['chrName'] == 'ChrC') | (row['chrName'] == 'ChrM')):
#       exon_set.add(idcol)
#       continue

    exon_set.add(idlist[0])
print(len(exon_set))