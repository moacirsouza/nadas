# (01-Gabarito/033.py)) Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numeros=[0.0,0.0,0.0]
for i in range(0,3):
    numeros[i] = float(input('Digite um número. Qualquer número. Eu vou te dizer quel é o menor deles. '))

numeros.sort()
print('')
print('O menor número é ' + str(round(numeros[0],2)))

