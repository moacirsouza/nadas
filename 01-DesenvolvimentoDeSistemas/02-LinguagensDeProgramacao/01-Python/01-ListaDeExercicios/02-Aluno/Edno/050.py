# (01-Gabarito/050.py)) Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o

soma = 0
for i in range(0,6):
    numero = int(input('Digite o {} número\t: '.format(i)))
    if numero % 2 != 0:
        soma = soma + numero

print('')
print('A soma dos números ímpares é {}'.format(soma))





