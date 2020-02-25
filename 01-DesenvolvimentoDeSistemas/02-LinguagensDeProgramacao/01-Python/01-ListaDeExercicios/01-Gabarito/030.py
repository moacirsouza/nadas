print("""
030) Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
""")

### Entrada do programa: Recebe um número inteiro
numero = int(input('Informe um número inteiro: '))

### A mensagem é pré-configurada com o retorno do caso
### para o qual o número é ímpar. Se ele for par, o if
### altera a mensagem. Se não, essa atribuição permanece
### e será exibida pelo "print" final.
mensagem = '\nO número {} é ímpar.\n'.format(numero)

### Aqui foi utilizado o operador de módulo, ou resto da
### divisão. Qualquer número par, ao ser dividido por 2
### retorna resto 0, enquanto que um número ímpar retorna
### valores diferentes disto.
if (numero%2 == 0):
    mensagem = '\nO número {} é par.\n'.format(numero)

### Imprime a mensagem, que será alterada de acordo com a
### entrada do usuário.
print(mensagem)
