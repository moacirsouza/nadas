print("""
038) Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
""")

### Entrada do programa: As variáveis "numero01" e "numero02" recebem
### os dois valores de entrada como inteiros (int).
numero01 = int(input('Digite o valor do primeiro número: ').strip())
numero02 = int(input('Digite o valor do segundo número: ').strip())

### A mensagem padrão é definida para quando os valores são iguais.
### Essa mensagem vai ser atribuída logo após o recebimento das
### entradas e só será alterada, caso um dos testes das estrutudas
### de decisão seja alcançado ao longo da execução.
mensagem = 'Não existe valor maior, os dois são iguais.'

### Testa se o primeiro número é maior. Se sim, altera a mensagem e
### o programa segue em frente.
if numero01 > numero02:
    mensagem = 'O primeiro valor é maior.'

### Testa se o segundo número é maior. Se sim, altera a mensagem e
### o programa segue em frente
if numero02 > numero01:
    mensagem = 'O segundo valor é maior.'

### Imprime a mensagem de saída, alterada de acordo com a relação
### entre os dois números de entrada.
### 
### É importante notar que a mensagem sempre vai conter a informação
### correta, uma vez que os dois "if" possuem condições excludentes,
### que não se sobrepõem. Caso nenhum dos testes dos condicionais seja
### alcançado, isso significa que os números são, fatalmente, iguais.
print(mensagem)
