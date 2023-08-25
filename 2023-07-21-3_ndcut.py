from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc('font', family='Microsoft JhengHei')   # rc函式 --> 可指定各式各樣的環境 ('font'環境 ->字型 )

with Image.open(r"imgs\small.jpg") as im:

    img = np.array(im)  # image to numpy.array
    print(img.shape)    # (8, 8, 3)

    # img2 = img[1:7, 1:7, :]
    # # img = np.transpose(img, (2,0,1))
    # # img2 = img[:, 1:7, 1:7]
    # # img2 = np.transpose(img2, (1, 2, 0))
    #
    # plt.imshow(img2)
    # plt.show()


    img1 = np.ones((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8) * 255
    img1[1:7, 1:7, :] = img[1:7, 1:7, :]   # [ 1:7, 1:7, 每個色板都要]

    fig, axs = plt.subplots(1, 2, sharex=True, sharey=True)
    axs[0].imshow(img)
    axs[0].set_title("原始")
    axs[1].imshow(img1, cmap='gray')
    axs[1].set_title("切割")

    plt.tight_layout()   # 緊密結合
    plt.show()



'''
二維串列切片 list
'''
# from PIL import Image
# import numpy as np
#
# with Image.open(r"imgs\small.jpg") as im:
#     im.show()
#
#     # image to numpy.array
#     img = np.array(im)
#     print(type(img))   # <class 'numpy.ndarray'>
#
#     # numpy to list
#     img_list = img.tolist()
#     print(type(img_list))  # <class 'list'>
#
#     # 切出中間黃色方形
#     img_list1 = img_list[1:7]
#     img_list2 = list(zip(*img_list1))[1:7]
#     img_list3 = list(zip(*img_list2))
#     print(img_list3)
#
#     # 將 (img_list) List物件 轉成 (im) Image物件
#     im2 = Image.new(im.mode, (len(img_list3[0]), len(img_list3)))   # 先開一個新Image物件  # mode、size 為物件的屬性
#     im2.putdata([ tuple(sub2) for sub1 in img_list3   for sub2 in sub1 ])  # 放入資料
#     im2.show()