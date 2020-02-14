print('[-- Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada --]\n')
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero ** (1/2)
print('O dobro do número {} é {}. O triplo é {}. E a raiz quadrada é {:.2f}.'.format(numero,dobro,triplo,raizQuadrada))
