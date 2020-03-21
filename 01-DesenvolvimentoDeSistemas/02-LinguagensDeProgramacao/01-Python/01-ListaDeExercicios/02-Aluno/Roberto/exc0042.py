print("""
042) Refaça o DESAFIO 035 dois triângulos, acrescentando o recurso de mostrar que
tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
""")

print("""
Este programa recebe o valor de três retas e verifica se, com elas,
é possível formar um triângulo. Para isso é importante saber que a
a soma de quaisquer dois lados de um triângulo deve, SEMPRE, ser 
maior que o terceiro lado restante.
""")
L1 = float(input('Digite o comprimento da primeira reta: '))
L2 = float(input('Digite o comprimento da segunda reta: '))
L3 = float(input('Digite o comprimento da terceira reta: '))
if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print('Os segmentos formam um triângulo: ')
    if L1 == L2 == L3:
      print('O triângulo possui os três lados iguais, portanto ele é EQUILÁTERO')
    elif L1 == L2 or L1 == L3 or L2 == L3:
      print('O triângulo possui dois lados iguais, portanto ele é ISÓSCELES')
    else:
      print('O triângulo possui dos três lados diferentes, porém ele é ESCALENO')
else:
    print('Os segmentos não formam um triângulo')
