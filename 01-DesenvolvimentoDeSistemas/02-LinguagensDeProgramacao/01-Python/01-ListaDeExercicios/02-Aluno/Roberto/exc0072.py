print("""
072) Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, 
de zero até vinte.
Seu programa deverá ler um número pelo teclado(entre 0 e 20) e 
mostrá-lo por extenso.
""")
contagem = ('zero', 'um', 'dois', 'três', 'quatro',
'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 
'dezoito', 'dezenove', 'vinte')
while True:
    número = int(input('Digite um  número entre 0 e 20: '))
    if 0 <= número <=20:
        break
    print('Tente novamente. ', end='')
print('Você digitou o número {}'.format(contagem[número]))