# (01-Gabarito/053.py)) Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

palavra = str(input('Digite uma palavra\t: '))

palavra = ''.join(palavra.split(' '))
contrario = palavra[::-1]

palindromo = palavra == contrario

texto = 'A palavra ' + palavra + ' não é um palíndromo!!!'

print('')
if palindromo:
    texto = 'A palavra ' + palavra + ' é um palíndromo!!!'

print(texto)