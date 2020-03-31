#(01-Gabarito/016.py)) Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela
# a sua porção Inteira. Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

numero = float(input('Digite um número REAL qualquer\t: '))

numero2 = str(numero)
numero2 = numero2.split('.')
print('A parte inteira de ' + str(numero) + ' é ' + numero2[0])