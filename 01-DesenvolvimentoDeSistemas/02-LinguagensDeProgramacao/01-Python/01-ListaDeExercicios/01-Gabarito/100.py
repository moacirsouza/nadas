print("""
100) Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares
sorteados pela função anterior.
""")

from random import randint
from time import sleep

numeros = []

def sorteia(lista):
    
    print('Números sorteados: ')

    for passo in range(5):
        sorteado = randint(1, 10)
        print(f'{passo+1}º: {sorteado} ')
        sleep(0.5)
        lista.append(sorteado)
    print('')


def somaPar(lista):

    soma = 0

    for item in lista:
        if item%2 == 0:
            soma += item

    print(f'A soma dos números sorteados é {soma}')


sorteia(numeros)
somaPar(numeros)
