print("""
097) Faça um programa que tenha uma função chamada escreva(), que receba um
texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
""")

def escreva(mensagem):
    mensagemFormatada = f' {mensagem} '
    comprimentoDaMensagem = len(mensagemFormatada)

    print('~'*comprimentoDaMensagem)
    print(mensagemFormatada)
    print('~'*comprimentoDaMensagem)


mensagemDoUsuario = input('Digite sua mensagem: ').strip()
escreva(mensagemDoUsuario)
