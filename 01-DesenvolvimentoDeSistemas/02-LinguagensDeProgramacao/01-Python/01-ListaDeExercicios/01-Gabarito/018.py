print("""
018) Faça um programa que leia um ângulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo.
""")

### Importação dos métodos que serão utilizados pelo programa.
### O método "radians" converte o valor de um ângulo em graus
### para radianos. O uso dele é, de certa forma, obrigatório,
### uma vez que as funções trigonométricas do Pyton trabalham
### com valores em radianos, não em graus.
from math import sin, cos, tan, radians

### Entrada do programa: Recebe o ângulo como um número real
### ("float"), que vai ser considerado em graus.
angulo = float(input('Informe o valor de um ângulo (Em graus): '))

### Transformação do valor do ângulo em graus para radianos.
### O motivo de fazer essa conversão com uma nova variável ao
### invés de realizar um "cast" diretamente na variável "angulo"
### da entrada é que, na apresentação do resultado este valor
### também vai ser mostrado e seria obrigatório usar uma nova
### conversão de radianos para graus, com o método "degrees".
### Esta decisão, portanto, evita carregar um módulo extra.
anguloEmRadianos = radians(angulo)

### Chamada direta dos métodos para cálculo dos valores solicitados.
### Não é preciso preceder a chamada com o nome do módulo, e.g.
### "math.sin", por conta do tipo de importação escolido. Se todo o
### módulo "math" fosse importado com o "import math", esse formato
### de chamada seria obrigatório.
seno = sin(anguloEmRadianos)
cosseno = cos(anguloEmRadianos)
tangente = tan(anguloEmRadianos)

print("""
Para o ângulo {:.2f}° temos os seguintes valores:
Seno: {:.2f}
Cosseno: {:.2f}
Tangente: {:.2f}
""".format(angulo, seno, cosseno, tangente))
