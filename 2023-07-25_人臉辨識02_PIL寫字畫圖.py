from PIL import Image, ImageDraw, ImageFont
# ImageDraw.ImageDraw.font = ImageFont.truetype(r'C:\Windows\Fonts\msjh.ttc')  # 設定所有照片共同字體

# get an image
with Image.open(r'.\尖兵班照片\劉芳如.jpg').convert("RGBA") as base:  # convert("RGBA") 可調透明度模式

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))  # 新增Image物件(另一張照片) 和原來照片一樣大 全透明

    # get a font
    fnt = ImageFont.truetype(r'C:\Windows\Fonts\msjh.ttc', 150)
    # get a drawing context
    d = ImageDraw.Draw(txt)  # 按 txt 產生 Draw 物件 --> 在上面畫圖寫字

    # 畫框
    d.rectangle([250,170,850,950], fill=None, outline=(0,0,255), width=10)
    d.rectangle([250,950,850,1200], fill=(0,0,255), outline=(0,0,255), width=10)

    # draw text, half opacity
    # d.text((300, 800), "Hello", font=fnt, fill=(255, 255, 255, 128))
    # draw text, full opacity
    d.text((330, 960), "劉芳如", font=fnt, fill=(255, 255, 255, 128))


    out = Image.alpha_composite(base, txt)  # 將 base(原圖) txt(透明圖) 合併-->透明圖層合併\
    out.show()
