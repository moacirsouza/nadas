print("""
\033[1;37;44m 020) \033[m Crie um programa em PYTHON que: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
""")
from random import shuffle
aluno01 = str(input('Digite o nome do Aluno 01: '))
aluno02 = str(input('Digite o nome do Aluno 02: '))
aluno03 = str(input('Digite o nome do Aluno 03: '))
aluno04 = str(input('Digite o nome do Aluno 04: '))
classe = [aluno01,aluno02,aluno03,aluno04]
shuffle(classe)
print('\nA orde escolhida para apresentar o trabalho foi {}'.format(classe))