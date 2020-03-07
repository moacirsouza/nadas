print("""
\033[1;37;44m 034) \033[m Crie um programa em PYTHON que: pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a \033[1;37;44mR$1.250,00\033[m, calcule um aumento de \033[7m10%\033[m.
Para os inferiores ou iguais, o aumento é de \033[7m15%\033[m.
""") 
salario = float(input('Qual o seu Salario: R$ '))
teto = 1250.00
if salario > teto:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
novoSalario = salario+aumento

print('Você terá um aumento de \033[1;35;43m R$ {:.2f}\033[m, logo  seu novo salario é \033[4;37;42m R$ {:.2f}\033[m'.format(aumento,novoSalario))