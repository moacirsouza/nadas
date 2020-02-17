print('[-- Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. --]\n')
from math import sin,cos,tan,degrees

angulo = degrees(float(input('Informe o valor de um ângulo: ')))
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)
print('Os valor de Seno, Cosseno e Tangente do ângulo {} são, respectivamente:\nSeno: {}\nCosseno: {}\nTangente: {}'.format(angulo, seno, cosseno, tangente))
