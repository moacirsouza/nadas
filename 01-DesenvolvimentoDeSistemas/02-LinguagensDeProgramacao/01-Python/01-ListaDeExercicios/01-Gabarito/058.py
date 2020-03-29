print("""
058) Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre
0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
""")

from random import randint

numero = int(input('Digite um número entre 0 e 10: '))
senha = randint(0,10)

### O contador começa com um por causa da primeira solicitação, feita fora do laço.
contador = 1

while numero != senha:
    contador += 1
    maiorOuMenor = 'menor'

    if senha > numero:
        maiorOuMenor = 'maior'
    
    numero = int(input('Errou. Tente um número {}: '.format(maiorOuMenor)))

mensagem = """
Parabéns! Você adivinhou!
Número de tentativas: {}
""".format(contador)

print(mensagem)
