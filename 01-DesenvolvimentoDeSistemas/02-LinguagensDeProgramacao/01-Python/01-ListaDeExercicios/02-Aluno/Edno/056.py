# (01-Gabarito/056.py)) Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#       - A média de idade do grupo.
#       - Qual é o nome do homem mais velho.
#       - Quantas mulheres tem menos de 20 anos.

nome = ["","","",""]
idade = [0,0,0,0]
sexo = ["","","",""]

soma_idades = 0
mais_velho = 0
nome_mais_velho = ''
cocotinhas = 0

for i in range(0,4):
    print('-'*50)
    nome[i] = str(input('Digite seu nome\t\t: '))
    sexo[i] = str(input('Digite seu sexo (M,F)\t: '))
    idade[i] = int(input('Digite sua idade\t: '))

    if sexo[i] == 'M' and idade[i] > mais_velho:
        nome_mais_velho = nome[i]

    if sexo[i] == 'F' and idade[i] < 20:
        cocotinhas = cocotinhas + 1

    soma_idades = soma_idades + idade[i]

print('')
print('')
print('Nossos Candidatos:')
print('')
print('Nome \t\t\tSexo \t\t\tIdade')
for i in range(0,4):
    print('{} \t\t\t{} \t\t\t{}'.format(nome[i], sexo[i], idade[i]))
print('')
print('O homem mais velho é {}, a média de idades é {} e a quantidade de mulheres com menos de 20 anos é {}'.format(nome_mais_velho, soma_idades/4, cocotinhas))

#for i in range(0,4):
#    print('{} de {} anos é do sexo {}'.format(nome[i], idade[i],sexo[i]))

