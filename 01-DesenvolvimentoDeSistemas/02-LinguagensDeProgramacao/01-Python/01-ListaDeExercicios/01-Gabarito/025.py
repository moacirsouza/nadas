print('[-- Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. --]\n')

### Entrada do programa: Recebe o nome de uma pessoa como "string"
nome = str(input('Digite seu nome completo: '))

### A variável "temSilva" realiza uma série de procedimentos na 
### "string", a fim de minimizar os potenciais problemas que o
### usuário pode causar na hora de verificar a existência do 
### padrão na entrada. Os métodos "strip()" é usado para remover
### espaços em branco do começo e do final do texto, enquanto o
### "lower()" força todos os caracteres alfabéticos a ficarem em
### minúsculo, facilitando a verificação do "find()".
temSilva = nome.strip().lower().find('silva')

print('O nome informado tem "Silva"? Se sim, em que posição? Se não, a resposta será "-1".\n{}'.format(temSilva))
