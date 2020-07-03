print("""
080) Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção (sem usar o
sort()). No final, mostre a lista ordenada na tela.
""")

### A solução final foi baseada no código postado no seguinte comentário do
### usuário João Pedro Calixto, no vídeo de resolução do Exercício 080 do
### Curso de Python do Curso em Vídeo: https://bit.ly/2D78pyX (Ver comentário
### em destaque)

### TODO: Documentar melhor a lógica usando comentários
listaComCincoNumeros = []
posicaoDeInsercao = 0

for valor in range(5):
    entrada = int(input(f'Informe o {valor+1}º número: '))

    for indice, valor in enumerate(listaComCincoNumeros):
        if entrada > valor:
            posicaoDeInsercao = indice + 1
    
    listaComCincoNumeros.insert(posicaoDeInsercao, entrada)
    posicaoDeInsercao = 0
    
print(f'A lista, ordenada é: {listaComCincoNumeros}')

### TODO: Melhorar a visualização do passo a passo abaixo
# 
# Exemplo de entrada: 9, 0, 2, 1, 6
# Observação: pdi = posição de inserção
#
# - programa principal
# iteracao | entrada  | for interno | pdi | saida   
#     0    |    9     |     n/a     |  0  | [9]
#     1    |    0     |      *      |  0  | [0, 9]
#     2    |    2     |      +      |  1  | [0, 2, 9]
#     3    |    1     |      -      |  1  | [0, 1, 2, 9]
#     4    |    6     |      \      |  3  | [0, 1, 2, 6, 9]
#
# - for's internos
#
#+-------------------------------------------------------+
#|   | indice | valor | entrada |  entrada > valor | pdi |
#+-------------------------------------------------------+
#| * |    0   |   0   |    0    |       não        |  0  |
#+-------------------------------------------------------+
#| + |    0   |   0   |    2    |       sim        |  1  |
#|   |    1   |   9   |    2    |       nao        |  1  |
#+-------------------------------------------------------+
#| - |    0   |   0   |    1    |       sim        |  1  |      
#|   |    1   |   2   |    1    |       não        |  1  |
#|   |    2   |   9   |    1    |       não        |  1  |
#+-------------------------------------------------------+
#| \ |    0   |   0   |    6    |       sim        |  1  |
#|   |    1   |   1   |    6    |       sim        |  2  |
#|   |    2   |   2   |    6    |       sim        |  3  |
#|   |    3   |   9   |    6    |       não        |  3  |
#+-------------------------------------------------------+
