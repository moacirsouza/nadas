print("""
069) Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
""")

pessoascommaisde18 = 0
homenscadastrados = 0
mulherescommenosde20 = 0

while True:
    idade = int(input('Qual a sua idade? '))
    sexo = ' '    
    while sexo not in 'MF': # Permanece solicitando se o usuário não digar M ou F.
        sexo = str(input('Qual o seu sexo [M/F]? ')).strip().upper()[0]
    if idade > 18:
        pessoascommaisde18 += 1
    if sexo == 'M':
        homenscadastrados += 1
    if sexo == 'F' and idade < 20:
        mulherescommenosde20 += 1
    continuar = ' '
    while continuar not in 'SN': # Permanece solicitando se o usuário não digitar S ou N.
        continuar = str(input('Quer continuar (S/N)?')).strip().upper()[0]
    if continuar == 'N':
        break

print('Total de Pessoas com mais de 18 anos são: {} pessoas'.format(pessoascommaisde18))
print('O total de homens cadastrados são: {} '.format(homenscadastrados))
print('O total de mulheres com menos de 20 anos são: {}'.format(mulherescommenosde20))

