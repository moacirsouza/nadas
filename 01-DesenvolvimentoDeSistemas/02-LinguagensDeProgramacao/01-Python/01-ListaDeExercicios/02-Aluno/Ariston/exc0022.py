print("""
022) Crie um programa em PYTHON que: leia o nome completo de uma pessoa e mostre: 
a) O nome com todas as letras maiúsculas; 
b) O nome com todas as letras minúsculas; 
c) Quantas letras ao todo (sem considerar espaços); 
d) Quantas letras tem o primeiro nome.
""")
nomeCompleto = str(input('Digite seu nomme completo: '))
Maius = nomeCompleto.upper()
minus = nomeCompleto.lower()
letrasSemEspacos = len(nomeCompleto.replace(' ',''))
quantaLetrasTemPrimeiroNome = len(nomeCompleto.split()[0])
print('\n Maiúscula {} '.format(Maius))
print('\n Minúscula {} '.format(minus))
print('\n Quantidade de letras ao todo {} '.format(letrasSemEspacos))
print('\n Quantidade de letras primeiro nome {} \n'.format(quantaLetrasTemPrimeiroNome))