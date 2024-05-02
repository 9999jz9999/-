import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 定義 Lissajous 曲線的函數
def lissajous_curve(a, b, delta):
    t = np.linspace(0, 2*np.pi, 1000)
    x = np.sin(a*t + delta)
    y = np.sin(b*t)
    return x, y

# 初始化圖片
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
line, = ax.plot([], [], lw=2)

# 更新函數
def update(frame):
    x, y = lissajous_curve(5, 4, 0.5 * frame)
    # 將x和y交換以進行90度旋轉
    line.set_data(y, x)
    return line,

# 創建動畫
ani = FuncAnimation(fig, update, frames=200, blit=True)

# 儲存 gif
ani.save('eg2.gif', writer='imagemagick', fps=30)

plt.show()
