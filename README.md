# My-PyPort-QRCode
Follow Serena's journey - from noob to pro. This repo contains a sample of my
python projects. 

```
Version 2.0.0 - Secure Code

#import library 
import qrcode
import requests

#create variable and source - url
url = 'https://github.com/Born-A-Bot/My-PyPort-QRCode' 

#create image
img = qrcode.make(url)

#save the image and assign a name to the file
img.save("C://Users/seren/Documents/scrooples/pyport/qr_code/git_py.png")

#generate message when task complete, qrcode generated and saved
print('image saved')

#cybersecurity - set redirect parameter to prevent user connection from being hijacked, redirected
response = requests.get(url, allow_redirects=False)

#display status of connection, response
print(f"Status Code: {response.status_code}")

#notification, no redirect
if "Location" in response.headers:
    print(f"Redirect Location: {response.headers['Location']}")
else:
    print("No redirect decteced.")



```



```
version 1.0.0 - baseline

#import library for qrcode 
import qrcode

#create variable and source - url
img = qrcode.make('https://github.com/Born-A-Bot/My-PyPort-QRCode')

#save the image and assign a name to the file
img.save("git_py.png")

#generate message when task complete, qrcode generated and saved
print('image saved')

```


<img width="410" height="410" alt="git_py" src="https://github.com/user-attachments/assets/daca163c-ad06-429d-9c3f-0c07f75afd28" />
