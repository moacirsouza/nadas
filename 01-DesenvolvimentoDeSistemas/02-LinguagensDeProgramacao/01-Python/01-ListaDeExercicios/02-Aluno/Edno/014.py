# (01-Gabarito/014.py)) Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
# Com uma ajuda do Google... (oC x 9) / 5) + 32

temp = float(input('Qual a temperatura em Celsius???? '))
crente = round(((temp*9)/5)+32,2)
print('')
print(str(temp) + 'ºC equivale a ' + str(crente) + 'ºF.')
