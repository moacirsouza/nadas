# Mostrar a média
aluno = input('Digite o nome do aluno: ')
nota1 = int(input('Digite a primeira nota:'))
nota2 = int(input('Digite a segunda nota :'))
media = (nota1+nota2)/2
print('O aluno {} tirou nota {:.0f} de média' .format(aluno, media))
