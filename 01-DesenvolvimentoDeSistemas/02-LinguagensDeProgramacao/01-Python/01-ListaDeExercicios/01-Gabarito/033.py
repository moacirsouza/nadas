print("""
033) Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
""")

### Entrada do programa: Cada uma das três variáveis recebe um número inteiro.
numero01 = int(input('Digite o primeiro número: '))
numero02 = int(input('Digite o segundo número: '))
numero03 = int(input('Digite o terceiro número: '))

### Define a primeira entrada como o maior número. Essa atribuição é
### completamente aleatória, qualquer um poderia ser escolhido como o 
### maior, pois essa posição é temporária e os testes a seguir é que
### vão definir qual das entradas possui o maior valor.
maior = numero01

### Se o segundo número é maior que o maior valor atual, a variável
### "maior" recebe este novo valor.
if numero02 > maior:
    maior = numero02

### Da mesma forma que no primeiro teste, o terceiro número é comparado
### com o valor atualmente retido na variável "maior" e, se ele for maior,
### a variável "maior" termina com este valor.
if numero03 > maior:
    maior = numero03

### Não importa qual das três variáveis recebe o maior valor, os testes
### vão sempre garantir que esse número seja, eventualmente, atribuído
### à variável "maior"
print('\nO maior número entre {}, {} e {} é: {}'.format(numero01, numero02, numero03, maior))
