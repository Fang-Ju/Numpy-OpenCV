'''
劉芳如
2023-07-18 homework
-將彩色圖片單以 R、G、B 單一色板呈現
'''


from PIL import Image
import numpy as np

with Image.open(r"Numpy&OpenCV\imgs\2023-3-31-1.png") as im:   # 開啟影像
    # im.show()
    # print(im)    # <PIL.PngImagePlugin.PngImageFile image mode=RGB size=992x896 at 0x292FDAEE1D0>

    # image to ndarray
    img_nd = np.array(im)
    # print(img_nd)
    # print(type(img_nd))     # numpy.ndarray
    # print(img_nd.dtype)     # uint8
    # print(img_nd.ndim)      # 3
    # print(img_nd.shape)     # (896, 992, 3) ( 高 寬 色板 )


# R 色板
# print(img_nd.T.shape)         # (3, 992, 896)
img_T = img_nd.T              # 轉置 --> ( 色板 寬 高 )
img_R = img_T[0]              # 取得 R 色板
# print(img_R.shape)            # (992, 896) (寬 高)
img_R = img_R.T               # 轉置 --> 轉回原來的 (高 寬)
# print(img_R.shape)            # (896, 992)

# 將 ndarray 轉成 Image物件
im_R = Image.new('L', (img_R.shape[1], img_R.shape[0]))            # 建立新的Image物件 ('黑白模式', (寬, 高) )
im_R.putdata(np.reshape(img_R, img_R.shape[0]*img_R.shape[1]))     # 放入img_R資料 <-- 將 img_R 改成一維資料 (896*992)
im_R.show()


# G 色板
img_T = img_nd.T              # 轉置 --> ( 色板 寬 高 )
img_G = img_T[1].T            # 取得 G 色板 並 轉置
# print(img_G.shape)            # (896, 992)

# 將 ndarray 轉成 Image物件
im_G = Image.new('L', (img_G.shape[1], img_G.shape[0]))            # 建立新的Image物件 ('黑白模式', (寬, 高) )
im_G.putdata(np.reshape(img_G, img_G.shape[0]*img_G.shape[1]))     # 放入img_G資料 <-- 將 img_G 改成一維資料 (896*992)
im_G.show()


# B 色板
img_T = img_nd.T              # 轉置 --> ( 色板 寬 高 )
img_B = img_T[2].T            # 取得 B 色板 並 轉置
# print(img_B.shape)            # (896, 992)

# 將 ndarray 轉成 Image物件
im_B = Image.new('L', (img_B.shape[1], img_B.shape[0]))            # 建立新的Image物件 ('黑白模式', (寬, 高) )
im_B.putdata(np.reshape(img_B, img_B.shape[0]*img_B.shape[1]))     # 放入img_B資料 <-- 將 img_B 改成一維資料 (896*992)
im_B.show()