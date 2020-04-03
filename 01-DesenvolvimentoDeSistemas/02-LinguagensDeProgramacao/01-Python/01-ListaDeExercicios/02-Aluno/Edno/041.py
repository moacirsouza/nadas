# [041](01-Gabarito/041.py)) A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a idade:
#       - Até 9 anos: MIRIM
#       - Até 14 anos: INFANTIL
#       - Até 19 anos: JÚNIOR
#       - Até 25 anos: SÊNIOR
#       - Acima: MASTER

from datetime import date

ano_corrente = date.today()
ano_corrente = ano_corrente.year

nascimento = int(input('Digite o ano de nascimento do atleta\t: '))

print('')
if nascimento < 1930:
    print('Amigo, deixe de ser mentiroso que um homem com mais de 89 anos deve é curtir os netos e bisnetos.')
else:
    nascimento = ano_corrente - nascimento
    print('Você tem {} anos.'.format(nascimento))
    if nascimento > 0 and nascimento <= 9:
        print('Sua categoria é Mirim')
    elif nascimento > 9 and nascimento <= 14:
        print('Sua categoria é Infantil')
    elif nascimento > 14 and nascimento <= 19:
        print('Sua categoria é Júnior (Meu último nome. :D)')
    elif nascimento > 19 and nascimento <= 25:
        print('Sua categoria é Sênior')
    else:
        print('Sua categoria é Master. Mas master quer dizer muito velho pra competir. :P')
