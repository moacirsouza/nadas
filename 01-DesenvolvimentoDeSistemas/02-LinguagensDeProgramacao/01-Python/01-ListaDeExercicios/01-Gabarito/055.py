print("""
055) Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o
maior e o menor peso lidos.
""")

for pessoa in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(pessoa)).strip())

    if pessoa == 1:
        maior = menor = peso
    
    if peso > maior:
        maior = peso
    
    if peso < menor:
        menor = peso

print("""
O maior peso informado foi {} Kg.
O menor peso informado foi {} Kg.
""".format(maior, menor))
