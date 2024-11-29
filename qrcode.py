import pyqrcode

# Solicitar o texto para converter em QR Code
qr_text = input("Enter text to convert to QR Code: ")

# Gerar o QR Code
qr_code = pyqrcode.create(qr_text)

# Exibir o QR Code (opcional)
qr_code.show()

# Solicitar o nome do arquivo para salvar a imagem
image_name = input("Enter image name to save (without extension): ")

# Salvar o QR Code como um arquivo PNG
qr_code.png(f"{image_name}.png", scale=6)

print(f"QR Code saved as {image_name}.png")
