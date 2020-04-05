# (01-Gabarito/054.py)) Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano_atual = date.today()
ano_atual = ano_atual.year

idades = [0,0,0,0,0,0,0]

for i in range(0,7):
    idades[i] = int(input('Digite o ano de nascimento da {}ª pessoa\t: '.format(i+1)))

print('')
print('')
for idade in idades:
    texto = 'é de maior'
    if(ano_atual-idade < 18):
        texto = 'é de menor'

    print('A pessoa que nasceu em {} tem {} anos e {}'.format(idade, ano_atual-idade, texto))
    #print(idade)
