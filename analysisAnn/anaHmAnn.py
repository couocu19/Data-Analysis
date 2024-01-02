import pandas as pd

df = pd.read_table("mssml-ann.bed", header=None, delimiter='\t', names=['chrName', 'start', 'end', 'annTypes', 'annInfo'])

#cds  结果：130369
# cd_df = df[df['annTypes'] =='CDS']
# print(cd_df.shape[0])
# set = set()
# for index,row in cd_df.iterrows():
#     idcol = row['annInfo']
#     idlist = idcol.split(";")
#     set.add(idlist[0])
# print(len(set))
# print(set)

#gene
# gene_df = df[df['annTypes'] =='gene']
# print(gene_df.shape[0])
# set = set()
# for index,row in gene_df.iterrows():
#     idcol = row['annInfo']
#     idlist = idcol.split(";")
#     set.add(idlist[0])
# print(len(set))
#print(set)

#mRNA
# gene_df = df[df['annTypes'] =='mRNA']
# print(gene_df.shape[0])
# set = set()
# for index,row in gene_df.iterrows():
#     idcol = row['annInfo']
#     idlist = idcol.split(";")
#     set.add(idlist[0])
# print(len(set))

#exon
ex_df = df[df['annTypes'] =='exon']
print(ex_df.shape[0])
set = set()
for index,row in ex_df.iterrows():
    idcol = row['annInfo']
    idlist = idcol.split(";")
    set.add(idlist[0])
print(len(set))

#protein(统计同等的注释类型)


