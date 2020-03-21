print("""
035) Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
elas podem ou não formar um triângulo.
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

if lado01+lado02 > lado03:
    if lado01+lado03 > lado02:
        if lado02+lado03 > lado01:
            print('É triângulo.')
else:
    print('Não é triângulo.')
