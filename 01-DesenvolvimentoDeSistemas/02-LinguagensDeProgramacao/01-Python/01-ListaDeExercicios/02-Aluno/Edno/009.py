# (01-Gabarito/009.py)) Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input('Digite um número\t: '))

titulo = 'Tabuada de ' + str(numero)
espacos = 80 - len(titulo)-3
print('*'*80)
print('* ' + titulo + ' '*espacos + '*')
print('*'*80)
for i in range(1,11):
    print('* ' + str(numero) + ' + ' + str(i) + ' = ' + str(numero+i) + '\t | ' + str(numero) + ' * ' + str(i) + ' = ' + str(numero*i) + '\t | ' + str(numero) + ' - ' + str(11-i) + ' = ' + str(11-i-numero) + '\t | ' + str(numero) + ' / ' + str(i) + ' = ' + str(round((numero/i),2)) + '\t |')

print('*'*80)
