print("""
091) Crie um programa onde 4 jogadas joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado. 
""")

from random import randint
from time import sleep

jogadas = {}
vencedores = []
larguraDaTabela = 30
posicaoDoMaiorResultado = 0

print('-'*larguraDaTabela)
print(f'{"Sorteio":^{larguraDaTabela}}')
print('-'*larguraDaTabela)

for numero in range(4):
    jogador=f'Jogador {numero+1:02d}'
    numeroSorteado = randint(1, 6)
    jogadas[jogador] = numeroSorteado
   
    print(f'{jogador}: {numeroSorteado}')
    sleep(0.5)

    for pontuacao in range(len(vencedores)):
        if jogadas[jogador] <= vencedores[pontuacao][1]:
            posicaoDoMaiorResultado += 1
    vencedores.insert(posicaoDoMaiorResultado, [jogador, jogadas[jogador]])
    posicaoDoMaiorResultado = 0

print('-'*larguraDaTabela)
print(f'{"Resultado":^{larguraDaTabela}}')
print('-'*larguraDaTabela)
for chave, resultado in enumerate(vencedores):
    print(f'{chave+1}º lugar: {resultado[0]}: {resultado[1]} pontos')
    sleep(0.5)
print('-'*larguraDaTabela)
