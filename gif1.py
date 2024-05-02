import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 定義 x(t) 和 y(t) 函數
def x(t):
    return np.cos(5*t) * np.cos(t)

def y(t):
    return np.cos(5*t) * np.sin(t)

# 生成 t 的值從 0 到 2*pi
t_values = np.linspace(0, 2*np.pi, 100)

# 初始化圖片
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
line, = ax.plot([], [], lw=2)

# 更新函數
def update(frame):
    line.set_data(x(t_values[:frame]), y(t_values[:frame]))
    return line,

# 創建動畫
ani = FuncAnimation(fig, update, frames=len(t_values), blit=True)

# 儲存 gif
ani.save('eg1.gif', writer='imagemagick', fps=30)

plt.show()
