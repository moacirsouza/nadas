print('[-- Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa. --]\n')
from math import hypot, sqrt
catetoOposto = float(input('Informe o valor do cateto oposto do triângulo retângulo: '))
catetoAdjacente = float(input('Informe o valor do cateto adjacente do triângulo retângulo: '))

# Calculando a hipotenusa diretamente pela soma dos quadrados dos catetos
hipotenusa = (catetoOposto**2+catetoAdjacente**2)**(1/2)
print('Calculando a hipotenusa diretamente pela soma dos quadrados dos catetos: {}'.format(hipotenusa))

# Calculando a hipotenusa utilizando o método hypot do módulo math
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print('Calculando a hipotenusa utilizando o método "hypot" da módulo "math": {}'.format(hipotenusa))

# Calculando a hipotenusa utilizando o método sqrt do módulo math
hipotenusa = sqrt(catetoOposto**2+catetoAdjacente**2)
print('Calculando a hipotenusa utilizando o método "sqrt" da módulo "math": {}'.format(hipotenusa))
