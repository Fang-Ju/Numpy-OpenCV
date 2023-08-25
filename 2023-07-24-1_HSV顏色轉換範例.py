import cv2 as cv
# flags = [i for i in dir(cv) if i.startswith('COLOR_')]
# list 生成 i --> cv所有能用的方法與屬性 --> 附加條件: COLOR_ 開頭的留下
# 找跟顏色有關的方法與屬性

flags_HSV = [i for i in dir(cv) if i.startswith('COLOR_HSV')]
flags_RGB = [i for i in dir(cv) if i.startswith('COLOR_RGB')]

print( flags_HSV )
print( flags_RGB )