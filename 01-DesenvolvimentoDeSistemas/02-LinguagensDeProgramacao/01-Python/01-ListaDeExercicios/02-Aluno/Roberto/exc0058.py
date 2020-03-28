print("""
058) Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre
0 e 10. Só que agora o jogador vai tentar adivinhas até acertas, mostrando no final
quantos palpites foram necessários para vencer.
""")
from random import randint
computador = randint(0, 10)
print('Vou pensar num número emtre 0 e 10, você consegue advinhar? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
print('Você acertou com {} tentativas '.format(palpites))

  
