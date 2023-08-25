from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc('font', family='Microsoft JhengHei')   # rc函式 --> 可指定各式各樣的環境 ('font'環境 ->字型 )

a, b = np.ogrid[255:0:-4,0:1]

_a = np.ones((64,256), dtype = np.uint8)
b = _a * a
print(b)

plt.imshow(b,cmap='gray')
plt.show()

# with Image.open(r"imgs\Figure_1.png") as im:
#     im.show()
#     img = np.array(im)  # image to numpy.array
#     img = np.transpose(img, (2, 0, 1))
#     print(img.shape)    # (4, 480, 640)
#     print(img)


    # img2 = img[1:7, 1:7, :]
    # # img = np.transpose(img, (2,0,1))
    # # img2 = img[:, 1:7, 1:7]
    # # img2 = np.transpose(img2, (1, 2, 0))
    #
    # plt.imshow(img2)
    # plt.show()


    # img1 = np.ones((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8) * 255
    # img1[1:7, 1:7, :] = img[1:7, 1:7, :]   # [ 1:7, 1:7, 每個色板都要]
    #
    # fig, axs = plt.subplots(1, 2, sharex=True, sharey=True)
    # axs[0].imshow(img)
    # axs[0].set_title("原始")
    # axs[1].imshow(img1, cmap='gray')
    # axs[1].set_title("切割")
    #
    # plt.tight_layout()   # 緊密結合
    # plt.show()
