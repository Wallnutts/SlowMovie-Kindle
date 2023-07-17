import requests
import time
import PIL
from PIL import Image

# Send the image to the endpoint as form data
def send_to_kindle(img,url):
    files = {'image': ('output.png', img, 'image/png')} #create dict object
    response = requests.post(url, files=files)

    # Display the response from the endpoint
    print('Kindle Response:', response.text)
    return(response.text)
    time.sleep(1)



    
