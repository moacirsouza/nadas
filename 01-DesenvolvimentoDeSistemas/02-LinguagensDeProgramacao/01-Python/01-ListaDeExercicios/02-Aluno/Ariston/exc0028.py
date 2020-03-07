print("""
\033[1;37;44m 028) \033[m Crie um programa em PYTHON que: faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
""")
from random import randint
sorte = int(input('Pensei em um numero entre 0 a 5.\nAdivinhe este número: '))
numero = randint(0,5)
if numero == sorte:
    print('Acertou! Eu pensei mesmo no número {}.'.format(numero))
else:
    print('Errou eu pensei no número {}, que pena!.'.format(numero))