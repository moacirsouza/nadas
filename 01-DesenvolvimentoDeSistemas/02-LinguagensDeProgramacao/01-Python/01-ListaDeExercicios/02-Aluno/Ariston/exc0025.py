print("""
025) Crie um programa em PYTHON que: leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
""")
nome = str(input('Digite o nome da pessoa: '))
nomeMudado = nome.upper().strip()
print('Em {} existe a palavra "SILVA" {}: '.format(nome.upper(),'SILVA' in nomeMudado))