# (01-Gabarito/064.py)) Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


numero = 0
soma = 0
cont = 0
while numero != 999:
    numero = int(input('Digite o número que quiser. Pra sair, digite 999\t: '))
    if numero != 999:
        cont += 1
        soma = soma+numero

print('')
print('{} números foram digitados. A soma dos número é {}.'.format(cont, soma))