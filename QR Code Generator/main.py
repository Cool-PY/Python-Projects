import qrcode as qr

img = qr.make("https://coolpy.netlify.com")
img.save('qrcode.png')
