import qrcode

# URL para o QR Code apontar (substitua pela URL do seu backend)
url = "http://localhost:5000/scanner/qr_code_id"

# Gera o QR Code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url)
qr.make(fit=True)

# Cria a imagem do QR Code
img = qr.make_image(fill="black", back_color="white")
img.save("meu_qrcode.png")

print("QR Code gerado com sucesso!")
