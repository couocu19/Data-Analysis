import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#绘制五个基因组的分组基本信息柱状图
def basic_info():
    # 设置全局字体以及大小
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 15
    df = pd.read_table("basic.csv")
    type = df['type']
    #创建两个图层对象
    fig, ax = plt.subplots()
    #fig=plt.figure(dpi=600)
    #ax=fig.add_subplot(111)
    # 准备左边数据
    left = df[df['species'].isin(['Homo sapiens', 'Mus musculus'])]
    sns.barplot(x="species", y="size(Mb)", hue="type", data=left, ax=ax, dodge=True, width=0.8,palette=['#7dabcf', '#fbc1ad'])
    #ax.bar(x="species", y="size(Mb)", hue="type", data=left, ax=ax, dodge=True, width=0.8,palette=['#7dabcf', '#fbc1ad'])

    # 右侧刻度尺 即ax1
    right_ax = ax.twinx()
    # 准备右边数据
    right = df[df['species'].isin(['Arabidopsis thaliana', 'Musa acuminata', 'Fragaria vesca'])]
    sns.barplot(x="species", y="size(Mb)", hue="type", data=right, ax=right_ax, dodge=True, width=0.8,palette=['#7dabcf', '#fbc1ad'])

    # 设置左右y轴范围
    y_max = max(left['size(Mb)'].max(), right['size(Mb)'].max())
    ax.set_ylim([0, y_max])
    right_ax.set_ylim([0, y_max])

    # 调整第一个图例的位置
    ax.legend(bbox_to_anchor=(0.7, 1.15), loc=2, borderaxespad=0.)

    # 设置x轴标签
    ax.set_xlabel('')

    # 设置左右y轴标签
    ax.set_ylabel('Size (Mb)', color='#7dabcf')
    right_ax.set_ylabel('Size (Mb)', color='#fbc1ad')

    # 设置左右y轴刻度颜色
    ax.tick_params(axis='y', labelcolor='#7dabcf')
    right_ax.tick_params(axis='y', labelcolor='#fbc1ad')

    # 设置x轴刻度位置
    ax.set_xticklabels(['Homo sapiens', 'Mus musculus', 'Arabidopsis thaliana', 'Musa acuminata', 'Fragaria vesca'],
                       rotation=30, ha='right')

    # 设定轴标签和图例
    #ax.set_ylabel('Size (Mb)')
    #right_ax.set_ylabel('Size (Mb)')
    #ax.set_xlabel('')
    #ax.legend(title='Type')

    #ax  = sns.barplot(data=df,x="name",y="size(Mb)",hue="species",dodge=0,width=0.8,palette=['#7dabcf', '#cfe7eb','#fbc1ad','#f46e49','#e5e1e0'])
    #ax = sns.barplot(data=df, x="species", y="size(Mb)", hue="type", dodge=True, width=0.8, palette=['#7dabcf','#fbc1ad'])
    #设置柱子上方显示值
    # for i,v in enumerate(df['size(Mb)']):
    #    ax.text(v+110,i,type[i],ha = 'center',color='gray')
    # 设置坐标轴边框线的颜色
    #ax.spines['top'].set_color('#666666')
    #ax.spines['right'].set_color('#666666')
    #ax.spines['bottom'].set_color('#666666')
    #ax.spines['left'].set_color('#666666')
    #设置字体
    #sns.set(font='Times New Roman')
    #sns.set(font_scale=4)
    #plt.ylabel('')  #设置y轴名称不显示

    #plt.xlabel('')
    #plt.xlim(-100,5000) #设置x轴显示的范围
    #plt.ylim(-100, 3500)
    #设置字体的整体颜色
    #设置坐标轴标签颜色
    #ax.tick_params(axis='x', colors='#666666')
    #ax.tick_params(axis='y', colors='#666666')
    #设置图的边框不显示
    #sns.despine(left=False, bottom=False,top=True,right=True)
    #调整整个图的大小比例
    #plt.subplots_adjust(top=0.8, bottom=0.3, left=0.25, right=0.683)
    plt.show()




if __name__ == '__main__':
    basic_info()
