#import library 
import qrcode
import requests
from PIL import Image


logo_link = "letterS_logo.png"

#import business logo
logo = Image.open(logo_link)

#specify image size, color, etc.
basewidth = 100

#auto adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ADAPTIVE)
qr = qrcode.QRCode(
    version= 2.0,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
)

#create variable and source - url
url = 'https://github.com/Born-A-Bot/My-PyPort-QRCode' 

#add url to image
qr.add_data(url)

#render the image
img = qr.make_image(fill_color = "black", black_color = "white").convert('RGB')


#set size of qr
pos = ((img.size[0] - logo.size[0]) //2,
	(img.size[1] - logo.size[1]) //2)
img.paste(logo,pos)

#save the image and assign a name to the file
img.save("C://Users/seren/Documents/scrooples/pyport/qr_code/qr_with_logo_v3.png")

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



