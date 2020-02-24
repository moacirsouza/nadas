print('[-- Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. --]\n')

### Entrada do programa: Recebe o nome de uma pessoa como "string"
nome = str(input('Digite seu nome completo: '))

### A variável "ondeEstaSilva" realiza uma série de procedimentos na 
### "string", a fim de minimizar os potenciais problemas que o
### usuário pode causar na hora de verificar a existência do 
### padrão na entrada. O método "strip()" é usado para remover
### espaços em branco do começo e do final do texto, enquanto o
### "lower()" força todos os caracteres a ficarem em minúsculo,
### facilitando a verificação do "find()".
ondeEstaSilva = nome.strip().lower().find('silva')

### Similarmente à variável "ondeEstaSilva", a "temSilva" realiza
### procedimentos que facilitam as verificações do operador "in"
### do Python.
temSilva = nome.strip().lower()

print('Método 1: Usando o método "find()": Se houver "Silva", mostre em que posição ele aparece. Se não houver, imprima "-1": {}'.format(ondeEstaSilva))
print('Método 2: Usando o operador "in": Existe "Silva" no nome? -> {}'.format('silva' in temSilva))
