from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc('font', family='Microsoft JhengHei')   # rc函式 --> 可指定各式各樣的環境 ('font'環境 ->字型 )

# list_2D = []
# for row in range(64) :
#     list_1D = []
#     for col in range(256) :
#         list_1D.append(row*4)
#
#     list_2D.append(list_1D)

# 巢狀生成式  --> 專門產生二維串列
list_2D = [[ row*4 for col in range(256)] for row in range(64)]
list1 = list_2D * 4  # 上下合併串列 直接相加


# list_2D = []
# for row in range(64) :
#     list_1D = []
#     for col in range(256) :
#         list_1D.append(252 - row*4)
#
#     list_2D.append(list_1D)
#
# list2 = list_2D * 4
list2 = list1[::-1]

_list1 = list1 + list2
_list2 = list2 + list1

img1 = np.array(_list1)
img2 = np.array(_list2)

x = np.hstack((img1,img2))

plt.imshow(x,cmap='gray')
plt.show()