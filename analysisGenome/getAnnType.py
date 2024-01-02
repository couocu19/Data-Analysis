import pandas as pd


df = pd.read_table("E:\\complete-gene-ann\\Arab\\Col-CEN_v1.2_genes.araport11.gff3\\Col-CEN-15.gff3",sep = "\t",header=None,names=['1','2','3','4','5','6','7','8','9'])

#df_filtered = df[~df['1'].isin(['ChrC', 'ChrM'])]
#df_filtered.to_csv('E:\\complete-gene-ann\\Arab\\Col-CEN_v1.2_genes.araport11.gff3\\Col-CEN-sort-15.gff3',sep='\t', index=False,header=False)

#for a in df:
 #   a[9] = a[9][1:]

#替换gene_id 为ID
#df["9"] = df["9"][1:]

df["9"] = df["9"].str.replace("gene_id ", "ID=")
df["9"] = df["9"].str.replace('transcript_id \"', "ID=")
df["9"] = df["9"].str.replace('"', '')
#df["9"] = df["9"].str.replace(' ID \"', "exon_id=")
#df["9"] = df["9"].str.replace("gene_id ", "ID=")

# 保存处理后的表格到本地文件
df.to_csv("E:\\complete-gene-ann\\Arab\\Col-CEN_v1.2_genes.araport11.gff3\\Col-CEN-15-ID.gff3", sep="\t", index=False,header=None)



#读取新区域上的注释文件
#df = pd.read_table("E:\\complete-gene-ann\\gff\\getAnnAreas\\hm\\ms-NA.bed",sep = "\t",header=None,names=['chrseq','start','end','ann-types'])
#统计注释类型
#group_df = df.groupby('ann-types').size().reset_index(name = 'count')
#print(group_df)
