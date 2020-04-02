# (01-Gabarito/040.py)) Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#       - Média abaixo de 5.0: REPROVADO
#       - Média entre 5.0 e 6.9: RECUPERAÇÃO
#       - Média 7.0 ou superior: APROVADO

print('*'*100)
print('* Fixação de Unidades sem Defasagem da Escola Universo (FUDEU)' + ' '*37+'*')
print('*'*100)
print('*' + ' '*98 + '*')
nota1 = float(input('* Digite a nota do primeiro semestre\t: '))
nota2 = float(input('* Digite a nota do segundo semestre\t: '))
print('*' + ' '*98 + '*')
media = round((nota1+nota2)/2,2)
print('* Nota 1 \t\t Nota 2 \t\t Média')
print('* {}\t\t\t {}\t\t\t {}'.format(nota1, nota2, media))
if media < 5:
    print('* Até ano que vem, papai. Você está REPROVADOOOOOOOOOO!!!')
if media > 5 and media < 7:
    print('* Você foi pra a recuperação. COIDADO NA NOTA!!!!')
else:
    print('Você é o cara!!! PASSOUUUUUUU!!!!')



