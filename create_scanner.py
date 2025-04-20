import qrcode
img = qrcode.make(
    'https://www.pexels.com/photo/woman-standing-behind-trees-2913125/'
)
img.save('myQRcode.png')
img.show()