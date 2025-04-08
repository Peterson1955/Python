# Documetação: https://www.pypi.org/project/qrcode/

import qrcode

dados = input('Digite a informação que deseja gerar o QRCode: ')

img = qrcode.make(dados)

arquivo = input('Digite o nome do para salvar o QRCode: ')

img.save(arquivo)

print('QRCode gerado com sucesso!')