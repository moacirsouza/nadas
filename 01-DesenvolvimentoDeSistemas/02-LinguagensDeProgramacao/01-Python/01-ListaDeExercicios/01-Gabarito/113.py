print("""
113) Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
agora a possibilidade da digitação de um número de tipo inválido. Aproveite
e crie também uma função leiaFloat() com a mesma funcionalidade.
""")


def leiaInt(mensagem='Número inteiro: '):
    while True:
        try:
            numero = int(input(mensagem).strip())
        except ValueError:
            print('ERRO: Entrada incorreta. Por favor, informe um \
número inteiro válido')
            continue
        else:
            return numero


def leiaFloat(mensagem='Número real: '):
    while True:
        try:
            numero = float(input(mensagem).strip())
        except ValueError:
            print('ERRO: Entrada incorreta. Por favor, informe um \
numéro real válido')
            continue
        else:
            return numero

supostoNumeroInteiro = leiaInt('Informe um número inteiro: ')
supostoNumeroReal = leiaFloat('Informe um número real: ')
    
print(f'Número inteiro: {supostoNumeroInteiro}')
print(f'Número real: {supostoNumeroReal}')
