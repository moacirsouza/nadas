# (01-Gabarito/034.py)) Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
# Mais cálculo de empresa esquerdista. Ninguém. NINGUÉM, ganha aumento de 10 ou 15 %
# uhaehuaehuaehueauh

print('*'*100)
print('* Recurso Oriundo de Unidades de Benfeitorias não Outorgadas - (ROUBO)' + ' '*29 + '*')
print('*'*100)
salario = float(input('* Diga qual é o çeu çalário, cumpanheiro\t: '))
print('')

aumento = 1.1
if salario <= 1250:
    aumento = 1.15

salario = salario * aumento

print('Cumpanheiro. seu salário aumentou pra R$ ' + str(salario) + '. Não esquece do pedaço da gente.')




