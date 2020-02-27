print("""
028) Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário vendeu ou perdeu.
""")

### Importa o método "randint()", da bilbioteca (módulo) "random"
### do Python. Este é o método que será responsável por gerar um
### número entre 0 e 5, conforme solicitado no enunciado.
from random import randint

### Entrada do programa: Recebe do usuário um número entre 0 e 5.
numero = int(input('Digite um número entre 0 e 5: '))

### Escolhe, "aleatoriamente", um número entre 0 e 5, a fim de 
### formar a "senha" que o usuário precisa adivinhar. O método
### "randint()" recebe dois inteiros como parâmetros e retorna
### um número entre eles.
senha = randint(0,5)

### Uso tradicional do if-else: A verificação da igualdade entre
### os valores das variáveis "numero" e "senha", levam à execução
### do primeiro bloco, também conhecido como "bloco da verdade".
### Quando o teste falha, ou seja, se "numero" e "senha" não tiverem
### conteúdos, o segundo bloco, conhecido como "bloco do else", será
### executado. 
if numero == senha:
    print('Olha só, acertou!\nVocê e o computador escolheram {}!'.format(numero))
else:
    print('Mais sorte da próxima vez!\nVocê escolheu {}, mas o computador pensou em {}'.format(numero,senha))

### Uma alternativa para o uso da estrutura tradicional if-else,
### neste caso, é a seguinte: Define-se uma variável "mensagem",
### que é inicializada com uma das respostas possíveis (Neste caso,
### a resposta negativa). Com apenas um if, realiza-se a verificação
### do caso oposto e dentro dele define-se o outro conteúdo possível
### da mensagem. Por fim, um "print" único imprime a mensagem, que
### sofrerá alteração dependendo da entrada do usuário.
# mensagem = '\nMais sorte da próxima vez!\nVocê escolheu {}, mas o computador pensou em {}'.format(numero,senha)
# if numero == senha:
#     mensagem = '\nOlha só, acertou!\nVocê e o computador escolheram {}!'.format(numero)
# print(mensagem)