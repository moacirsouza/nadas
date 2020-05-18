print("""
097) Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parãmetro e mostre uma mensagem com tamanho adaptável.
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~~~~~~~
Olá, Mundo !
~~~~~~~~~~~~~~~
""")
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
escreva('Roberto Mendonça')
escreva('Curso em Video')
escreva('Oi')