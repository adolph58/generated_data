import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# 设置图标标题并给坐标轴加上标签。中文显示乱码，改成英文
ax.set_title("squares", fontsize=24)
ax.set_xlabel("values", fontsize=14)
ax.set_ylabel("values's squares", fontsize=14)

# 设置刻度标记的大小。
ax.tick_params(axis='both', labelsize=14)

plt.show()