print("""
072) Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. Seu programa deverá ler um
número pelo teclaro (entre 0 e 20) e mostrá-lo por extenso.
""")

deZeroAVintePorExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                          'seis', 'sete', 'oito', 'nove', 'dez', 'onze ',
                          'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
                          'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    entradaDoUsuario = int(input('Digite um número entre 0 e 20: '))
    if 20 >= entradaDoUsuario >= 0:
        break
    print('Número inválido. Tente novamente.')

print(f'Você digitou o número {deZeroAVintePorExtenso[entradaDoUsuario]}')
