'''
学习用OpenCV控制鼠标事件
学习以下函数：cv.setMouseCallback()

'''


# import cv2 as cv
# events = [i for i in dir(cv) if 'EVENT' in i]
# print( events )
#
# '''
# opencv 所有的事件
# [
# # FLAG
# 'EVENT_FLAG_ALTKEY',
# 'EVENT_FLAG_CTRLKEY',
# 'EVENT_FLAG_LBUTTON',
# 'EVENT_FLAG_MBUTTON',
# 'EVENT_FLAG_RBUTTON',
# 'EVENT_FLAG_SHIFTKEY',
# #
# # BUTTON
# 'EVENT_LBUTTONDBLCLK',
# 'EVENT_LBUTTONDOWN',
# 'EVENT_LBUTTONUP',
# 'EVENT_MBUTTONDBLCLK',
# 'EVENT_MBUTTONDOWN',
# 'EVENT_MBUTTONUP',
# 'EVENT_MOUSEHWHEEL',
# 'EVENT_MOUSEMOVE',
# 'EVENT_MOUSEWHEEL',
# 'EVENT_RBUTTONDBLCLK',
# 'EVENT_RBUTTONDOWN',
# 'EVENT_RBUTTONUP']
#
# '''


# # 一个简单的示例
# import numpy as np
# import cv2 as cv
# # mouse callback function
# def draw_circle(event,x,y,flags,param):        # 參數固定寫法 (x,y 為傳入的滑鼠位置座標)
#     if event == cv.EVENT_LBUTTONDBLCLK:        # 事件為 EVENT_LBUTTONDBLCLK 左鍵連點兩下
#         cv.circle(img,(x,y),100,(255,0,0),-1)  # (x,y)為滑鼠座標 -> 以他為圓心畫半徑100的圓 | (255,0,0)顏色 |  -1 表示實心圓
#
# # Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv.namedWindow('window1')
# cv.setMouseCallback('window1',draw_circle)  # window1視窗中 任何滑鼠的動作動去執行draw_circle
# while(1):
#     cv.imshow('window1',img)
#     if cv.waitKey(20) & 0xFF == 27:
#         break
# cv.destroyAllWindows()
#
#
# 一个更高级的示例
import numpy as np
import cv2 as cv

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv.destroyAllWindows()