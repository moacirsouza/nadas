print("""
050) Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o 
""")

somaDosPares = 0

for entrada in range(1,7):
    temporario = int(input('Informe o número {}: '.format(entrada)))
    if temporario % 2 == 0:
        somaDosPares += temporario

print('\nA soma dos pares é: {}'.format(somaDosPares))
