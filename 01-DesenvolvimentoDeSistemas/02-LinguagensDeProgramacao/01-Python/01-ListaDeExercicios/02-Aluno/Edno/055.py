# (01-Gabarito/055.py)) Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

pesos = []

print('')
print('')

for i in range(0,5):
    pesos.append(float(input('Digite o peso da {}ª pessoa\t: '.format(i+1))))

pesos.sort()

print('')
print('')

print('O maior peso é {} Kg e o menor peso é {} Kg.'.format(pesos[0],pesos[len(pesos)-1]))

