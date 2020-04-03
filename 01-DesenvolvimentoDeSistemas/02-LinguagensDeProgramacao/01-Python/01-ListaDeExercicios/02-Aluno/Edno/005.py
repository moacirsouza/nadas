# (01-Gabarito/005.py)) Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.

numero = int(input('Digite um número\t: '))

print(type(numero))

anterior = numero-1
posterior = numero + 1

print('O número antes de ' + str(numero) + ' é ' + str(anterior) + ' e o número depois de ' + str(numero) + ' é ' + str(posterior))

