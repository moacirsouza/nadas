print("""
002) Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
""")

### Entrada do programa: Recebe o nome como texto ("string").
### É importante lembrar o método "input" sempre recebe os
### dados como "string", mesmo que o cast não seja feito
### explicitamente.
nome=input('Digite o seu nome: ')

### Método 1: Utilizando a sintaxe da vírgula, do Python 2.
print('\n[Sintaxe do Python2] Usando a vírgula:')
print('É um prazer te conhecer,',nome+'!\n')

### Método 2: Utilizando a sintaxe do símbolo de porcentagem,
### do Python 2.
print('[Sintaxe do Python2] Usando o símbolo de percentual:')
print('É um prazer te conhecer, %s!\n' % nome)

### Método 3: Utilizando a sintaxe do método format, do
### Python 3. Esta deve ser a sintaxe preferida.
print('[Sintaxe do Python3] Usando o .format :')
print('É um prazer te conhecer, {}!\n'.format(nome))
