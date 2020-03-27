print("""
052) Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
""")

numero = int(input('Digite um número para verificar se ele é primo: ').strip())
contador = 0
nao = ' não'

for divisor in range(1, numero+1):
    if numero % divisor == 0:
        contador += 1

if contador == 2:
    nao = ''

mensagemFinal = 'O número {}{} é primo.'.format(numero, nao)

print(mensagemFinal)
