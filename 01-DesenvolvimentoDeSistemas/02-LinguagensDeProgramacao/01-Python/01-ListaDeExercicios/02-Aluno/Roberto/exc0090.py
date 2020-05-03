print("""
090) Faça um programa que leia nome e média de um aluno, guardando
também a situação de um dicionário. No final, mostre
o conteúdo da estrutura na tela.
""")
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média do aluno {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')






