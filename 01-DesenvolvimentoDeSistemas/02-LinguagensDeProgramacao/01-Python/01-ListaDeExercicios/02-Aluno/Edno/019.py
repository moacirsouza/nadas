#(01-Gabarito/019.py)) Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

alunos = ['','','','']
aluno = ''
for i in range(0,4):
    aluno = str(input("Fala, professor! Qual o nome do amiguinho número "+str(i)+"? "))
    alunos[i] = aluno

sel = random.randint(0,3)

print('')
print('Atenção! Quem vai apagar o quadro agora é ' + alunos[sel])