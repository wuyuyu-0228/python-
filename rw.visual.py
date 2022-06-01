import matplotlib.pyplot as plt
#15-3.3
from random_walk import RandomWalk
while True:
    rw=RandomWalk()
    rw.fill_walk()

    #将所有点都绘制出来
    plt.style.use('classic')
    fig,ax=plt.subplots(figsize=(10,6))
    point_numbers=range(rw.num_points)
    ax.plot(rw.x_values,rw.y_values)
    plt.plot(rw.x_values,rw.y_values,linewidth=1)

    #突出起点和终点
    # ax.plot(0, 0, c='green', edgecolors='none', s=100 )
    # ax.plot(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk?(y/n):')
    if keep_running == 'n':
        break