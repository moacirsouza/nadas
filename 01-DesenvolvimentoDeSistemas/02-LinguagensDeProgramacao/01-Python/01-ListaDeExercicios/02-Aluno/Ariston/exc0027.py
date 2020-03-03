print("""
027) Crie um programa em PYTHON que: leia o nome completo de uma pessoa, mostrando em seguida 
o primeiro e o último nome separadamente.
""")
nome = str(input('Digite seu nome completo: '))
primeiroNome=nome.split()[0]
ultimoNome=nome.split()[-1]
print('\nNo nome {}\nO primeiro nome é: {}\ne o último nome é {}\n'.format(nome,primeiroNome,ultimoNome))
