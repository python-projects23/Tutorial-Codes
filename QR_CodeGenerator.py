# PYTHON QUICKIES #PROJECT 1
# QR CODE GENERATOR

# install qrcode using cmd command "pip install qrcode pillow"
import qrcode

# define data
data = "PYTHON QUICKIES QR CODE GENERATOR"

# create QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# add data to the QR code instance
qr.add_data(data)

# make the QR code image
qr.make(fit=True)

# get the QR code image as PIL Image instance
img = qr.make_image(fill_color="black", back_color="white")

# Name the file
img.save("QR.png")








