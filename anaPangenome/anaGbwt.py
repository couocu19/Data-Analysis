import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# 读取表格数据
df = pd.read_csv('E:\\pangenome\\musa\\Musaceae_pangenome.min_1K.v2.fasta.fai', sep='\t', header=None)

# 分割第一列并创建新列
df[5] = df[0].str.split('_').str[0]
#for index, row in df.iterrows():
#    print(row)
#print(df)

# 按照新列分组，并计算第二列之和
result = df.groupby(5)[1].sum()
result1 = df.groupby(5).size().reset_index(name = 'count')
print(result)
print('-------------------------------------------')
print(result1)


# 添加错误处理机制
def get_group(x):
    try:
        #return '_'.join(x.split("#")[:2])
        return '_'.join(x)
    except IndexError:
        return None

# 计算每组的Value总和
#df['Group'] = df['1'].apply(get_group)
#分组，然后计算每个分组的总大小
#df_group = df.groupby(['Group'], as_index=False)

# 遍历每个分组
# for name, group in df_group:
#    # if(name == 'HG00438_1'):
#     #    print(group)
#     print('Group:', name)
#     print(group)
#df_grouped = df.groupby(['Group'], as_index=False).agg({'Value': 'sum'})
#sum_value = df_grouped.iloc[:20, 1].sum()
#print(sum_value)
# 输出分组数据
#print(df_group)