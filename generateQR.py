import qrcode

features = qrcode.QRCode(version=1,box_size=500,border=5)

features.add_data('https://github.com/Swathi40')
features.make(fit=True)
generate_image = features.make_image(fill_color="black",back_color="white") 
generate_image.save('image5.png')