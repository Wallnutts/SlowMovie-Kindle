import requests
import time

# Send the image to the endpoint as form data
def send_to_kindle(img,url):
    print('entered')
    files = {'image': ('output.png', img, 'image/png')} #create dict object
    print(files)
    response = requests.post(url, files=files)

    # Display the response from the endpoint
    print(response.text)
    return(response.text)

time.sleep(1)

    
