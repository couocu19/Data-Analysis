import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("D:\python-study\DataAnalysis\data\HR.csv")
df=df[df["last_evaluation"]<=1][df["salary"]!="nme"][df["department"]!="sale"] #去除异常值

#改变样式
sns.set_style(style="whitegrid")
sns.set_context(context="poster",font_scale=0.5) #字体
sns.set_palette(sns.color_palette("RdBu",n_colors=7)) #颜色,官网有很多例子

#sns.countplot(x="salary",hue="department",data=df)

#绘制直方图

# plt.title("SALARY")
# plt.xlabel("salary")
# plt.ylabel("Number")
# plt.xticks(np.arange(len(df["salary"].value_counts()))+0.5,df["salary"].value_counts().index)
# plt.axis([0,4,0,10000])
# plt.bar(np.arange(len(df["salary"].value_counts()))+0.5,df["salary"].value_counts(),width=0.5)
# #显示每一列上具体的值
# for x,y in zip(np.arange(len(df["salary"].value_counts()))+0.5,df["salary"].value_counts()):
#     plt.text(x,y,y,ha="center",va="bottom")
#绘制直方图
# f = plt.figure()
# f.add_subplot(1,3,1)
# sns.displot(df["satisfaction_level"],bins=10,kde=True)  #hist/ked,分别代表直方图和分布图的显示问题
#
# f.add_subplot(1,3,2)
# sns.displot(df["last_evaluation"],bins=10,kde=True)
#
# f.add_subplot(1,3,3)
# sns.displot(df["average_monthly_hours"],bins=10,kde=True)

#BOX PLOT 箱线图
#sns.boxplot(x=df["time_spend_company"],saturation=0.75,whis=3)

#绘制折线图
#求随着员工在公司待的时间长短，员工的离职情况的变化率，首先需要按照员工在公司待的时间进行分类，其次需要对其中的每列属性求均值，包括离职率

# sub_df=df.groupby("time_spend_company").mean()
# #sns.pointplot(x=sub_df.index,y=sub_df["left"])  #y将每一组中的离职率提取出来
# sns.pointplot(x="time_spend_company",y="left",data=df)  #另一种写法 #todo:这里的left值是会自动算成均值吗？

#饼图 pie  todo:优化
lbs=df["salary"].value_counts().index
#explodes=[0,0.1,0]
explodes=[0.1 if i=="low" else 0 for i in lbs] #设置分离块
plt.pie(df["salary"].value_counts(normalize=True),labels=lbs,explode=explodes,autopct="%.1f%%")

#



plt.show()
