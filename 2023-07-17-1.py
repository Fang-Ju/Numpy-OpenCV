from PIL import Image
import numpy as np

with Image.open(r"imgs\small.jpg") as im:  # 模組裡專門開影像的open   # im(隨意命名) 為 Image物件
    im.rotate(0).show()   # Image物件 的 show()  --> 電腦內建用什麼方式展現影像 他就用那個方式show圖
    # print(im)   # print 看不到內容 --> <PIL.PngImagePlugin.PngImageFile image mode=RGB size=803x696 at 0x25A6345A6E0>

    # image to numpy.array
    img = np.array(im)
    print(img)
    print(type(img))   # <class 'numpy.ndarray'>

    # numpy to list
    img_list = img.tolist()
    print(img_list)
    print(type(img_list))  # <class 'list'>

    # # 將四角的顏色像素變成白色
    # img_list[0][0] = [255, 255, 255]
    # img_list[0][-1] = [255, 255, 255]
    # img_list[-1][0] = [255, 255, 255]
    # img_list[-1][-1] = [255, 255, 255]
    # print(img_list)

    # 將四角的顏色像素變成白色 --> 直接做成tuple
    img_list[0][0] = (255, 255, 255)
    img_list[0][-1] = (255, 255, 255)
    img_list[-1][0] = (255, 255, 255)
    img_list[-1][-1] = (255, 255, 255)
    print(img_list)

    # list整理 --> 裡面改成 tuple
    img_list = [ tuple(sub2) for sub1 in img_list   for sub2 in sub1 ]
    print(img_list)

    # 將 (img_list) List物件 轉成 (im) Image物件
    im2 = Image.new(im.mode, im.size)   # mode、size 為物件的屬性  # 先開一個新Image物件
    im2.putdata(img_list)  # 放入資料  # TypeError: color must be int or tuple
    im2.show()