import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

# 读取文件
# with open("E:\\pangenome\\arab\\SR\\SR_types.txt", 'r') as file:
#      data = file.readlines()

# data = pd.read_table("E:\\pangenome\\arab\\SR\\SR_types.txt",sep='\t',header=None)
#
# unique_types = []
#
# for line in data:
#     parts = line.split('\t')
#     print(parts)
#     values = parts[4].strip().split(',')
#     unique_values = set(values)
#     with open("E:\\pangenome\\arab\\SR\\SR_types_uniqType_all.txt", 'a') as file:
#       if len(unique_values) == 1:
#        file.write(parts[0]+"\t"+parts[1]+"\t"+parts[2]+"\t"+values[0]+'\n')
#       else:
#        file.write(parts[0]+"\t"+parts[1]+"\t"+parts[2]+"\t"+"MIX_TYPES"+'\n')
#          unique_types.extend(unique_values)
#
# num_unique_types = len(set(unique_types))
# print(f"总共有{num_unique_types}种不同类型的值。")


# 处理文件内容
# processed_lines = []
# for line in data:
#     parts = line.split('\t')
#     col_four = parts[4].strip().split(',')
#     dup_count = col_four.count('DUP')
#     inv_count = col_four.count('INV')
#     trans_count = col_four.count('TRANS')
#     ins_count = col_four.count('INS')
#     del_count = col_four.count('DEL')
#     new_line = f"{dup_count}\t{inv_count}\t{trans_count}\t{ins_count}\t{del_count}\n"
#     processed_lines.append(new_line)

#将处理后的内容写入新文件
# with open("E:\pangenome\arab\SR\SR_types_count.txt", 'w') as file:
#    for line in processed_lines:
#        file.write(line)

df = pd.read_table("E:\\pangenome\\arab\\SR\\SR_types_count.txt",header=1,sep='\t',names=['DUP','INV','TRANS','INS','DEL'])

value_counts = pd.DataFrame({col: df[col].value_counts().reindex(range(33), fill_value=0) for col in df.columns})
print(value_counts)



####绘制SR类型数量折线图
plt.figure(figsize=(12, 6))
# x_data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
# #DUP = [1925, 2559, 2525, 2706, 2568, 2651, 2334, 2322, 2489, 2588, 66, 2494, 2521, 2593, 2533, 2486, 2477, 2861, 3124, 2624, 3012, 2987, 3219, 2761, 3057, 2747, 2487, 2522, 2634, 2267, 2919, 2070, 2070]
# #INV = [32, 50, 45, 53, 45, 45, 39, 39, 30, 44, 1, 43, 53, 40, 48, 49, 48, 51, 64, 41, 55, 62, 62, 61, 60, 51, 39, 49, 59, 46, 43, 36, 36]
# #TRANS = [491, 587, 624, 637, 631, 706, 571, 497, 611, 654, 4, 610, 647, 669, 634, 689, 530, 717, 913, 655, 816, 826, 918, 687, 787, 750, 596, 632, 722, 531, 791, 506, 506]
# #DEL = [733, 939, 818, 843, 964, 868, 867, 827, 827, 957, 2, 873, 873, 885, 816, 755, 856, 1049, 1035, 961, 1009, 1182, 969, 1083, 1048, 983, 834, 879, 918, 793, 824, 758, 758]
# DUP=[4255, 3842, 3479, 3545, 3668, 3578, 4115, 4207, 4956, 3779, 3666, 3426, 3567, 3722, 3628, 3390]
# INV = [55,  55,  47,  50,  55,  64,  61,  49,  39,  51,  60,  61,  54,  54,  57,  53]
# TRANS = [463,  437,  444,  420,  430,  461,  422,  425,  500,  431,  465,  489,  454,  442,  412,  432]
# DEL = [ 3331,  3289,  3237,  3454,  3434,  3317,  3442,  3444,  2773,  3354,  3465,  3316,  3336,  3241,  3416,  3318]
#
# plt.plot(DUP)
# plt.plot(INV)
# plt.plot(TRANS)
# plt.plot(DEL)
# plt.xticks(range(1,17))
# #plt.xlabel(x_data)
#
#
plt.plot(value_counts['DUP'])
plt.plot(value_counts['INV'])
plt.plot(value_counts['TRANS'])
plt.plot(value_counts['DEL'])
# # #plt.bar(x=x_data,height=value_counts['DUP'])
# # #plt.bar(x=x_data,height=value_counts['INV'])
# # #plt.bar(x=x_data,height=value_counts['TRANS'])
# # #plt.bar(x=x_data,height=value_counts['DEL'])
plt.legend(['DUP','INV','TRANS','DEL'])
# # #sn.displot(df,x='DUP',hue='DUP')
# # #sn.displot(df,bins=32)
# # # 绘制折线图
# # #
# #
plt.xlabel('SR Count')
plt.ylabel('Region count')
# # plt.title('Mutation Counts')
#
# # plt.grid(True)
# # plt.show()
#
plt.show()


