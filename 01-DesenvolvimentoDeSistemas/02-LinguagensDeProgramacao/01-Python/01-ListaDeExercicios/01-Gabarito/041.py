print("""
041) A Confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre a sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
""")

from datetime import date

anoDeNascimento = int(input('Informe o ano de nascimento do(a) atleta: ').strip())
anoAtual = date.today().year
idade = anoAtual - anoDeNascimento

if   idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JÚNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

mensagemFinal = 'O(A) atleta tem {} ano(s) e é da categoria {}'.format(idade, categoria)

print(mensagemFinal)
