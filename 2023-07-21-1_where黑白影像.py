from PIL import Image
import numpy as np

with Image.open(r"imgs\face01.png") as im:   # 開啟影像
    img = np.array(im)   # ndarray

    img1 = np.transpose(img, (2, 0, 1))   # 換個方向觀察
    # transpose( 要轉換的ndarray, ( img.shape[2], img.shape[0], img.shape[1] )


    # 彩色轉灰階值
    gray = im.convert('L')   # Image物件

    # gray Image 物件改成 array
    _gray = np.array(gray)

    # 黑白影像(二元) where 練習
    a = np.zeros((_gray.shape[0], _gray.shape[1]), dtype=np.uint8)
    b = np.ones((_gray.shape[0], _gray.shape[1]), dtype=np.uint8) * 255
    binary = np.where(128 > _gray, a, b)

    # (彩、R、G、B) 四個小部件放入同個放畫面
    import matplotlib.pyplot as plt

    fig, axs = plt.subplots(2, 3, sharex=True, sharey=True)  # 產生圖畫紙物件fig、並產生小圖案(axs)陣列(2列 3行)
    print(fig)     # Figure(640x480)
    print(axs)
    '''
    [[<Axes: > <Axes: > <Axes: >]
     [<Axes: > <Axes: > <Axes: >]]
    '''

    # RGB
    axs[0, 0].imshow(img)
    axs[0, 0].set_title("RGB")

    # BINARY
    axs[0, 1].imshow(binary, cmap='gray')
    axs[0, 1].set_title("BINARY")

    # GRAY
    axs[0, 2].imshow(gray, cmap='gray')
    axs[0, 2].set_title("GRAY")

    # R
    axs[1, 0].imshow(img1[0], cmap='gray')
    axs[1, 0].set_title("R")

    # G
    axs[1, 1].imshow(img1[1], cmap='gray')
    axs[1, 1].set_title("G")

    # B
    axs[1, 2].imshow(img1[2], cmap='gray')
    axs[1, 2].set_title("B")



    plt.tight_layout()   # 緊密結合
    plt.show()