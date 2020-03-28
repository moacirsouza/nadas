print("""
057) Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto
""")
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados incorretos, favor Digite seu sexo corretamente [M/F] ')).strip().upper()[0]
print('O Sexo informado é {} '.format(sexo))


  
  
