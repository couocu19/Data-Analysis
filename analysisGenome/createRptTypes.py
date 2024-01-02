import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#处理人类数据 1号染色体和15号染色体
df1 = pd.read_table("E:\\complete-gene-ann\\rpt-all-repre-chr\\所有物种完整的重复序列\\人类\\hm-NR-all.bed",header=None,delimiter='\t',names=['chrseq','start','end','chrName','rpt-types'])

#df1 = df1[df1['chrseq'] != 'chrM']
#gp_df2 = df1.groupby('chrseq').size().reset_index(name = 'count')
#print(gp_df2)

#小鼠 删除chrseq为chrM的所有行



#把整个表格按照重复序列类型进行分类
# 获取表格的总行数
#print(df.shape[0])
group_df = df1.groupby('rpt-types').size().reset_index(name = 'count')
print(group_df)
print('----------------------------------')
#合并dna类型
dna_replace_dict = {'DNA':'DNA transposons','DNA/Crypton':'DNA transposons','DNA/Crypton-A?':'DNA transposons','DNA/Kolobok':'DNA transposons','DNA/MULE-MuDR':'DNA transposons','DNA/Merlin':'DNA transposons','DNA/PIF-Harbinger':'DNA transposons','DNA/PiggyBac':'DNA transposons','DNA/TcMar':'DNA transposons','DNA/TcMar-Mariner':'DNA transposons','DNA/TcMar-Pogo':'DNA transposons','DNA/TcMar-Tc1':'DNA transposons','DNA/TcMar-Tc2':'DNA transposons','DNA/TcMar-Tigger':'DNA transposons','DNA/TcMar?':'DNA transposons','DNA/hAT':'DNA transposons',
                    'DNA/hAT-Ac':'DNA transposons','DNA/hAT-Blackjack':'DNA transposons','DNA/hAT-Charlie':'DNA transposons','DNA/hAT-Tip100?':'DNA transposons','DNA/hAT?':'DNA transposons','DNA?':'DNA transposons','DNA?/PiggyBac?':'DNA transposons','DNA?/hAT-Tip100?':'DNA transposons','RC/Helitron':'DNA transposons','RC/Helitron?':'DNA transposons','RC?/Helitron?':'DNA transposons','DNA?/hAT?':'DNA transposons','DNA/hAT-Tag1':'DNA transposons','DNA/hAT-Tip100':'DNA transposons',
                    'DNA/Academ-1':'DNA transposons','DNA/CMC-EnSpm':'DNA transposons','DNA/Zisupton':'DNA transposons','PLE/Chlamys':'DNA transposons','PLE/Naiad':'DNA transposons','DNA/Kolobok-T2':'DNA transposons','DNA/IS3EU':'DNA transposons','DNA/PIF-Harbinge':'DNA transposons','DNA/TcMar-Marine':'DNA transposons','DNA/TcMar-Stowaw':'DNA transposons','DNA/hAT-hAT19':'DNA transposons','DNA/CMC-Transib':'DNA transposons','DNA/Maverick':'DNA transposons'};
df1.loc[:,'rpt-types'] = df1['rpt-types'].replace(dna_replace_dict)
#合并line Retroposon/RTE-derived
line_replace_dict = {'LINE/CR1':'LINE','Retroposon/L1-dep?':'LINE','Retroposon/L1-de':'LINE','Retroposon/RTE-derived':'LINE','LINE/Dong-R4':'LINE','LINE/I-Jockey':'LINE','LINE/L1':'LINE','LINE/L1-Tx1':'LINE','LINE/L2':'LINE','LINE/Penelope':'LINE','LINE/RTE-BovB':'LINE','LINE/RTE-X':'LINE','LINE/R1':'LINE','LINE/RTE':'LINE','LINE?':'LINE'}
df1.loc[:,'rpt-types'] = df1['rpt-types'].replace(line_replace_dict)
#合并sine
sine_replace = {'SINE/5S-Deu-L2':'SINE','SINE/Alu':'SINE','Retroposon/SVA':'SINE','SINE/MIR':'SINE','SINE/tRNA':'SINE','SINE/tRNA-Deu':'SINE','SINE/tRNA-RTE':'SINE','SINE/B2':'SINE','SINE/B4':'SINE','SINE/ID':'SINE','SINE/5S':'SINE','SINE/U-L1':'SINE','SINE/tRNA?':'SINE','SINE/U':'SINE',}
df1.loc[:,'rpt-types'] = df1['rpt-types'].replace(sine_replace)
#合并ltr
ltr_replace = {'LTR/ERV1':'LTR','LTR/ERVK?':'LTR','LTR/ERV1?':'LTR','LTR/ERVK':'LTR','LTR/ERVL':'LTR','LTR/ERVL-MaLR':'LTR','LTR/ERVL?':'LTR','LTR/Gypsy':'LTR','LTR/Gypsy?':'LTR','LTR?':'LTR','LTR/Copia':'LTR','LTR/Caulimovirus':'LTR','LTR/Cassandra':'LTR'}
df1.loc[:,'rpt-types'] = df1['rpt-types'].replace(ltr_replace)
#合并satellite
sa_replace = {'Satellite':'Satellite','Satellite/centr':'Satellite','Satellite/acro':'Satellite','Satellite/subtelo':'Satellite'}
df1.loc[:,'rpt-types'] = df1['rpt-types'].replace(sa_replace)
#合并other
other_replace = {'Unknown':'other','Unspecified':'other','Retroposon':'other'}
df1.loc[:,'rpt-types'] = df1['rpt-types'].replace(other_replace)
#合并small-rna
rna_replace = {'rRNA':'RNA','snRNA':'RNA','tRNA':'RNA','scRNA':'RNA','srpRNA':'RNA'}
df1.loc[:,'rpt-types'] = df1['rpt-types'].replace(rna_replace)
#
group_df = df1.groupby('rpt-types').size().reset_index(name = 'count')
print(group_df)

df1.to_csv('E:\\complete-gene-ann\\rpt-all-repre-chr\\所有物种完整的重复序列\\人类\\hm-NR-allSml.bed',sep='\t', index=False)