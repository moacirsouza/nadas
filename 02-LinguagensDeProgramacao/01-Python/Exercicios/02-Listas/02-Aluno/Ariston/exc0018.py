import math
print('fazer um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.\n')
angulo = int(input('Digite o angulo: '))
seno=math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print('\nParao o angulo {}° nós temos seno é {:.2f}, cosseno é {:.2f} e tangente é {:.2f}.'.format(angulo,seno,cosseno,tangente))