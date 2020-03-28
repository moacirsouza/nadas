print("""
054) Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
""")

from datetime import date

anoAtual = date.today().year
maioresDeIdade = 0
menoresDeIdade = 0

for usuario in range(1, 8):
    anoDeNascimento = int(input('Informe o ano de nascimento do usuário {:02}: '.format(usuario)).strip())
    if (anoAtual - anoDeNascimento) >= 21:
        maioresDeIdade += 1
    else:
        menoresDeIdade += 1

print("""
{} pessoas são maiores de idade.
{} pessoas são menores de idade.
""".format(maioresDeIdade, menoresDeIdade))
