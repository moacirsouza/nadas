# (01-Gabarito/030.py)) Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite o número\t: '))

if numero % 2 == 0:
    print(str(numero) + ' é par.')
else:
    print(str(numero) + ' é ímpar.')