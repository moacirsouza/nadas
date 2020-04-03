#(01-Gabarito/042.py)) Refaça o DESAFIO 035 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
#      - Equilátero: todos os lados iguais
#      - Isósceles: dois lados iguais
#      - Escaleno: todos os lados diferentes

lados=[0,0,0]
descricoes=['Escaleno', 'Isósceles', 'Equilátero']

lados[0] = int(input('Primeiro lado\t: '))
lados[1] = int(input('Segundo lado\t: '))
lados[2] = int(input('Terceiro lado\t: '))

iguais = 0
numero_anterior = 0

for i in range(0,3):
    if i<2:
        if lados[i] == lados[i+1]:
            iguais = iguais + 1

print('')
print('O triângulo que será formado é um triângulo {}'.format(descricoes[iguais]))

