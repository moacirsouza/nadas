print("""
074) Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
valor que estão na tupla.
""")

from random import random
listaTemporaria = []

for contador in range(0,5):
    listaTemporaria += [random()]

tuplaComCincoNumerosAleatorios = tuple(listaTemporaria)

print(f'A tupla gerada foi: {tuplaComCincoNumerosAleatorios}.')
print(f'O maior número da tupla é {max(tuplaComCincoNumerosAleatorios)}.')
print(f'O menor número da tupla é {min(tuplaComCincoNumerosAleatorios)}.')
