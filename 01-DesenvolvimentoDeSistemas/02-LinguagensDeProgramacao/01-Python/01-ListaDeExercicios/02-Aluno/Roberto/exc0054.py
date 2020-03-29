print("""
054) Crie um programa que leia o ano de nascimento de sete
pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.
""")

from datetime import date
anoatual = date.today().year
somadasmaioresidades = 0
somadasmenoresidades = 0
for contador in range (1, 8):
    anodenascimento = int(input('Ano de Nascimento: '))
    if (anoatual - anodenascimento) >= 21:
        somadasmaioresidades += 1 
    else:
        somadasmenoresidades += 1
print('Quantidade de pessoas de maioridade: {}'.format(somadasmaioresidades))
print('Quantidade de pessoas de menoridade: {}'.format(somadasmenoresidades)) 

