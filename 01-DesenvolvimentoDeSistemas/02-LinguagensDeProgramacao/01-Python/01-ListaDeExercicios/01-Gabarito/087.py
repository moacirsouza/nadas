print("""
087) Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores somaDosPares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
""")

tamanhoDaMatriz = 3
matriz = []
saida = ''
somaDosPares = somaDosNumerosDaTerceiraColuna = 0
titulo = f' Usando números inteiros preencha \
a matriz {tamanhoDaMatriz}x{tamanhoDaMatriz} a seguir '

print('-'*len(titulo))
print(f'{titulo}')
print('-'*len(titulo))

for linha in range(tamanhoDaMatriz):
    matriz.append([])
    for coluna in range(tamanhoDaMatriz):
        numero = int(input(f'Célula [{linha},{coluna}]: ').strip())
        
        if numero%2 == 0:
            somaDosPares += numero

        if coluna == 2:
            somaDosNumerosDaTerceiraColuna += numero

        matriz[linha].append(numero)
        saida += f'[ {matriz[linha][coluna]:^3} ]'
    saida += '\n'

maiorValorDaSegundaLinha = max(matriz[1])

print('-'*len(titulo))
print(saida[:-1])
print('-'*len(titulo))
print(f'A) A soma dos valores pares é {somaDosPares}.')
print(f'B) A soma dos valores da terceira coluna é {somaDosNumerosDaTerceiraColuna}.')
print(f'C) O maior valor da segunda linha é {maiorValorDaSegundaLinha}.')
