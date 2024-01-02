import pandas as pd

df = pd.read_table("E:\\complete-gene-ann\\gff\\findNewGene\\human\\hm-IDandNme.txt",sep="\t",header=None)
#df2 = pd.read_table("E:\\complete-gene-ann\\gff\\findNewGene\\human\\hm-geneIDS.txt",header=None)

df[1] = df[1].fillna(df[0].str[2:])
#同时遍历两个表格
df[1].to_csv("E:\\complete-gene-ann\\gff\\findNewGene\\human\\hm-ID-full.txt",sep="\t",header=None,index=False)
#print(df)


# for row1, row2 in zip(df1, df2):
#     print("Table 1 row:", row1)
#     print("Table 2 row:", row2)
#     print()

    # 在这里可以进行进一步的操作或处理
    # ...

