print("""
Crie um programa que leia o nome completo de uma pessoa e mostre: a) O nome com todas as letras maiúsculas; b) O nome com todas as letras minúsculas; c) Quantas letras ao todo (sem considerar espaços); d) Quantas letras tem o primeiro nome 
""")

### Entrada de dados
nomeCompleto=input('Por favor, informe seu nome completo: ')

### Definição de variáveis e extração das informações do texto
tudoMaiusculo=nomeCompleto.upper()
tudoMinusculo=nomeCompleto.lower()
totalDeLetras=len(nomeCompleto.replace(' ',''))
comprimentoDoPrimeiroNome=len(nomeCompleto.split()[0])

### Apresentação dos resultados
print('a) O nome informado, com todas as letras maiúsculas é: {}'.format(tudoMaiusculo))
print('b) O nome informado, com todas as letras minúsculas é: {}'.format(tudoMinusculo))
print('c) O total de letras do nome informado, sem contar os espaços é: {}'.format(totalDeLetras))
print('d) A quantidade de letras no primeiro nome é: {}'.format(comprimentoDoPrimeiroNome))
