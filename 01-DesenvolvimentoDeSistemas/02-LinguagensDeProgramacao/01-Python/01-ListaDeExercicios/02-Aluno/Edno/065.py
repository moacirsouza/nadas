# (01-Gabarito/065.py)) Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


continuar = 1

maior = 0
menor = 999999999
cont = 0
soma = 0

while continuar == 1:
    numero = int(input('Digite qualquer número inteiro\t: '))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

    soma = soma + numero
    cont += 1

    print('')
    continuar = int(input('Continuar a digitar? [1] - SIM. Para não, digite qualquer outro número.'))

print('O maior número é {}, o menor número é {}. {} números foram digitados e a média é {}'.format(maior, menor, cont, round(soma/cont,2)))