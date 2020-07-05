print("""
042) Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:
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

lado01 = float(input('Digite o valor do lado 01: ').strip())
lado02 = float(input('Digite o valor do lado 02: ').strip())
lado03 = float(input('Digite o valor do lado 03: ').strip())

if lado01+lado02 > lado03 and \
   lado01+lado03 > lado02 and \
   lado02+lado03 > lado01:
    if lado01 == lado02 == lado03:
        tipoDeTriangulo = 'Equilátero'
    elif lado01 == lado02 or lado01 == lado03 or lado02 == lado03:
        tipoDeTriangulo = 'Isósceles'
    else:
        tipoDeTriangulo = 'Escaleno'
    print('É um triângulo {}.'.format(tipoDeTriangulo))
else:
    print('Não é triângulo.')
