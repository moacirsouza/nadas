print('[-- Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido. --]\n')
from random import choice 
nome01 = input('Digite o nome do primeiro aluno: ')
nome02 = input('Digite o nome do segundo aluno: ')
nome03 = input('Digite o nome do terceiro aluno: ')
nome04 = input('Digite o nome do quarto aluno: ')
alunos = [nome01,nome02,nome03,nome04]
alunoquemiraapagar = choice(alunos)
print('O aluno escolhido foi: {} ' .format(alunoquemiraapagar))



