print("""
074) Crie um programa que vai gerar cinco números aleatórios e colocar em
uma tupla. Depois disso, mostre a listagem de números gerados e também
indique o menos e o maior valor que estão na tupla.
""")

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1,10), randint(1, 10))
print('Os números sorteados foram:')
for n in numeros:
    print('{} '.format(n), end='')
print('\nO maior valor sorteado foi: {} '.format(max(numeros)))
print('O menos valor sorteado foi: {} '.format(min(numeros)))



