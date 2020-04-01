# (01-Gabarito/038.py)) Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#       - O primeiro valor é maior
#       - O segundo valor é maior
#       - Não existe valor maior, os dois são iguais

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

if numero1 > numero2:
    print('{} é maior que {}'.format(numero1, numero2))
elif numero1 < numero2:
    print('{} é menor que {}'.format(numero1, numero2))
else:
    print('{} é igual a {}'.format(numero1, numero2))

print('.')
