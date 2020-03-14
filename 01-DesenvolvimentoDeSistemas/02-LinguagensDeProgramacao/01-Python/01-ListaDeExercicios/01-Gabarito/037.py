print("""
037) Escreva um programa que leia um número inteiro qualquer e peça ao usuário para
escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
""")

### Entrada do programa: Recebe um número como inteiro (int)
### É sempre bom lembrar que o usuário pode escrever o que
### bem entender, portanto, usar métodos como o strip() é 
### praticamente mandatório para qualquer programa que se
### preocupa, minimamente, em processar adequadamente as
### informações que recebe. Até agora isso não acontecia
### muito em nossos exercícios, mas é boa prática preocupar-se
### com esse tipo de questão. Sendo assim, passarei a utilizar
### o strip() com mais frequência de agora em diante
numero = int(input('Informe um número inteiro: ').strip())

### Os conversores de bases numéricas do Python são métodos
### built-in da linguagem. Isso significa que não é preciso
### carregar (i.e., importar) nenhum módulo para utilizá-los.
### No entanto, é importante ressaltar que cada base numérica
### recebe um prefixo, a saber: os binários são precedidos de
### "0b", os octais de "0o" e os hexadecimais de "0x". Por uma
### questão meramente estética, decidi remover esses prefixos
### e apresentar apenas os valores convertidos. Como os métodos
### de conversão retornam os valores como "string", bastou usar
### a técnica de fatiamento de listas para remover os dois
### primeiros caracteres
numeroEmBinario = bin(numero)[2:]
numeroEmOctal = oct(numero)[2:]
numeroEmHexadecimal = hex(numero)[2:]

escolhaDaBaseDeConversao = input("""
O número {} pode ser convertido para as seguintes bases numéricas:
[1] Binária
[2] Octal
[3] Hexadecimal
[4] Todas
Escolha sua opção: """.format(numero)).strip()

resultado = '\nO número {}, em '.format(numero)

### Decidi deixar o valor da "escolhaDaBaseDeConversao" como
### "string" ao invés de tranformá-lo em inteiro. Essa escolha
### não tem grande relevância para este caso e o inverso poderia
### ter sido feito sem grandes prejuízos para a lógica ou
### eficiência do código.
###
### Também é importante verificar que utilizei o operador de 
### concatenação de "strings" em dois momentos, dentro de cada
### estrutura de desvio, uma com o formato "+=", que adiciona um
### novo valor à variável "resultado", originalmente definida
### fora do escopo dos if's e em seguida o "+", que adiciona ao
### final do texto o valor do inteiro convertido na base selecionada
if escolhaDaBaseDeConversao == '1':
    resultado += 'Binário, é ' + numeroEmBinario
elif escolhaDaBaseDeConversao == '2':
    resultado += 'Octal, é ' + numeroEmOctal
elif escolhaDaBaseDeConversao == '3':
    resultado += 'Hexadecimal, é ' + numeroEmHexadecimal
elif escolhaDaBaseDeConversao == '4':
    resultado += """Binário, é {},
em Octal, é {} e em Hexadecimal, é {}.
""".format(numeroEmBinario, numeroEmOctal, numeroEmHexadecimal)
else:
    resultado = '\nVocê escolheu uma opção inexistente. Tente novamente.'

### Por causa da manipulação do texto, realizada na definição das
### variáveis e dentro das estruturas de controle, o "print" final
### acabou ficando bem simples. Independente do que for escolhido
### pelo usuário, o programa, agnosticamente, apenas imprime o
### conteúdo da variável "resultado"
print(resultado)
