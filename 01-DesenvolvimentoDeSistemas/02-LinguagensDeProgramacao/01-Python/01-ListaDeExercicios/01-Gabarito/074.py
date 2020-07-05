print("""
074) Crie um programa que vai gerar cinco números aleatórios e colocar em
uma tupla. Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.
""")

from random import random

### Solução 0: Essa é uma maneira mais elegante de resolver a questão, no
### entanto, como combinado, tentaremos evitar usar conhecimentos que ainda
### não foram ministrados nos módulos do Curso em Vídeo, portanto, o uso de
### uma lista ainda não é permitido neste ponto.
# listaTemporaria = []
# for contador in range(0,5):
#     listaTemporaria += [random()]
# tuplaComCincoNumerosAleatorios = tuple(listaTemporaria)

### Solução 1: A tupla é imutável, então, a única maneira de criar números
### aleatórios nas cinco posições é chamar o método "random()" em cada uma
### das posições individualmente, durante a declaração da variável.
tuplaComCincoNumerosAleatorios = (random(), random(),
                                  random(), random(),
                                  random())

print(f'A tupla gerada foi: {tuplaComCincoNumerosAleatorios}.')
print(f'O maior número da tupla é {max(tuplaComCincoNumerosAleatorios)}.')
print(f'O menor número da tupla é {min(tuplaComCincoNumerosAleatorios)}.')
