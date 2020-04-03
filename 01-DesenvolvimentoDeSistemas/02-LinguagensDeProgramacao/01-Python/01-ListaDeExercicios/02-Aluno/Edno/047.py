# (01-Gabarito/047.py)) Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.


print('')
print('Ímpar\t\t\tPar')
for i in range(1,51):
    if(i%2 != 0):
        print('{}\t\t\t{}'.format(i, i+1))

