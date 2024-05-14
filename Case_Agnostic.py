import numpy as np
import matplotlib.pyplot as plt

# 生成x的范围
x = np.linspace(-5, 5, 100)

# 计算概率密度函数
pdf = (1.0 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

# 绘制概率密度函数曲线图
plt.figure(figsize=(8, 6))
plt.plot(x, pdf, color='blue', linewidth=4.5)
plt.title('均值为零、单位方差的多变量分布')
plt.xlabel('变量值')
plt.ylabel('概率密度')
plt.grid(True)
plt.show()
