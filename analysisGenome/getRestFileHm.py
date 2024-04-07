import pandas as pd

# 读取文件1和文件2中的数据
with open('C:\\Users\\couco\\Desktop\\hm-list.txt', 'r') as file1:
    data_file1 = file1.read().splitlines()

with open('C:\\Users\\couco\\Desktop\\assembly_result.txt', 'r') as file2:
    data_file2 = file2.read().splitlines()

# 处理文件1中的数据
for i, line in enumerate(data_file1):
    split_values = line.split('.')
    if len(split_values) > 0:
        new_value = split_values[0]
        data_file1[i] = new_value
        #print(data_file1[i])

# 处理文件1中的数据并查找重复值
seen_values = set()
duplicate_values = set()
for i, line in enumerate(data_file1):
    split_values = line.split('.')
    if len(split_values) > 0:
        new_value = split_values[0]

        if new_value in seen_values:
            duplicate_values.add(new_value)
        else:
            seen_values.add(new_value)

        data_file1[i] = new_value

# 输出重复值
print("文件1中的重复值:")
for value in duplicate_values:
    print(value)




# 找到文件1中的哪一行对应的值在文件2中的每一行都找不到，并打印输出
not_found_values = []
for value in data_file1:
    found = False
    for line in data_file2:
        if value in line:
            #print(value+' '+line)
            found = True
            break
    if not found:
        not_found_values.append(value)

# 输出找不到的值
print("文件1中的值在文件2中找不到的值:")
for value in not_found_values:
    print(value)
