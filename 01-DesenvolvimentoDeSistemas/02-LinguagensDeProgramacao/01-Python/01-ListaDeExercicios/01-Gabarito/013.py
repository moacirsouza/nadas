print("""
013) Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
salário, com 15% de aumento. 
""")

salario = float(input('Informe o salário do funcionário: R$ '))
aumento = 0.15

salarioFinal = salario+(salario*aumento)

print('O salário final, com acréscimo de 15%, será R$ \
{:.2f}'.format(salarioFinal))

### A fórmula a seguir é uma forma mais reduzida de calcular 15%
### de aumento de qualquer valor
# salarioFinal = salario*1.15
# print('O salário final, com acréscimo de 15%, será R$ \
# {:.2f}'.format(salarioFinal))