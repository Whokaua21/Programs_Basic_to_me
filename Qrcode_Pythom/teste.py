import qrcode

# URL do site que você deseja vincular ao código QR
url_do_site = "https://www.exemplo.com"

# Crie um objeto QRCode
codigo_qr = qrcode.QRCode(
    version=1,  # Versão do código QR
    error_correction=qrcode.constants.ERROR_CORRECT_L,
)

# Adicione a URL ao objeto QRCode
codigo_qr.add_data(url_do_site)
codigo_qr.make(fit=True)

# Crie uma imagem do código QR
imagem_qr = codigo_qr.make_image(fill_color="black", back_color="white")

# Salve a imagem do código QR em um arquivo
imagem_qr.save("codigo_qr_site.png")
