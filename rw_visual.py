import matplotlib.pyplot as plt
import pygal

from random_walk import RandomWalk

while True:
    rw=RandomWalk()
    rw.fill_walk()

    plt.figure(figsize=(10,6))

    point_numbers=list(range(rw.num_point))

    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,s=15)
    # plt.plot(rw.x_values,rw.y_values,linewidth=1)
    #突出起点和终点
    plt.scatter(0,0,c='green',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=100)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    #使用pygal完成随机漫步可视化
    # hist=pygal.XY(stroke=False)
    # hist.title='Random Walk'
    # hist.add('A',[(rw.x_values[i],rw.y_values[i]) for i in range(0,rw.num_point)])
    # hist.render_to_file('RandomWalk.svg')

    keep_running= input('Make another walk? (y/n)')
    if keep_running=='n':
        break