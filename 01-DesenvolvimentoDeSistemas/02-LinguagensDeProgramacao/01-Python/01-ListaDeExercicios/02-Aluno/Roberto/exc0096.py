print("""
096) Faça um programa que tenha uma função chamada
Área(), que recebe as dimensões de um terreno retangular(largua e comprimento) e mostre a área do terreno.
""")
def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


# Programa Principal
print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m):  '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)