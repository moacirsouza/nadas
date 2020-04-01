# (01-Gabarito/025.py)) Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome, sr: '))
nome = nome.upper()
if nome.find('SILVA') >- 1:
    print('O sr. é da família Silva. Seu lugar está reservado. Acompanhe-me, por favor.')

print('Sinta-se à vontade.')