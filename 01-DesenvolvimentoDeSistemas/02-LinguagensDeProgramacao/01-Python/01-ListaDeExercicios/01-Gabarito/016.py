print("""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6. 
""")
### A função trunc remove a parte inteira de um número real. Não é necessário
### importar toda a biblioteca math, apenas a função trunc. Isso economiza
### memória e deixa o código mais limpo.
from math import trunc
real = float(input('Digite um número real: '))
parteInteira = trunc(real)
print('A parte inteira do número {} é {}.'.format(real, parteInteira))
