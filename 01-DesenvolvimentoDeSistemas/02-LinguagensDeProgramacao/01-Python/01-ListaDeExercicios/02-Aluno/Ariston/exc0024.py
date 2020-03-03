print("""
024) Crie um programa em PYTHON que: leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
""")
cidade = str(input('Digite o nome da cidade: '))
resultado=('SANTO' == cidade.upper().strip().split()[0])
print('A cidade começa com "SANTO":  {}.\n'.format(resultado))