print("""
103) Faça um programa que tenha uma função chamada ficha(), que receba
dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
dado não tenha sido informado corretamente.
""")

def ficha(jogador='<desconhecido>', numeroDeGols='0'):

    ### O parâmetro "jogador" foi usado na chamada da função,
    ### mas o usuário não informou nenhum texto. Se este teste
    ### não for realizado, a impressão final mostrará um bloco
    ### vazio ao invés do termo "<desconhecido>"
    if jogador == '':
        jogador = '<desconhecido>'

    if numeroDeGols.isnumeric():
        numeroDeGols = int(numeroDeGols)
    else:
        erroGolsNaoInteiro = '''
ERRO: É preciso informar um número inteiro para a quantidade de gols.
Neste caso o programa assume o valor zero.
'''
        print(erroGolsNaoInteiro)
        numeroDeGols = 0

    retorno = f'O jogador {jogador} fez {numeroDeGols} gols.'

    print(retorno)


nome = input('Nome do Jogador: ').strip()
gols = input('Número de Gols: ').strip()

### Chamada com os dois parâmetros
# ficha(nome, gols)

### Chamada com apenas o primeiro parâmetro
# ficha(jogador=nome)

### Chamada com apenas o segundo parâmetro
ficha(numeroDeGols=gols)

### Chamada sem nenhum parâmetro
# ficha()
