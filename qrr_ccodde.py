import qrcode as qr #pip install qrcode
import image #pip install image


img= qr.make("Link")
img.save("name.png")
img.show()
