from PIL import Image
import numpy as np

a1 = np.random.randint(0, 256, size=(30, 40), dtype=np.uint8)
a2 = np.random.randint(0, 256, size=(30, 40, 3), dtype=np.uint8)
print(a1.dtype)    # int32
print(a1.ndim)     # 2
print(a1.shape)    # (16, 12)
print(a1)

# 將 ndarray 轉成 Image物件
im2 = Image.new('L', (a1.shape[1], a1.shape[0]))
im2.putdata(np.reshape(a1, a1.shape[0]*a1.shape[1]))
im2.show()

# 另外一種顯像方式
import matplotlib.pyplot as plt
plt.imshow(a1, cmap='gray')
plt.imshow(a2)
plt.show()
