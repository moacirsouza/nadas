print('[-- Crie um programa que leia o nome completo de uma pessoa e mostre: a) O nome com todas as letras maiúsculas; b) O nome com todas as letras minúsculas; c) Quantas letras ao todo (sem considerar espaços); d) Quantas letras tem o primeiro nome --]\n')
nome = input('Digite o nome completo: ')
print('O  nome com todas as letras maiúsculas é: {}' .format(nome.upper()))
print('O nome com todas as letras minúsculas é: {}' .format(nome.lower()))
print('Quantas letras ao todo? {}' .format(len(nome.replace(' ', ''))))
separa = len(nome.split()[0])
print('Quantas letras tem o primeiro nome? {}' .format(separa))



# Por que não deu certo assim??/
# print('Quantas letras tem o primeiro nome? {}' .format(len(nome.split()[0]))

