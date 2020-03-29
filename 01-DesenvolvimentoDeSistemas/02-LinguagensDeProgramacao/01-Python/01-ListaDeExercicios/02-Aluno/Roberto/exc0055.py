print("""
055) Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o
maior e o menor peso lidos.
""")

maiorpeso = 0
menorpeso = 0

for contador in range (1, 6):
    peso = float(input('Qual o peso da {}a pessoa? '.format(contador)))
    if contador == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso

print('O menor peso foi: {}'.format(menorpeso))
print('O maior peso foi: {}'.format(maiorpeso))



    
