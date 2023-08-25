from PIL import Image
import numpy as np

with Image.open(r"imgs\small.jpg") as im:
    im.show()

    # image to numpy.array
    img = np.array(im)
    print(type(img))   # <class 'numpy.ndarray'>

    # numpy to list
    img_list = img.tolist()
    print(type(img_list))  # <class 'list'>

    # 切出中間黃色方形
    img_list1 = img_list[1:7]
    img_list2 = list(zip(*img_list1))[1:7]
    img_list3 = list(zip(*img_list2))
    print(img_list3)

    # 將 (img_list) List物件 轉成 (im) Image物件
    im2 = Image.new(im.mode, (len(img_list3[0]), len(img_list3)))   # 先開一個新Image物件  # mode、size 為物件的屬性
    im2.putdata([ tuple(sub2) for sub1 in img_list3   for sub2 in sub1 ])  # 放入資料
    im2.show()