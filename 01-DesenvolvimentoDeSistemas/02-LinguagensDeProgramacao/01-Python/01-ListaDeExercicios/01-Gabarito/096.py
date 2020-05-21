print("""
096) Faça um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno.
""")

def areaDeTerreno(largura, comprimento):
    area = largura*comprimento
    print(f'A área do seu terreno é {area}m².')


areaDeTerreno(4, 5)
