import numpy as np
import cv2 as cv

img = cv.imread(r'.\imgs\face10.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
rows,cols = img.shape
# cols-1 and rows-1 are the coordinate limits.
# M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),10,1)
# # 參數( 中心點為 ((cols-1)/2.0,(rows-1)/2.0) , 旋轉 10度(逆時針方想旋轉), 放大1倍(不放大))

M = cv.getRotationMatrix2D((0, 0),10,1)
# 參數( 中心點為 ((cols-1)/2.0,(rows-1)/2.0) , 旋轉 10度(逆時針方想旋轉), 放大1倍(不放大))

dst = cv.warpAffine(img,M,(cols,rows)) # 視窗大小固定在原影像尺寸 (cols,rows)

cv.namedWindow("img", 0)  # 這樣視窗才可以縮放
cv.imshow("img", dst)
cv.waitKey(0)
cv.destroyAllWindows()