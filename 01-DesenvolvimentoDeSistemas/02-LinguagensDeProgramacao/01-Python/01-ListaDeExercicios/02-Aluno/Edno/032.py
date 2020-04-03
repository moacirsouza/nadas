# (01-Gabarito/032.py)) Faça um programa que leia um ano qualquer e moste se ele é BISSEXTO.
# Pra ser bissexto:
# Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100
# Condição 2: Ser múltiplo de 400 (se for múltiplo de 400 automaticamente é de 4)

ano = int(input('Digite um ano qualquer da história\t: '))

bissexto = (ano%4 == 0 and ano%100 !=0) or (ano%400==0)

texto = ' é bissexto!!!!'

if not bissexto:
    texto = ' não' + texto

print(str(ano) + texto)

