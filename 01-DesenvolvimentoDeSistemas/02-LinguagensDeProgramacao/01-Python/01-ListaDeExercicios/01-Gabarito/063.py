print("""
063) Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n
primeiros elementos de uma Sequência de Fibonacci.
Ex:
0 → 1 → 1 → 2 → 3 → 5 → 8 
""")

### A Sequênia de Fibonacci é definida como: 
### F(0)=0, F(1)=1 e, para n>1, F(n)=F(n-1)+F(n-2)
###
### Desta forma, os 10 primeiros termos são:
### 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
###
### Referências:
### https://en.wikipedia.org/wiki/Fibonacci_number
### https://oeis.org/A000045

contador = 2
quantidadeDeTermos = int(input('Quantos termos da Sequência de Fibonacci você deseja mostrar: ').strip())
fibonacci = [0, 1]

while contador < quantidadeDeTermos:
    fibonacci += [fibonacci[contador-1]+fibonacci[contador-2]]
    contador += 1
print('A sequência de Fibonacci com {} termos é:\n{}'.format(contador, fibonacci))
