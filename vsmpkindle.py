
#Example file for sending a single image through to the kindle. 
#set the kindle address here
url = 'http://192.168.1.32:5000//uploadthen'

import requests
import time
from PIL import Image
from io import BytesIO

# Load the image file
img = Image.open('frames/frame{}.png'.format(str(x).zfill(5)))
print('frames/frame{}.png'.format(str(x).zfill(5)))

# Resize the image
img.thumbnail((1072, 1448), Image.ANTIALIAS)

# Convert the image to bytes
img_bytes = BytesIO()
img.save(img_bytes, format='PNG')
img_bytes.seek(0)

# Send the image to the endpoint as form data

files = {'image': ('output.png', img_bytes, 'image/png')}
response = requests.post(url, files=files)

# Display the response from the endpoint
print( response.text)

time.sleep(1)

    
