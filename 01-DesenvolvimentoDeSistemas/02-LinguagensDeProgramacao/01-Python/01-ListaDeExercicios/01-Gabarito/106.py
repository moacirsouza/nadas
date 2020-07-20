print("""
106) Faça um mini-sistema que utilize o interactiveHelp do Python. O usuário
vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a
palavra 'FIM', o programa se encerrará.
""")


### TODO: Criar a função de colorização dos textos
def chamaInteractiveHelp():
    while True:
        pesquisa = input('Informe o nome do método ou Biblioteca \
(Digite "fim" para sair)> ').strip()

        if pesquisa.lower() == 'fim':
            print('Obrigado por usar o Interactive Help!')
            break
        else:
            help(pesquisa)

chamaInteractiveHelp()
