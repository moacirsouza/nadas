print("""
087) Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha. 
""")
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print(matriz)
print('-=' * 30)
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')  # :^5 Centraliza com 5 espaços
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é: {spar}')
for l in range(0, 3):
    scol += matriz[l][2] # a coluna é a mesma, o que irá variar será a linha.
print(f'A soma dos valores da terceira coluna é: {scol}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior} ')