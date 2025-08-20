# My-PyPort-QRCode
Follow Serena's journey - from noob to pro. This repo contains a sample of my
python projects. 

```
#import library for qrcode
import qrcode

#create variable and source - url
img = qrcode.make('https://github.com/Born-A-Bot/My-PyPort-QRCode')

#save the image and assign a name to the file
img.save("git_py.png")

#generate message when task complete, qrcode generated and saved
print('image saved')

```


