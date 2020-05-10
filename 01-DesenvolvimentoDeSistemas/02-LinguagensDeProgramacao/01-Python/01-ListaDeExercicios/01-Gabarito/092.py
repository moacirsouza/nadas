print("""
092) Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente 
de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule
e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
""")

from datetime import date

anoAtual = date.today().year
titulo = ' Bem-vindo(a) ao Cadastro da Previdência Social '
formatador = len(titulo)
tempoDeContribuicao = 35
beneficiario = {}

print('-'*formatador)
print(f'{titulo:^{formatador}}')
print('-'*formatador)

print(f'{"Cadastre os dados do(a) beneficiário(a)":^{formatador}}')
nome = input('Nome: ').strip()
anoDeNascimento = int(input('Ano de Nascimento: ').strip())
idade = f'{anoAtual - anoDeNascimento} anos (Completos ou a completar)'
ctps = int(input('Número da CTPS (0 se não possuir): ').strip())

beneficiario = {'Nome':nome, 'Idade': idade, 'CTPS': ctps}

if ctps != 0:
    anoDeContratacao = int(input('Ano de contratação: ').strip())
    salario = float(input('Salário: R$ ').strip())

    idadeDeContratacao = anoDeContratacao - anoDeNascimento
    contratacao = f'{anoDeContratacao} ({idadeDeContratacao} anos)'
    aposentadoria = f'{idadeDeContratacao+tempoDeContribuicao} anos'

    beneficiario.update(dict(Contratação=contratacao,
                             Salário=salario,
                             Aposentadoria=aposentadoria))
else:
    beneficiario.update(dict(CTPS='Não possui'))

print('-'*formatador)
print(f'{"Resumo das informações cadastradas":^{formatador}}')
print('-'*formatador)
for chave, valor in beneficiario.items():
    reais = ''
    if chave == 'Salário':
        reais = 'R$ '

    print(f' - {chave}: {reais}{valor}')
print('-'*formatador)
