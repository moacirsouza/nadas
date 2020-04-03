# (01-Gabarito/039.py)) Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço,
# se é a hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_corrente = date.today()
ano_alistamento = ano_corrente.year - 18
'''
É assim, Moka: O cara que devia se alistar em 2020 tem que ter nascido em 2002.
É só subtrair o ano de alistamento do ano de nascimento. Se for negativo,
falta tempo. Se for positivo, já passou do tempo.
'''

idade = int(input('Digite o ano do seu nascimento, filho\t: '))
ano_nascimento = ano_corrente.year-idade

tempo_para_alistamento = ano_alistamento-ano_nascimento
print('')
if tempo_para_alistamento > 0:
    print('Filho, você deveria ter se alistado há {} anos. Seu irresponsável. Vou fazer você sofrer!'.format(tempo_para_alistamento))
elif tempo_para_alistamento < 0:
    print('Filho, admiro seu entusiasmo, mas falta(m) {} anos para seu alistamento.'.format(tempo_para_alistamento*-1))
else:
    print('Muito bem! Pontual! Gosto assim. Trouxe a documentação de alistamento?')
