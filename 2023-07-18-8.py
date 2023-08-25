from PIL import Image
import numpy as np

a1 = np.random.randint(0, 256, size=(30, 40), dtype=np.uint8)
print(a1.dtype)    # uint8
print(a1.ndim)     # 2
print(a1.shape)    # (30, 40)
print(a1)

a2 = np.reshape(a1, (15, -1))  # -1 : 前面確定了 -1 表讓電腦自動計算
print(a2.dtype)    # uint8
print(a2.ndim)     # 2
print(a2.shape)    # (15, 80)
print(a2)

a3 = np.reshape(a1, (17, -1))  # -1表讓電腦自動計算
# ValueError: cannot reshape array of size 1200 into shape (17,newaxis)
# 除不盡是不行的

print(a3.dtype)    # uint8
print(a3.ndim)     # 2
print(a3.shape)    # (15, 80)
print(a3)
