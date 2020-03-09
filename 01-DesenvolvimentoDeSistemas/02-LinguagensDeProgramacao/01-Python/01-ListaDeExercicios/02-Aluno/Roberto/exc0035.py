print("""
034) Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
""")
salariodofuncionario = float(input('Digite o valor do seu salário: '))
if salariodofuncionario > 1250:
    novosalario = salariodofuncionario + (salariodofuncionario*10/100)
else:
    novosalario = salariodofuncionario + (salariodofuncionario*15/100)
print('O seu novo salário será {:.2f}'.format(novosalario))
