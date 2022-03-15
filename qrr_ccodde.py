import qrcode as qr #pip install qrcode
import image #pip install image


img= qr.make("https://youtu.be/kcVeiQn4PjY")
img.save("name.png")
img.show()
