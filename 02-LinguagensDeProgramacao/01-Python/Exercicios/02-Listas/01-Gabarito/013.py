print('[-- Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. --]\n')
salario = float(input('Informe o salário do funcionário: R$ '))
aumento = 0.15
salarioFinal = salario+(salario*aumento)
print('O salário final, com acréscimo de 15%, será R$ {:.2f}'.format(salarioFinal))
