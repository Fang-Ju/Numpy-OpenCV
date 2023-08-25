import numpy as np
import cv2 as cv


# def imread_np(file1):
#     mem = np.fromfile(file1, dtype=np.uint8)
#     # print(mem)
#     # print(mem.shape)  # (7157,)
#     cv_img = cv.imdecode(mem, 1)  # 1-->讀彩色的  cv.IMREAD_COLOR (ImreadModes)
#     return cv_img
#
# # img = cv.imread(r'.\尖兵班照片\劉芳如.jpg') # 讀不到中文
# # img = cv.imread(r'.\尖兵班照片\face10.jpg') # 讀不到中文
# # img = cv.imread(r'.\imgs\face10.jpg')
# # img = imread_np(r'.\imgs\face10.jpg')
# img = imread_np(r'.\尖兵班照片\劉芳如.jpg') # 運用 numpy 讀到中文了
# assert img is not None, "file could not be read, check with os.path.exists()"


# PIL 讀法
from PIL import Image, ImageDraw

#1
# img = Image.open(r'.\尖兵班照片\劉芳如.jpg')
# img = np.array(img)  # 變成 ndarray
# img = Image.fromarray(img)  # 變成 ImageObject
# img.show()

#2
# img = Image.open(r'.\尖兵班照片\劉芳如.jpg')
# img = np.array(img) [:,:,::-1] # 變成 ndarray 符合BGR要求

# 影像前畫圖
img = Image.open(r'.\尖兵班照片\劉芳如.jpg')
draw = ImageDraw.Draw(img)  # 產生Draw物件 相當於在照片上產生透明的圖畫紙，以便之後畫在上面
draw.line((0, 0) + img.size, fill=128)   # (PIL)img.size -> return tuple
draw.line((0, img.size[1], img.size[0], 0), fill=128)
# line((四個點xy,xy劃一條線), fill=線的顏色)

img.show()


cv.namedWindow("img", 0)  # 這樣視窗才可以縮放
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()