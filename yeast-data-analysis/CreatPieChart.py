import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#绘制饼图区分匹配数据和未匹配数据

labels = ['assembled','the-rest-unmapped']
data = ['0.0043','0.9957']
plt.pie(data, labels=labels, colors=['Crimson','PaleTurquoise'],autopct='%1.2f%%')  # 第一个参数是占比，第二个各自的标签，第三个是显示精度

plt.axis('equal')  # 让图看起来是圆的，不然就扁了
plt.legend()  # 左上角的那个图例，随机的，可以自己换位置

plt.show()
