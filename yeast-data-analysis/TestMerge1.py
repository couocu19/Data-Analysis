import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
x1=np.random.randn(50)
np.random.seed(1)
x2=np.random.randn(50)

plt.figure(dpi=120)
sns.set(style='dark')
sns.set_style("dark", {"axes.facecolor": "#e9f3ea"})
g=sns.distplot(x1,
               hist=True,
               bins=15,#修改箱子个数
               kde=False,
               color="#098154")
g=sns.distplot(x2,
               hist=True,
               bins=15,#修改箱子个数
               kde=False,
               color="#098100")
plt.show()
plt.savefig('demo.png')
