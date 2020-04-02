# (01-Gabarito/046.py)) Faça um programa que mostre na tela uma contagem regressiva para o
# estouro de fogos de artifício, indo de 10 até 0, com pausa de 1 segundo entre eles.

from time import sleep

print('')
print('Vamos lá! Contagem regressiva!!!')
print('')
for i in range(10,0, -1):
    print(i)
    sleep(1)

print('')
print('Fogos!!!!')