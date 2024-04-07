import pandas as pd

#df = pd.read_table("E:\\complete-gene-ann\\gff\\findNewGene\\arab\\ab-NewGene.txt",header=None,names=['chrName','type','start','end','geneName'])
#df = pd.read_table("E:\\complete-gene-ann\\gff\\findNewGene\\mouse\\ms-NewGene.txt",header=None,names=['chrName','type','start','end','geneName'])
df = pd.read_table("E:\\complete-gene-ann\\gff\\findNewGene\\human\\hm-NewGene.txt",header=None,names=['chrName','start','end','type','geneName'])

df['genLen'] = df['end'] - df['start']
print(df['genLen'].mean())