print("""
Faça um programa que leia uma frase pelo teclado e mostre: a) Quantas vezes aparece a letra "A"; b) Em que posição ela aparece a primeira vez; c) Em que posição ela aparece a última vez. 
""")

### Entrada do programa: Recebe uma frase como "string"
frase = str(input('Digite uma frase: '))

### Como no exercício anterior, remover os espaços do 
### início e do final da frase e fazer com que todos os
### caracteres sejam minúsculos, facilita o processamento
### dos métodos e operadores do Python. Assim, criamos uma
### variável intermediária, chamada "fraseProcessada", que
### atenda estes requisitos.
fraseProcessada = frase.lower().strip()

### Conta a quantidade de letras "a" na frase
quantidadeDeAs = fraseProcessada.count('a')

### É importante lembrar que o método "find()" começa a
### contar a partir do índice 0, uma vez que qualquer
### "string" é tratada como um "Array" ou "Lista" dentro
### da linguagem e os primeiros conteúdos destes objetos
### são sempre 0. A adição de 1 ao final "corrige" essa
### questão, adicionando conforto ao usuário, que, em
### geral, vai começar a contar do número 1.
primeiraOcorrenciaDeA = fraseProcessada.find('a')+1

### O método "rfind()" faz o mesmo que o "find()", mas
### começa a contagem do final da "string" para o começo.
### Da mesma forma que no "find()", o primeiro índice é 0,
### por isso é importante adicionar o 1 ao resultado da busca.
ultimaOcorrenciaDeA = fraseProcessada.rfind('a')+1

### O uso das aspas duplas triplas facilita a impressão do
### texto com a manutenção da formatação original, sem a 
### necessidade de usar caracteres de escape, como o "\n"
### para criação de nova linha etc.
print("""
A letra 'a' aparece {} vezes na frase.
A primeira ocorrência da letra 'a' na frase é na posição {}.
A última ocorrência da letra 'a' na frase é na posição {}.
""".format(quantidadeDeAs,primeiraOcorrenciaDeA,ultimaOcorrenciaDeA))
