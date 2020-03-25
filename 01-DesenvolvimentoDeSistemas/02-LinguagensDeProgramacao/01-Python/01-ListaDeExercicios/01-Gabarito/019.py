print("""
019) Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido. 
""")
from random import choice
nome01 = input('Informe o nome do primeiro(a) aluno(a): ')
nome02 = input('Informe o nome do segundo(a) aluno(a): ')
nome03 = input('Informe o nome do terceiro(a) aluno(a): ')
nome04 = input('Informe o nome do quarto(a) aluno(a): ')
alunos = [nome01, nome02, nome03, nome04]
quemVaiApagar = choice(alunos)
print('O(a) aluno(a) escolhido(a) foi: {}'.format(quemVaiApagar))
