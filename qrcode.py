import pyqrcode
import png

s = "https://www.facebook.com/gurup.subedee.3"
url = pyqrcode.create(s)
url.svg("guruqr.svg", scale=8)
url.png("guruqr.png", scale=6)