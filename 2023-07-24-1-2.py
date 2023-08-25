import cv2 as cv
import numpy as np

# color_dict_HSV = { '色相' : [ upper ] , [ lower ] }
color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
              'white': [[180, 18, 255], [0, 0, 231]],
              'red1': [[180, 255, 255], [159, 50, 70]],
              'red2': [[9, 255, 255], [0, 50, 70]],
              'green': [[89, 255, 255], [36, 50, 70]],
              'blue': [[128, 255, 255], [90, 50, 70]],
              'yellow': [[35, 255, 255], [25, 50, 70]],
              'purple': [[158, 255, 255], [129, 50, 70]],
              'orange': [[24, 255, 255], [10, 50, 70]],
              'gray': [[180, 18, 230], [0, 0, 40]]}
                        #  upper , lower


cap = cv.VideoCapture(0)  # 找到攝影機產生攝影機物件
while(1):
    # Take each frame
    _, frame = cap.read()   # 攝影機讀一張張的照片 1秒30張  --> return兩個參數，我只要第二個 用frame留下它(不要的用_接)
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # 那張照片 將RGB轉成HSV
    # define range of blue color in HSV  --> 網路上查
    lower_blue = np.array([110,50,50])   # 藍色的最小極限
    upper_blue = np.array([130,255,255]) # 藍色的最大極限
    # lower_red2 = np.array([0, 50, 70])
    # upper_red2 = np.array([9, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)  # 產生遮罩
    # mask = cv.inRange(hsv, lower_red2, lower_red2)  # 產生遮罩

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)   # 遮罩和位元運算
    # --> 只看藍色的東西

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:  # 按鍵盤 Esc(27)
        break
cv.destroyAllWindows()