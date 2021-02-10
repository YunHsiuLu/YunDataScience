import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 創建一個3d坐標系
fig = plt.figure()
ax = Axes3D(fig)
#直接查詢參數與設定
#help(plt.plot)
#help(np.random.sample)

# 利用x軸和y軸繪製sin曲線
x = np.linspace(0, 1, 100) # linspace創建等差陣列
y = np.cos(x * 2 * np.pi) / 2 + 0.5
# 通過zdir = 'z' 將資料繪製在z軸，zs = 0.5 則是將資料繪製在z = 0.5的地方
ax.plot(x, y, zs = 0.5, zdir = 'z', color = 'black', label = 'curve in (x, y)')
fig.savefig('figure2.png')