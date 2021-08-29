# 2D绘图库
import matplotlib.pyplot as plt
import numpy as np

# 计算正弦曲线上点的x和y坐标
x = np.arange(0, 2 * np.pi, 0.1)
y = np.sin(x)

plt.title("sine wave curve")
plt.plot(x, y)  # 使用matplotlib来绘制点
plt.show()
