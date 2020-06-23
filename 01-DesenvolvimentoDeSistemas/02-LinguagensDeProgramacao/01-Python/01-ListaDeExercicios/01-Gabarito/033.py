print("""
033) Faça um programa que leia três números e mostre qual é o maior
e qual é o menor.
""")

### Entrada do programa: Cada uma das três variáveis recebe um número
### inteiro.
numero01 = int(input('Digite o primeiro número: '))
numero02 = int(input('Digite o segundo número: '))
numero03 = int(input('Digite o terceiro número: '))

### Define a primeira entrada como o maior número. Essa atribuição é
### completamente aleatória, qualquer um poderia ser escolhido como o 
### maior, pois essa posição é temporária e os testes a seguir é que
### vão definir qual das entradas possui o maior valor.
maior = numero01
menor = numero01

### Testes para verificação do maior número. Se os quatro testes
### falharem, o maior número será o primeiro, conforme a primeira
### atribuição da variável "maior" supôs.
if numero02 > numero01 and numero02 > numero03:
    maior = numero02

if numero03 > numero01 and numero03 > numero02:
    maior = numero03

### Testes para verificação do menor número. Se os quatro testes
### falharem, o menor número será o primeiro, conforme a primeira
### atribuição da variável "menor" supôs.
if numero02 < numero01 and numero02 < numero03:
    menor = numero02

if numero03 < numero01 and numero03 < numero02:
    menor = numero03
    
### Não importa qual das três variáveis recebe o maior valor, os testes
### vão sempre garantir que esse número seja, eventualmente, atribuído
### à variável "maior". O mesmo raciocínio vale para o menor valor.
print("""
Os três números informados foram: {}, {} e {}.
O maior deles é {}.
O menor deles é {}.
""".format(numero01, numero02, numero03, maior, menor))

### E se dois dos três números forem iguais?
