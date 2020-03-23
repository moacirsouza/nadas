print("""
045) Crie um programa que faça o computador jogar Jokenpô com você.
""")

from random import randint
from time import sleep

menuDoJogador = """Seja bem-vindo(a)! Vamos jogar JoKenPô?
Escolha um dos três:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Sua jogada: """

escolhaDoJogador = int(input(menuDoJogador).strip())
escolhaDoComputador = randint(0, 2)
mensagemFinal = ''
computadorVenceu = 'O Computador venceu.'
computadorPerdeu = 'Parabéns, VOCÊ VENCEU!'
pedraPapelTesoura = ['PEDRA', 'PAPEL', 'TESOURA']
opcaoInvalida = False

resultado = computadorPerdeu

if escolhaDoJogador == escolhaDoComputador:
    resultado = 'EMPATOU!'
elif escolhaDoJogador == 0:
    if escolhaDoComputador == 1:
        resultado = computadorVenceu 
elif escolhaDoJogador == 1:
    if escolhaDoComputador == 2:
        resultado = computadorVenceu
elif escolhaDoJogador == 2:
    if escolhaDoComputador == 0:
        resultado = computadorVenceu
else:
    opcaoInvalida = True
    mensagemFinal = 'OPÇÃO INVÁLIDA.'
    resultado = ''

if not opcaoInvalida:
    mensagemFinal += """
+{}+
|{:^27}|
+{}+
| {:^12}| {:^12}|
+{}+
| {:^12}| {:^12}|
+{}+

{}""".format('-'*27,
             'Resultados',
             '-'*27,
             'Você',
             'Computador',
             '-'*27,
             pedraPapelTesoura[escolhaDoJogador],
             pedraPapelTesoura[escolhaDoComputador],
             '-'*27,
             resultado)
    print('\nJO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ!\n')
    sleep(0.5)

mensagemFinal += '\nJogue novamente!'

print(mensagemFinal)
