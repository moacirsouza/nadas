print("""
034) Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um
aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
""")

### Entrada do programa: Recebe o salário como um número real ("float").
salario = float(input('Informe o salário do funcionário: R$ '))
aumento10 = 0.1
aumento15 = 0.15

if salario > 1250:
    salario += salario*aumento10
else:
    salario += salario*aumento15

print('Um aumento de 10% no salário informado é igual a R$ \
{:.2f}'.format(salario))
