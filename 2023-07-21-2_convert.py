from PIL import Image
import numpy as np

with Image.open(r"imgs\263744.jpg") as im:   # 開啟影像
    img = np.array(im)   # ndarray

    # 彩色轉灰階值
    gray = im.convert('L')   # Image物件

    # gray Image 物件改成 array
    _gray = np.array(gray)

    # Mode1
    b1 = im.convert('1')
    _b1 = np.array(b1)
    print(_b1)

    # 黑白影像(二元) where 練習
    a = np.zeros((_gray.shape[0], _gray.shape[1]), dtype=np.uint8)
    b = np.ones((_gray.shape[0], _gray.shape[1]), dtype=np.uint8) * 255
    binary = np.where(128 > _gray, a, b)

    # (彩、R、G、B) 四個小部件放入同個放畫面
    import matplotlib.pyplot as plt

    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)  # 產生圖畫紙物件fig、並產生小圖案(axs)陣列(2列 2行)
    print(fig)     # Figure(640x480)
    print(axs)
    '''
    [[<Axes: > <Axes: > <Axes: >]
     [<Axes: > <Axes: > <Axes: >]]
    '''

    # RGB
    axs[0, 0].imshow(img)
    axs[0, 0].set_title("RGB")

    # Mode 1
    axs[1, 1].imshow(b1)
    axs[1, 1].set_title("BINARY Mode 1")

    # BINARY
    axs[0, 1].imshow(binary, cmap='gray')
    axs[0, 1].set_title("BINARY")

    # GRAY
    axs[1, 0].imshow(gray, cmap='gray')
    axs[1, 0].set_title("GRAY")


    plt.tight_layout()   # 緊密結合
    plt.show()