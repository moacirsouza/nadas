print('[-- O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. --]\n')
from random import shuffle
nome01 = input('Digite o nome do primeiro aluno: ')
nome02 = input('Digite o nome do segundo aluno: ')
nome03 = input('Digite o nome do terceiro aluno: ')
nome04 = input('Digite o nome do quarto aluno: ')
ordemdeapresentacao = [nome01, nome02, nome03, nome04]
shuffle(ordemdeapresentacao)
print('A ordem de apresentação será: ')
print(ordemdeapresentacao)

