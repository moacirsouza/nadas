#(01-Gabarito/027.py)) Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente. Ex: Ana Maria de Souza. primeiro=Ana último: Souza.

nome = str(input('Qual é a vossa graça? '))

nome = nome.split(' ')

print('')
print('Seu primeiro nome é: ' + nome[0])
print('Seu último nome é: ' + nome[len(nome)-1])