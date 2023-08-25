from PIL import Image
import numpy as np

# with Image.open(r"imgs\small.jpg") as im:
#     im.show()
#     img_nd = np.array(im)   # image to numpy.array
#     print(img_nd)
#     print(img_nd.dtype)    # 陣列元素型態。   --> uint8
#     print(img_nd.itemsize) # 陣列元素資料型態大小(或稱所佔空間)，單位是為位元組。  --> 1 個位元組
#     print(img_nd.ndim)     # 陣列的維度。  --> 3 個維度
#     print(img_nd.shape)    # 陣列維度元素個數的元組，也可以用於調整陣列大小。  --> (8, 8, 3)
#     print(img_nd.size)     # 陣列元素個數。 --> 192


with Image.open(r"imgs\face10.jpg") as im:
    # im.show()
    img_nd = np.array(im)   # image to numpy.array
    print(img_nd)
    print(img_nd.dtype)    # 陣列元素型態。   --> uint8
    print(img_nd.itemsize) # 陣列元素資料型態大小(或稱所佔空間)，單位是為位元組。  --> 1 個位元組
    print(img_nd.ndim)     # 陣列的維度。  --> 3 個維度
    print(img_nd.shape)    # 陣列維度元素個數的元組，也可以用於調整陣列大小。  --> (216, 200, 3)  ( 高 寬 RGB )  ( 列 行 色板 )
    print(img_nd.size)     # 陣列元素個數。 --> 129600

a1 = np.array([1,2,3])
print(a1.dtype)    # int32
print(a1.ndim)     # 1
print(a1.shape)    # (3,) (有逗點 表 一個元素的元組 ) --> 一維，裡面有三個元素

a2 = np.array([1.0,2,3])
print(a2.dtype)    # float64 --> ndarray 所有元素都是同一個型態
print(a2.ndim)     # 1
print(a2.shape)    # (3,)

# list 裡面元素可以是不同型態
list1 = [1.0,2,3]
print(type(list1[0]))  # <class 'float'>
print(type(list1[1]))  # <class 'int'>

a1 = np.array([1,2,3], np.uint8)
print(a1.dtype)    # uint8
print(a1.ndim)     # 1
print(a1.shape)    # (3,) (有逗點 表 一個元素的元組 ) --> 一維，裡面有三個元素

a2 = np.array([1.5,2.5,3.5], dtype=np.uint8)
print(a2.dtype)    # uint8
print(a2.ndim)     # 1
print(a2.shape)    # (3,)
print(a2)          # [1 2 3] 將小數點後數值直接刪除

# a3 = np.array(['1.5','2.5','3.5'], dtype=np.uint8)  # ValueError: invalid literal for int() with base 10: '1.5'
# print(a3.dtype)
# print(a3.ndim)
# print(a3.shape)
# print(a3)

a3 = np.array(['1','2','3'], dtype=np.uint8)
print(a3.dtype)   # uint8
print(a3.ndim)    # 1
print(a3.shape)   # (3,)
print(a3)         # [1 2 3]

# a3 = np.array(['a','b','c'], dtype=np.uint8)  # ValueError: invalid literal for int() with base 10: 'a'
# print(a3.dtype)
# print(a3.ndim)
# print(a3.shape)
# print(a3)

a3 = np.array(['a','b','c'])
print(a3.dtype)   # <U1
print(a3.ndim)    # 1
print(a3.shape)   # (3,)
print(a3)         # ['a' 'b' 'c']

a4 = np.array(['aaaaa','bbbbbb','ccccc'])
print(a4.dtype)   # <U6
print(a4.ndim)    # 1
print(a4.shape)   # (3,)

a5 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,6]])
print(a5.dtype)   # int32
print(a5.ndim)    # 2
print(a5.shape)   # (3列, 4行)
print(a5)
'''
[[1 2 3 4]
 [5 6 7 8]
 [9 8 7 6]]
'''
a5[2][0] = 90
print(a5)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [90  8  7  6]]
'''

# list 和 ndarray 比較
list2 = [[1,2,3,4],[5,6,7,8],[9,8,7,6]]
list2[2] = 90
print(list2)
'''
a5[2][0] = 90
print(a5)
'''

a5[2] = 90   # numpy 的 廣播功能(broadcast)  --> 自動填滿陣列
# 因為 : ndarray 陣列大小是固定
print(a5)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [90 90 90 90]]
'''
# numpy 廣播能功能broadcast
a = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])
b = np.array([0, 1, 2])
print(a + b)
'''
[[ 0  1  2]
 [10 11 12]
 [20 21 22]
 [30 31 32]]
'''