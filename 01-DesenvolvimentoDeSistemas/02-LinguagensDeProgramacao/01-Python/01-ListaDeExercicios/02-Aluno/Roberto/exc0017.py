print('[-- Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa. --]\n')
from math import hypot
catetooposto = int(input("Digite o valor do Cateto Oposto: "))
catetoadjacente = int(input("Digite o valor do Cateto Adjacente: "))
hipotenusa = hypot(catetooposto, catetoadjacente)
print("O valor da Hipotenusa, cujo cateto oposto é {} e o cateto adjacente é {} é {} " .format(catetooposto, catetoadjacente, hipotenusa))


