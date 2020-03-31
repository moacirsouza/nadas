# (01-Gabarito/006.py)) Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math

numero = int(input('Digite um número\t: '))

print('O dobro de ' + str(numero) + ' é: ' + str(numero*2))
print('O triplo de ' + str(numero) + ' é: ' + str(numero*3))
print('A raiz quadrada de ' + str(numero) + ' é: ' + str(math.sqrt(numero)))

