print("""
086) Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos
pelo teclado. No final, mostre a matriz na tela com a formatação correta.
""")

tamanhoDaMatriz = 3
matriz = []
saida = ''
titulo = f' Usando números inteiros preencha \
a matriz {tamanhoDaMatriz}x{tamanhoDaMatriz} a seguir '

print('-'*len(titulo))
print(titulo)
print('-'*len(titulo))

for linha in range(tamanhoDaMatriz):
    matriz.append([])
    for coluna in range(tamanhoDaMatriz):
        numero = int(input(f'Célula [{linha},{coluna}]: ').strip())
        matriz[linha].append(numero)
        saida += f'[ {matriz[linha][coluna]:^3} ]'
    saida += '\n'

print('-'*len(titulo))
print(saida[:-1])
print('-'*len(titulo))
