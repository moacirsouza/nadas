# (01-Gabarito/052.py)) Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um numero natural\t: '))

mensagem = 'O número {} não é primo!!!'
eh_primo = True

for i in range(2,numero):
    if numero % i == 0 and i != numero:
        eh_primo = False
        break

if eh_primo:
    mensagem = 'O número {} é primo!!!'

print(mensagem.format(numero))
