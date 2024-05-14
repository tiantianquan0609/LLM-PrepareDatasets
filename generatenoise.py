import numpy as np
import matplotlib.pyplot as plt

# 设置图像大小
plt.figure(figsize=(8, 6))

# 生成随机噪声数据
noise_image = np.random.rand(100, 100)  # 生成一个100x100的随机数组，范围在[0,1)

# 绘制噪声图
plt.imshow(noise_image, cmap='gray')
plt.title('随机噪声图')
plt.axis('off')  # 关闭坐标轴
plt.colorbar()  # 添加颜色条
plt.show()
