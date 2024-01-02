import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
         'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#create list for made up average temperatures
Avg_Temp = [35, 45, 55, 65, 75, 85, 95, 100, 85, 65, 45, 35]
#create list for made up average percipitation %
Avg_Percipitation_Perc = [.90, .75, .55, .10, .35, .05, .05, .08, .20, .45, .65, .80]
data = {'Month': Month,
        'Avg_Temp': Avg_Temp,
        'Avg_Percipitation_Perc': Avg_Percipitation_Perc}
#将字典转为dataframe
df = pd.DataFrame(data)
df

#绘制基础图层
fig, ax1 = plt.subplots(figsize=(10,6))
color = 'tab:green'
ax1.set_title('Average Percipitation Percentage by Month', fontsize=16)
ax1.set_xlabel('Month', fontsize=16)
ax1.set_ylabel('Avg Temp', fontsize=16, color=color)
#第一图条形图
ax1 = sns.barplot(x='Month', y='Avg_Temp', data = df, palette='summer')
ax1.tick_params(axis='y')
#twinx共享x轴(类似的语法，如共享y轴twiny)
ax2 = ax1.twinx()
color = 'tab:red'
#第二个图，折线图
ax2.set_ylabel('Avg Percipitation %', fontsize=16, color=color)
ax2 = sns.lineplot(x='Month', y='Avg_Percipitation_Perc', data = df, sort=False, color=color)
ax2.tick_params(axis='y', color=color)
#显示绘制结果
plt.show()