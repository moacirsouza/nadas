print("""
027) Faça um programa que leia o nome completo de uma pessoa, mostrando em
seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza.
primeiro=Ana
último: Souza.
""")

### Entrada do programa: Recebe o nome da pessoa como "string"
nome = str(input('Digite o seu nome completo: '))

### A variável "nomeProcessado" usa o método "strip()" para 
### remover os espaços extras do início e do final da "string"
nomeProcessado = nome.strip()

### O método "split()" divide uma "string" em uma lista de
### de "strings", separadas por espaço. Por exemplo: Se a
### "string" 'um texto longo' sofrer um "split()", o resultado
### será a lista ['um', 'texto',' longo']. Cada um dos itens poderá,
### então, ser referenciado por um índice numérico que começa
### em 0. Em qualquer lista há um índice especial, "-1", que sempre
### se refere ao último item do conjunto.
primeiroNome = nomeProcessado.split()[0]
ultimoNome = nomeProcessado.split()[-1]

### Uma maneira alternativa para encontrar o último item de uma lista
### é calcular o tamanho dela com o método "len()" e informar este
### valor, subtraído de 1, como índice. A subtração é necessária porque
### o "len()" retorna o tamanho da lista como se ela começasse com o
### índice 1. Por exemplo, o tamanho da lista ['um', 'texto', 'longo']
### é 3, mas o índice do último item é 2. Sem a subtração, recebe-se
### o erro "IndexError: list index out of range".
# ultimoNome = nomeProcessado.split()[len(nomeProcessado.split())-1]

print("""
O seu primeiro nome é: {}.
O seu último nome é: {}.
""".format(primeiroNome,ultimoNome))
