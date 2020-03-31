# (01-Gabarito/008.py)) Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

numero = float(input('Digite o número de metros\t: '))

print(str(numero) + ' metro(s) equivale a ' + str(numero*100) + ' centímetros')
print(str(numero) + ' metro(s) equivale a ' + str(numero*1000) + ' milímetros')