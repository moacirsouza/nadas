print("""
088) Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
""")

from random import randint

titulo = ' Palpitador "Anabela de Malhadas" para MEGA-SENA '
todosOsJogos = []

### Para quem não conhece a Anabela de Malhadas, segue a
### referência: https://www.youtube.com/watch?v=hIrRNFa8OiA
locutor = ['Você é um ponto, Anabela!',
           'Olá Anabela! Madrugou!',
           'O quê???',
           'Gosto tanto de te ouvir, Anabela!',
           'Estou-me a ficar consigo, Anabela',
           'Anabela! Vamos lá ou não?',
           'Anabela... A ver se nos entendemos...',
           'Vai me dar o fanico consigo, Anabela!',
           'Anabela, você está a me fazer transpirar. A sério.',
           'É MAIS de quatro e meio, Anabela!',
           'Mais para frente!',
           'Vai me dar o treco consigo, Anabela!',
           'Ai Jesus, para o que te deu hoje!',
           'Quatro quinhentos e qualquer coisa! Diga!']

print('-'*len(titulo))
print(titulo)
print('-'*len(titulo))

quantidadeDeJogos = int(input('Quantos jogos eu devo sortear? ').strip())

for jogo in range(quantidadeDeJogos):
    todosOsJogos.append([])
    for numero in range(6):
        while True:
            valorGerado = randint(1,60)
            if valorGerado not in todosOsJogos[jogo]:
                todosOsJogos[jogo].append(valorGerado)
                break
    print(f'Jogo {jogo+1}: {todosOsJogos[jogo]}')
print('-'*len(titulo))
print(f'Locutor: {locutor[randint(0, len(locutor)-1)]}')
