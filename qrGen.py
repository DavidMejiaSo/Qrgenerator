import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=7,
    border=2
)

input_link = 'https://66d3b3741cdaaea2759540e2--illustrious-cuchufli-01f24b.netlify.app'
qr.add_data(input_link)

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")  # Especifica el nombre del archivo aquí
