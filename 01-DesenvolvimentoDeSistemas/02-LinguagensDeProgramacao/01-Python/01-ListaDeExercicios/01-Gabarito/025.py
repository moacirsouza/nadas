print("""
025) Crie um programa que leia o nome de uma pessoa e diga se ela tem
"SILVA" no nome.
""")

### Entrada do programa: Recebe o nome de uma pessoa como "string"
nome = str(input('Digite seu nome completo: '))

### A variável "nomeProcessado" realiza uma série de procedimentos
### na "string", a fim de minimizar os potenciais problemas que o
### usuário pode causar na hora de verificar a existência do 
### padrão na entrada. O método "strip()" é usado para remover
### espaços em branco do começo e do final do texto, enquanto o
### "lower()" força todos os caracteres a ficarem em minúsculo,
### facilitando, por exemplo, a verificação do "find()".
nomeProcessado = nome.lower().strip()

### Depois de processar a entrada na variável "nomeProcessado", a
### utilização de métodos como o "find()" fica amplamente simplificada.
### Agora, independente de como a entrada for entregue ao programa,
### i.e., usando letras maiúsculas ou minúsculas, com o sem espaços no
### começo ou no final do nome, o "find()" não terá problemas em
### encontrar o padrão.
ondeEstaSilva = nomeProcessado.find('silva')

### Similarmente à variável "ondeEstaSilva", a "temSilva" deve
### realizar procedimentos que facilitam as verificações do operador
### "in" do Python. Como esses procedimentos foram realizados na 
### variável "nomeProcessado", é suficiente fazer "temSilva" receber
### o valor de "nomeProcessado".
temSilva = nomeProcessado

print('\nMétodo 1: Usando o método "find()": Se houver "Silva", \
mostre em que posição ele aparece. Se não houver, imprima "-1": \
{}.'.format(ondeEstaSilva))

print('\nMétodo 2: Usando o operador "in": Existe "Silva" no nome? -> \
{}.'.format('silva' in temSilva))
