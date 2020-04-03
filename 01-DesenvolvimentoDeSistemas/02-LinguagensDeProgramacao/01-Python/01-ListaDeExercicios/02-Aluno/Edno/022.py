#(01-Gabarito/022.py)) Crie um programa que leia o nome completo de uma pessoa e mostre:
# a) O nome com todas as letras maiúsculas;
# b) O nome com todas as letras minúsculas;
# c) Quantas letras ao todo (sem considerar espaços);
# d) Quantas letras tem o primeiro nome.

nome = str(input('Qual seu nome completo, xará? '))
primeiro_nome = ''

print('Seu nome em maiúsculo é: ' + nome.upper())
print('Seu nome em minúsculo é: ' + nome.lower())
primeiro_nome = nome.split(' ')
print('Seu nome sem espaços é: ' + ''.join(nome.split(' ')))
print('Seu primeiro nome tem ' + str(len(primeiro_nome[0])) + ' espaços.')
