#(01-Gabarito/020.py)) O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

alunos = ['','','','']
aluno = ''

for i in range(0,4):
    aluno = str(input("Fala, professor! Qual o nome do amiguinho número "+str(i)+"? "))
    alunos[i] = aluno

alunos.sort()

print('')
print('Atenção!!! A ordem de apresentação do trabalho é a seguinte:')
for aluno in alunos:
    print('*\t' + aluno)

