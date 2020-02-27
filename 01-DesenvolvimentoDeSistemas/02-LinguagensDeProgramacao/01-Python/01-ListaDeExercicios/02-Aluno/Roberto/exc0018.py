print('[-- Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. --]\n')
from math import sin, cos, tan, radians
angulo = float(input("Digite o valor do ângulo(em graus): "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print("\nOs Valores do seno, cosseno e tangente do ângulo {}° são respectivamente {:.2f} , {:.2f} e {:.2f} " .format(angulo,seno,cosseno,tangente))


