# Gerador de QR Code

Este é um script em Python para gerar QR Codes a partir de texto fornecido pelo usuário. O QR Code gerado pode ser exibido e salvo como uma imagem PNG.

## Funcionalidades
- Converta qualquer texto em um QR Code.
- Exiba o QR Code diretamente na tela.
- Salve o QR Code como um arquivo PNG com um nome personalizado.

## Pré-requisitos

Certifique-se de que você tenha o Python instalado no seu sistema. Você também precisará das seguintes bibliotecas Python:

- `pyqrcode`
- `pypng`

Você pode instalá-las usando o pip:

```bash
pip install pyqrcode pypng
```

## Como Usar

1. Clone ou baixe este repositório para sua máquina local

`git clone https://github.com/isaccanedo/QR_code_generation`

2. Execute o script:

   ```bash
   python qr_code_generator.py
   ```

3. Siga as instruções na tela:
   - Insira o texto que deseja converter em QR Code.
   - Insira o nome desejado para o arquivo PNG (sem extensão).
4. O script irá:
   - Gerar o QR Code.
   - Exibi-lo na tela (opcional).
   - Salvá-lo como um arquivo PNG no mesmo diretório do script.

## Exemplo

### Entrada:
```
Enter text to convert to QR Code: Olá, Mundo!
Enter image name to save (without extension): ola_mundo
```

### Saída:
- Um QR Code exibido na tela.
- Um arquivo PNG chamado `ola_mundo.png` salvo no diretório atual.

## Visão Geral do Código

```python
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
```

## Notas
- Certifique-se de instalar todas as bibliotecas necessárias antes de executar o script.
- O script salva o arquivo PNG do QR Code no mesmo diretório onde é executado.
