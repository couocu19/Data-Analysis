import numpy as np
import matplotlib.pyplot as plt
import turtle
import random



def creat_chr_rates_histogram():
    x_data = [f"chr{i}" for i in range(1, 18)]
    # y_data1 = [0.15,0.21,0.2,0.22,0.2,0.2,0.2,0.2,0.2,0.2,0.22,0.21,0.21,0.21,0.21,0.2,0.02]
    # y_data = [0.61,0.7,0.7,0.66,0.67,0.65,0.66,0.66,0.65,0.68,0.67,0.65,0.69,0.7,0.67,0.68,0.65]

    y_data1 = []
    y_data = []
    # 正确显示中文和负号
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False
    # 画图，plt.bar()可以画柱状图
    for i in range(len(x_data)):
        plt.bar(x_data[i], y_data[i])
        plt.bar(x_data[i], y_data1[i])
    # 设置图片名称
    #plt.title("BWA二次匹配reads覆盖度")
    plt.title("Fanse2首次匹配reads覆盖度")
    # 设置x轴标签名
    plt.xlabel("染色体编号")
    # 设置y轴标签名
    plt.ylabel("reads在当前染色体上的覆盖度（0~1）")
    # 显示
    plt.show()


def creat_chr_rates_histogram1():
    x_data = [f"chr{i}" for i in range(1, 18)]
    # y_data1 = [0.61, 0.7, 0.7, 0.66, 0.67, 0.65, 0.66, 0.66, 0.65, 0.68, 0.67, 0.65, 0.69, 0.7, 0.67, 0.68, 0.65]
    # y_data2 = [0.66,0.774,0.77,0.74,0.74,0.714,0.733,0.73,0.72,0.75,0.75,0.72,0.76,0.77,0.74,0.75,0.66]

    y_data1 = [0.8326152,0.9774910 ,0.9848241,0.9665906,0.9526101,0.9372892,0.9498469,0.9338977 ,0.9197978 ,0.9342194,0.9630063,0.9118337,0.9604124,0.9596001,0.9510406,0.9525940,0.6278343]
    y_data2 = [0.1472952,0.1645052,0.1784284, 0.1551001,0.1560791,0.1577134,0.1534493,0.1548389,0.1514022, 0.1563297,0.1579701,0.1733778,0.1585548,0.1569945,0.1646371,0.1544175,0.1639446]
    y_data3 = [0]*17
    for i in range(0,17):
        a = y_data1[i]+y_data2[i]
        y_data3[i] = a
    for a in y_data3:
        print(a)

    y_data4 = [0.98,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.80]
    #
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False
    bar_width = 0.35
    index = np.arange(17)
    #for i in range(len(x_data)):
    plt.bar(index, y_data1, bar_width, # A班x轴数据起始位置为index序列 alpha表示透明度
            alpha=0.5, color='#c0737a',label='第一次比对') #肉粉色
    plt.bar(index + bar_width, y_data4, bar_width,  # B班x轴起始位置与A班数据错开
                alpha=0.5, color='#2c6fbb',label='两次比对后') #蓝色

    plt.xticks(index + bar_width / 2, x_data)  # index+bar_width/2 使得标签居中显示
    plt.ylim(0.5,1)
    plt.title("第一次比对和第二次比对后的reads总覆盖度对比图")
    # 设置x轴标签名
    plt.xlabel("染色体编号")
    # 设置y轴标签名
    plt.ylabel("reads在当前染色体上的覆盖度（0~1）")
    plt.legend()
    plt.show()

def create_char_avg_rates():
    t = turtle.Turtle()
    t.fillcolor('orange')
    t.begin_fill()
    t.pencolor('orange')
    t.circle(100)
    t.end_fill()

    t.forward(60)
    #t.goto(80,50)
    t.fillcolor('pink')
    t.begin_fill()
    t.pencolor('pink')
    t.circle(57)
    t.end_fill()

    t.backward(60)
    t.circle(100,20)

    t.fillcolor('yellow')
    t.begin_fill()
    t.pencolor('yellow')
    t.circle(100,69)
    t.end_fill()


    t.pencolor('orange')
    t.circle(100,271.2)

    t.forward(59)
    t.pencolor('pink')
    t.circle(57,133)

    t.fillcolor('yellow')
    t.begin_fill()
    t.pencolor('yellow')
    t.circle(57,202)
    t.end_fill()
    t.pencolor('pink')
    t.circle(57,30)



    turtle.done()






if __name__ == '__main__':
    creat_chr_rates_histogram1()
    #create_char_avg_rates()









