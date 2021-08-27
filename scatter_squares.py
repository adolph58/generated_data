import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# 参数 c，表示自定义颜色，可以传颜色的名称，也可以传元组，
# 元组包含三个 0~1 的小数值，分别表示红色、绿色和蓝色的分量
# ax.scatter(x_values, y_values, c='red', s=10)
# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
# 颜色映射,渐变，从小到大，颜色变深
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# 设置图标标题并给坐标轴加上标签。中文显示乱码，改成英文
ax.set_title("squares", fontsize=24)
ax.set_xlabel("values", fontsize=14)
ax.set_ylabel("values's squares", fontsize=14)

# 设置刻度标记的大小。
ax.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围。
ax.axis([0, 1100, 0, 1100000])

# 显示图表
plt.show()
# 自动保存图表
# plt.savefig('images/squares_plot.png', bbox_inches='tight')