print("""
050) Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o 
""")
somadospares = 0
for contador in range (1, 7):
    numero = int(input('Digite o número: '))
    if numero % 2 == 0:
        somadospares += numero
print('A soma dos pares foi: {}'.format(somadospares))



