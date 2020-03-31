print("""
060) Faça um programa que leia um número qualquer
e mostre o seu fatorial.
""")

# from math import factorial
# n = int(input('Digite um número para calcular seu Fatorial: '))
# f = factorial(n)
# print('O fatorial de {} é {}'.format(n, f))

### Outro método, sem uso do módulo math !!

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando  {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

