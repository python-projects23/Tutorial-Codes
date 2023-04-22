# QR Code Generator

import qrcode

data = "https://github.com/python-projects23/Tutorial-Codes/blob/master/printing_var.py"

# create QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("QR_code_Gen.png")
