from PIL import Image
import numpy as np

a1 = np.zeros((3,4), dtype=np.uint8)

print(a1.dtype)    # uint8
print(a1.ndim)     # 2
print(a1.shape)    # (3, 4)
print(a1)
'''
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]
'''

a2 = np.ones((3,4), dtype=np.uint8)

print(a2.dtype)    # uint8
print(a2.ndim)     # 2
print(a2.shape)    # (3, 4)
print(a2)
'''
[[1 1 1 1]
 [1 1 1 1]
 [1 1 1 1]]
'''
print(a2*255)
'''
[[255 255 255 255]
 [255 255 255 255]
 [255 255 255 255]]
'''

a3 = np.ones((300,400), dtype=np.uint8)*255  # (列 行) (高 寬)

print(a3.dtype)
print(a3.ndim)
print(a3.shape)
a3 = np.reshape(a3,120000)  # 將a2拉平，拉成120000個格子

# 將 ndarray 轉成 Image物件
im2 = Image.new('L', (400,300))
im2.putdata(a3)
im2.show()
