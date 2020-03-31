#(01-Gabarito/017.py)) Faça um programa que leia o comprimento do cateto
# oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

from math import sqrt

c_oposto = int(input('Qual o comprimento em centímetros do cateto oposto? '))
c_adjacente = int(input('Qual o comprimento em centímetros do cateto adjacente? '))

#hipotenusa = pow(c_oposto, 2) + pow(c_adjacente, 2)
hipotenusa = round(sqrt(pow(c_oposto, 2) + pow(c_adjacente, 2)),2)


print('O cálculo da hipotenusa é: ' + str(c_oposto) + '² + ' + str(c_adjacente) + '² = c², que resulta em ' + str(hipotenusa))

