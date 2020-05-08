print("""
090) Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo a estrutura na tela.
""")

nome = input('Informe o nome do(a) aluno(a): ').strip()
media = float(input(f'Informe e a média de {nome}: ').strip())
erro = 0

if 7 <= media <= 10:
    situacao = 'Aprovado'
elif 5 <= media <= 6.9:
    situacao = 'Em recuperação'
elif 0 <= media < 5:
    situacao = 'Reprovado'
else:
    erro = 1
    situacao = 'Falha na entrada de dados. Procure a Adminstração da Escola.'

if erro == 1:
    print(situacao)
else:
    aluno = {'Nome': nome, 'Média': media, 'Situação': situacao }
    print('-'*30)
    for chave, valor in aluno.items():
        print(f'{chave}: {valor}')
    print('-'*30)
