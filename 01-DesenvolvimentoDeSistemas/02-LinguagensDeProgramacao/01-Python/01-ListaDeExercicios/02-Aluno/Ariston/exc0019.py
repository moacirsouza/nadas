print("""
019) Crie um programa em PYTHON que sorteia um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
""")
from random import choice
aluno01 = str(input('Digite o nome do Aluno 01: '))
aluno02 = str(input('Digite o nome do Aluno 02: '))
aluno03 = str(input('Digite o nome do Aluno 03: '))
aluno04 = str(input('Digite o nome do Aluno 04: '))
classe = [aluno01,aluno02,aluno03,aluno04]
escolhido = choice(classe)
print('O aluno escolhido foi {}'.format(escolhido))