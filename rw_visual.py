import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个 RandomWalk 实例。
    # 初始值：5000 个点，s=15
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # 将所有的点都绘制出来。
    plt.style.use('classic')
    # 指定屏幕尺寸，figsize 指定生成的图形的尺寸，单位为英寸
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values,  rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 突出起点和终点。
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴。
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break