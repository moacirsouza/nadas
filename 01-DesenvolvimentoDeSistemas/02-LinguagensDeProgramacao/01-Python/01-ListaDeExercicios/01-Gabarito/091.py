print("""
091) Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado. 
""")

from random import randint

jogadores = {}
vencedores = {'1º':{}, '2º':{}, '3º':{}, '4º':{}}
larguraDaTabela = 30
contador = 0

print('-'*larguraDaTabela)
print('{:^{centralizador}}'.format('Sorteio', centralizador=larguraDaTabela))
print('-'*larguraDaTabela)

for numero in range(4):
    numeroSorteado = randint(1, 6)
    jogadores[f'Jogador {numero+1:02d}'] = numeroSorteado
    # jogadores[f'{numero+1}º'] = numeroSorteado
    
    print(f'Jogador {numero+1:02d}: {numeroSorteado} ')

    # for indice in range(len(vencedores)):
    #     print(indice, contador, numeroSorteado)
    #     #print(vencedores[f'{indice+1}º'])
    #     if numeroSorteado > vencedores[f'{indice+1}º'].get(f'Jogador {indice+1:02d}', -1):
    #         print(vencedores[f'{indice+1}º'].get(f'Jogador {indice+1:02d}', -1))
    #         print('nao existe')
    #         contador += 1
    #     vencedores.update(jogadores)
    #     contador = 0

# for chave, valor in jogadores.items():
#     print(f'Chave: {chave}. Valor: {valor}')
#     if 

# lista = []
# cont = 0
# for c in range(0, 5):
#     x = int(input('Qual seu valor? '))
#     for t in range(0, len(lista)):
#         if x > lista[t]:
#             cont = cont + 1
#     print(f'O valor {x} foi adicionado na posição {cont}')
#     lista.insert(cont, x)
#     cont = 0
# print(lista)

print('-'*larguraDaTabela)
print('{:^{centralizador}}'.format('Resultado', centralizador=larguraDaTabela))
print('-'*larguraDaTabela)

print(jogadores)
print(vencedores)
