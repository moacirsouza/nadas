print("""
040) Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
""")

nota01 = float(input('Informe a primeira nota do(a) aluno(a): ').strip())
nota02 = float(input('Informe a segunda nota do(a) aluno(a): ').strip())

media = (nota01+nota02)/2

if media < 5:
    resultado = 'REPROVADO(A)'
elif media >= 5 and media <= 6.9:
    resultado = 'em RECUPERAÇÃO'
else:
    resultado = 'APROVADO(A)'

mensagemFinal = """
As notas do(a) aluno(a) foram {} e {}.
A média do(a) aluno(a) é {:.2f}.
Ele(a) está {}.
""".format(nota01,
           nota02,
           media,
           resultado)

print(mensagemFinal)
