print("""
099) Faça um programa que tenha uma função chamada maior(), que receba vários
parâmetros com valores inteiros. Seu programa tem que analisar todos os valores
e dizer qual deles é o maior.
""")

def maior(*numeros):
    print(f'O maior número entre {", ".join(map(str, numeros))}, é {max(numeros)}.')

maior(2, 3)
maior(1, 2, 3, 4)
maior(6, 7, 8, 9, 20)
maior(45, 6, 7, 21, 34, 232)
