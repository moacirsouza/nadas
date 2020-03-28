print("""
053) Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
""")

frase = str(input('Digite a frase: '))
fraseSemEspacos = frase.replace(' ', '').lower()
fraseInvertida = fraseSemEspacos[::-1]
nao = ' não'

if fraseSemEspacos == fraseInvertida:
    nao = ''

mensagem = '{} é um palíndromo'.format(nao)

print('A frase: "{}" {}'.format(frase, mensagem))
