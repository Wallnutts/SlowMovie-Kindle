
url = 'http://192.168.1.32:5000/uploadthen'

import requests
import PIL
from PIL import Image, ImageEnhance
from io import BytesIO

# Load the image file
img = Image.open('frame.bmp')

# Resize the image
#img.thumbnail((1448, 1072), Image.ANTIALIAS)

enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(1)

enhancer = ImageEnhance.Brightness(img)
img = enhancer.enhance(2)

# Convert the image to bytes
img_bytes = BytesIO()
img.save(img_bytes, format='PNG')
img_bytes.seek(0)

# Send the image to the endpoint as form data

files = {'image': ('output.png', img_bytes, 'image/png')}
response = requests.post(url, files=files)

# Display the response from the endpoint
print( response.text)
