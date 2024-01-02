import pandas as pd
#统计每个代表染色体上的新区域上的主要重复类型是啥

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_table("E:\\complete-gene-ann\\rpt-all-repre-chr\标准化后\\NR-hm-15-retr-std.bed",header=None,delimiter='\t',names=['1','2','3','4','5'])
#DNA transposons,LTR,LINEs,SINEs,Simple_repeat,Satellite,Small RNA,Low_complexity,Unclassified
rpt_tpes = ['DNA transposons','LTR','LINE','SINE','Simple_repeat','Satellite','RNA','Low_complexity','Unclassified']
rpt_lns = []
df = df[df['4']=='homo-chr15']

leng=0
i=0
for a in rpt_tpes:
    leng=0
    for index, row in df[df['5'] == a].iterrows():
        diff = row['3'] - row['2']
        leng = leng + diff
    rpt_lns.append(leng)

filled_ratio= [0.0852,0.1615,0.0497,0.0826,0.0899,0.2866,0.0329]
for a in rpt_lns:
    print(a/filled_ratio[1])

