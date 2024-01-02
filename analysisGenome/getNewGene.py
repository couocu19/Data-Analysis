import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# 读取新基因组注释文件
df = pd.read_csv("E:\\complete-gene-ann\\gff\\findNewGene\\arab\\abnew-gene-sml-2.txt", sep="\t", header=None)
#df = pd.read_csv("E:\\complete-gene-ann\\gff\\findNewGene\\human\\hmnew-gene-sml.txt", sep="\t", header=None)
#print(df[4])
#df[4] = df[4].str.extract(r"(=[^;]*)")
#df[4] = df[4].str.replace('=', '')
#df[4] = df[4].str.extract(r"(gene_id[^;]*)")
#df[4] = df[4].str.replace('"', '')
#df[4] = df[4].str.extract(r'(AT[^"]*)')
#print(df[4])
#df[4] = df[4].str.slice(0, 1)
#写回到文件
#df[4].to_csv("E:\\complete-gene-ann\\gff\\findNewGene\\human\\hmnew-gene-sml-1.txt", sep="\t", index=False, header=None)

#读取老基因组注释文件
df1 = pd.read_csv("E:\\complete-gene-ann\\gff\\findNewGene\\arab\\abold-gene-sml-2.txt", sep="\t", header=None)
#df1 = pd.read_csv("E:\\complete-gene-ann\\gff\\findNewGene\\human\\hmold-gene-sml.txt", sep="\t", header=None)
# df1[4] = df1[4].str.extract(r"(ID=[^;]*)")
# df1[4] = df1[4].str.extract(r"(-[^;]*)")
# df1[4] = df1[4].str.replace('-', '')
#df1.to_csv("E:\\complete-gene-ann\\gff\\findNewGene\\abold-gene-sml-2.txt", sep="\t", index=False, header=None)
#统计新老基因组中相同的基因，即共有的基因
# 使用 merge 函数将两个 DataFrame 按第 5 列进行匹配

merged_df = pd.merge(df, df1, on=df.columns[4])
#merged_df.to_csv("E:\\complete-gene-ann\\gff\\findNewGene\\ab-commonGene.txt", sep="\t", index=False, header=None)
# 找到新基因组中独有的基因
# 在这段代码中，isin 函数用于判断 A 文件的第 5 列是否存在于 B 文件的第 5 列中，并返回一个布尔值的 Series。
# 然后，使用逻辑取反符号 ~，筛选出不匹配的行，得到一个新的 DataFrame filtered_df。最后，通过打印 filtered_df 来查看结果。
# 先获取所有相同值得行
matched_rows = merged_df[df.columns[4]]
#print(matched_rows)
filtered_df = df[~df[df.columns[4]].isin(matched_rows)]
#filtered_df.to_csv("E:\\complete-gene-ann\\gff\\findNewGene\\ab-NewGene.txt", sep="\t", index=False, header=None)

column_5_values = set(df1[df1.columns[4]].unique())
column_5_values1 = set(df[df.columns[4]].unique())
print(len(column_5_values))
print(len(column_5_values1))
#求平均每个基因延长了多少碱基
# 计算差值 L1 和 L2
L1 = merged_df.iloc[:, 3] - merged_df.iloc[:, 2]  # 左右第三列和第二列的差值
L2 = merged_df.iloc[:, 8] - merged_df.iloc[:, 7]  # 第9列和第8列的差值
#print(L2)
# 计算 L2 和 L1 的所有差值
L_diff = []
i = 0
while i < len(L1) :
    diff= L1[i] - L2[i]
    i = i+1
    L_diff.append(diff)

merged_df["diff"] = L_diff


#for l1
#print(L_diff)
#添加到merged_df中
#merged_df.insert(9, "L_diff", L_diff)
#merged_df.to_csv("E:\\complete-gene-ann\\gff\\findNewGene\\ab-commonGene.txt", sep="\t", index=False, header=None)
#提取第 10 列数据
column_10 = merged_df.iloc[:, 9]
# 计算平均值
average = column_10.mean()

#中位值
mdn = column_10.median()
# 计算最大值
maximum = column_10.max()
max_gene = merged_df[merged_df.iloc[:, 9] == maximum]
print(max_gene)

# 计算最小值
minimum = column_10.min()
# 统计大于 0 的行数
rows_greater_than_0 = len(column_10[column_10 > 0])
positive = column_10[column_10 > 0]
positive_mean = positive.mean()

# 统计小于 0 的行数
rows_less_than_0 = len(column_10[column_10 < 0])
negative = column_10[column_10 < 0]
negative_mean = negative.mean()

print("平均值:", average)
print("最大值:", maximum)
print("最小值:", minimum)
print("中位数:", mdn)
print("大于0的行数:", rows_greater_than_0)
print("小于0的行数:", rows_less_than_0)
print("大于0的行数中第10列的平均值:", positive_mean)
print("小于0的行数中第10列的平均值:", negative_mean)