print("""
039) Faça um programa que leia o ano de nascimento de um jovem e informe, de
acordo com sua idade: 
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
""")
anodenascimento = int(input('Qual o seu ano de nascimento? '))
anoatual = 2020
idade = anoatual - anodenascimento 
tempoquefalta = (18-idade)*12
tempoquepassou = (idade-18)*12
if idade < 18:
    print('Você ainda vai se alistar ao serviço militar, faltam {} meses'.format(tempoquefalta))
elif idade > 18:
    print('Já passou o tempo de alistamento, passaram {} meses'. format(tempoquepassou))
else:
    print('É a hora de se alistar')
    