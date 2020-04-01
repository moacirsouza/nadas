# (01-Gabarito/023.py)) Faça um programa que leia um número de 0 a 9999 e
# mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834. unidade: 4, dezena: 3, cententa: 8, milhar: 1.

numero = int(input('Digite um número entre 1 e 9999, irmão: '))
tipo = ['milhar', 'centena', 'dezena', 'unidade']

if numero <1 or numero >9999:
    print('Seu merda! Eu mandei digitar um número entre 1 e 9999. Não estrague a brincadeira não!!!')
else:
    novo = str(numero)
    for i in range(0, len(novo)):
        print(tipo[i-len(novo)] + ': ' + novo[i])