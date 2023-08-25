import numpy as np
import cv2 as cv

img = cv.imread(r'.\imgs\face10.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"
# assert 當條件為假的時候拋出錯誤  條件: img is not None

res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_LANCZOS4)  # print(cv.INTER_LANCZOS4) --> 4 --可以這樣寫--> interpolation = 4
# x方向y方向同時放大兩倍 , interpolation(內插法 插值法)(按照你的樣本補資料)
# (dsize)None --> 一定要寫(規定) 告訴他要變大多少，寫None是表示在其他處說明 -->  fx=2, fy=2 他用這兩個參數說明

#OR
# height, width = img.shape[:2]
# res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)
# 這就是用dsize參數調整大小，不用fx, fy(這兩個參數可寫可不寫)

cv.namedWindow("src", 0)  # 這樣視窗才可以縮放
cv.imshow("src", img)
cv.namedWindow("res", 0)  # 這樣視窗才可以縮放
cv.imshow("res", res)
cv.waitKey(0)
cv.destroyAllWindows()
