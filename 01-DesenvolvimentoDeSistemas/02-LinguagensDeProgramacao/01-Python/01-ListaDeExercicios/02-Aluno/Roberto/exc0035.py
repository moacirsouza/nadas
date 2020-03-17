print("""
035) Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
elas podem ou não formar um triângulo.
""")
L1 = float(input('Digite o comprimento da primeira reta: '))
L2 = float(input('Digite o comprimento da segunda reta: '))
L3 = float(input('Digite o comprimento da terceira reta: '))
if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print('Os segmentos formam um triângulo: ')
else:
    print('Os segmentos não formam um triângulo')

