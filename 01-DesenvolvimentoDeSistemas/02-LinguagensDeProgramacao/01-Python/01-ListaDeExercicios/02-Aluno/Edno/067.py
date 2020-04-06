# (01-Gabarito/067.py)) Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

numero = 1

while numero > 0:
    print('Para sair, digite um número negativo.')
    numero = int(input('Digite um número qualquer\t: '))
    print('')
    if numero > 0:
        for i in range(1,11):
            print('{}\t+\t{}\t=\t{}\t| {}\t*\t{}\t=\t{}\t| {}\t-\t{}\t=\t{}\t|  {}\t/\t{}\t=\t{}\t|'.format(i,numero,numero+i,i,numero,numero*i, 11-i,numero, (10-i+1)-numero, i, numero, round(numero/i,2)))