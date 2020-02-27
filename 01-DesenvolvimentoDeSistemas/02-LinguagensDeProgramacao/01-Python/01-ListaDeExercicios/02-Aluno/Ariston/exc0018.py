import math
print('fazer um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.\n')
angulo = float(input('Digite o angulo (em graus): '))
seno=math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('\nParao o angulo {}° nós temos seno é {:.2f}, cosseno é {:.2f} e tangente é {:.2f}.'.format(angulo,seno,cosseno,tangente))