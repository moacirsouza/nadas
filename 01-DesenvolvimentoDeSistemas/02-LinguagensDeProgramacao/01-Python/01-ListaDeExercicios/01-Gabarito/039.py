print("""
039) Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
com a sua idade, se ele ainda vai se alistar ao serviço, se é a hora de se alistar ou
se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que
falta ou que passou do prazo.
""")

### Importação da classe "date", do módulo "datetime"
from datetime import date

### Entrada do programa: A variável "anoDeNascimento" recebe o valor
### de entrada como inteiro (int). Novamente, é importante notar o uso
### do método "strip()", no momento do recimento da entrada do usuário,
### a fim de fazer uma primeira validação simples, i.e., a remoção de
### possíveis espaços em branco antes e/ou depois do conteúdo que será
### processado
anoDeNascimento = int(input('Informe o ano em que você nasceu: ').strip())

### A propriedade "year", do construtor "today()", retorna o valor
### do ano atual
anoAtual = date.today().year

idadeDoJovem = anoAtual - anoDeNascimento
idadeMinimaParaAlistamento = 18
mensagemFinal = """
Estamos em {} e você tem, ou terá até o fim do ano, {} ano(s).
""".format(anoAtual, idadeDoJovem)

### O conjunto de testes é bem simples e apenas verifica se o jovem
### tem mais, menos ou exatamente 18 anos de idade. De acordo com
### este critério a variável "mensagemFinal" recebe novas informações para
### cada caso.
if idadeDoJovem > idadeMinimaParaAlistamento:
    prazo = idadeDoJovem - idadeMinimaParaAlistamento
    mensagemFinal += """
O prazo para seu alistamento já expirou há {} ano(s).
""".format(prazo)
elif idadeDoJovem < idadeMinimaParaAlistamento:
    prazo = idadeMinimaParaAlistamento - idadeDoJovem
    mensagemFinal += """
Ainda falta(m) {} ano(s) para o seu alistamento.
""".format(prazo)
else:
    mensagemFinal += """
Este é o ano do seu alistamento! Para maiores
informações, visite a Junta Militar mais próxima!
"""

### Por fim, apenas a variável "mensagemFinal" é passada como parâmetro
### para a saída do programa. Todos os dados, cálculos e variações
### possíveis, derivadas da regra de negócios, já foram tratadas
### anteriormente, por isso não é mais preciso alterar nada pontualmente
print(mensagemFinal)
