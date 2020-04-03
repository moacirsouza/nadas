# Faça um programa que calcule a soma entre todos os números ímpares que
# são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0

for i in range(1,501, 2):
    if i % 3 == 0:
        soma = soma + i
        print('{} é múltiplo de 3. A soma dos múltiplos de 3 ímpares é {}'.format(i, soma))

print('A soma total de todos os números múltiplos de 3 que são ímpares é {}'.format(soma))


