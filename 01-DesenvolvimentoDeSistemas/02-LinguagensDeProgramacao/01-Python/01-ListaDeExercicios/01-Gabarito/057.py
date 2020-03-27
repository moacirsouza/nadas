print("""
057) Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto
""")

sexo = input('Informe o sexo da pessoa (m/f): ').strip().lower()

while sexo != 'm' and sexo != 'f':
    sexo = input("""
Opção inválida.
Use "m" ou "f" para registrar o sexo da pessoa (m/f): """).strip().lower()

sexoRegistrado = 'Masculino'

if sexo == 'f':
    sexoRegistrado = 'Feminino'

print("""
Opção escolhida: {}
Sexo {} registrado. """.format(sexo, sexoRegistrado))
