# (01-Gabarito/057.py)) Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = ''
erro = -1

while sexo not in ['M','F','m','f']:
    if erro > -1:
        print('Deixe de ser jumento. Você não sabe que é pra digitar só M ou F?')
    sexo = str(input('Digite o Sexo: "M" ou "F" \t: '))
    erro = erro + 1


