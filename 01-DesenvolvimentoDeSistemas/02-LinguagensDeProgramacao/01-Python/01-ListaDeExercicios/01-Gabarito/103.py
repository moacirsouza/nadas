print("""
103) Faça um programa que tenha uma função chamada ficha(), que receba
dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
dado não tenha sido informado corretamente.
""")

def ficha(jogador='<desconhecido>', numeroDeGols=0):
    retorno = f'O jogador {jogador} fez {numeroDeGols} gols.'

    print(retorno)


nome = input('Nome do Jogador: ').strip()
gols = input('Número de Gols: ').strip()

if gols.isnumeric():
    gols = int(gols)
else:
    erroGolsNaoInteiro = 'ERRO: É preciso informar um número inteiro \
para a quantidade de gols. Neste caso o programa assume o valor zero.\n'
    print(erroGolsNaoInteiro)
    gols = 0

if nome == '':
    ficha(numeroDeGols=gols)
else:
    ficha(nome, gols)
