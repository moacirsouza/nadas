print("""
009) Faça um programa que leia um número inteiro qualquer e mostre na tela
a sua tabuada. 
""")

numero = int(input('Digite um número inteiro: '))
titulo = 'Tabuada do ' + str(numero)

print('+{:-^16}+'.format(titulo))
print('| {:>2} x  1 = {:>4} |'.format(numero,numero*1))
print('| {:>2} x  2 = {:>4} |'.format(numero,numero*2))
print('| {:>2} x  3 = {:>4} |'.format(numero,numero*3))
print('| {:>2} x  4 = {:>4} |'.format(numero,numero*4))
print('| {:>2} x  5 = {:>4} |'.format(numero,numero*5))
print('| {:>2} x  6 = {:>4} |'.format(numero,numero*6))
print('| {:>2} x  7 = {:>4} |'.format(numero,numero*7))
print('| {:>2} x  8 = {:>4} |'.format(numero,numero*8))
print('| {:>2} x  9 = {:>4} |'.format(numero,numero*9))
print('| {:>2} x 10 = {:>4} |'.format(numero,numero*10))
print('+'+('-'*16)+'+')
