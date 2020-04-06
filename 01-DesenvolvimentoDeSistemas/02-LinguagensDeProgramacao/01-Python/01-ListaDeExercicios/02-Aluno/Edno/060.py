# (01-Gabarito/060.py)) Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5!=5x4x3x2x1=120

def fatorial(valor):
    if valor > 1:
        valor = valor * fatorial(valor-1)
    return valor

numero = int(input('Digite um número inteiro qualquer\t: '))

print('O fatoria de {} é {}'.format(numero, fatorial(numero)))
