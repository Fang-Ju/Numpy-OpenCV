import numpy as np
import cv2 as cv
print(cv.IMREAD_GRAYSCALE) # 0 --> 灰階
img = cv.imread(r'.\imgs\face10.jpg', cv.IMREAD_GRAYSCALE)  # 讀檔時給參數
assert img is not None, "file could not be read, check with os.path.exists()"
rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(cols,rows))  # 轉換陣列 (img,M, col(寬(行),rows 高(列) )
# warpAffine 扭曲仿射

cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()
