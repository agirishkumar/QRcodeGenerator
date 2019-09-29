# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 


# String which represent the QR code 
s = input("Enter the text: ")

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the png file naming "myqr.png" 
url.svg("qr.svg", scale = 8) 

