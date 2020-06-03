print("""
101) Crie um programa que tenha uma função chamada voto() que vai receber como
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando
se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
""")

# Regras da obrigatoriedade do voto no Brasil:
# 1. Negado se você tiver menos de 16 anos
# 2. Opcional se você tiver entre 16 e até 18 ou mais de 65 anos
# 3. Obrigatório se você tiver entre 18 e até 65 anos
from datetime import date

def voto(anoDeNascimento):

    anoAtual = date.today().year
    idade = anoAtual - anoDeNascimento
    mensagemBase = f'Você tem {idade} anos: Voto'

    if idade < 16:
        situacao = 'negado.'
    elif 16 <= idade < 18 or idade > 65:
        situacao = 'opcional.'
    else:
        situacao = 'obrigatório.'
    
    retorno = ' '.join([mensagemBase, situacao])
    
    return retorno


nascimento = int(input('Informe seu ano de nascimento: ').strip())
resultado = voto(nascimento)
print(resultado)
