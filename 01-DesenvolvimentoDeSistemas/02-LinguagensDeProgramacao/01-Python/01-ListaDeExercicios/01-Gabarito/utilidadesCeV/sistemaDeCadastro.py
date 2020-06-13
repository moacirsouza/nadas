def separador(caractere='-', repeticoes=30):
    print(caractere*repeticoes)


def imprimeMenu(titulo='MENU PRINCIPAL'):

    comprimentoDoTitulo = len(titulo)*3
    opcoes = {
        '1':'Ver pessoas cadastradas',
        '2':'Cadastrar nova Pessoa',
        '3':'Sair do Sistema'
    }

    separador(repeticoes=comprimentoDoTitulo)

    print(f'{titulo:^{comprimentoDoTitulo}}')

    separador(repeticoes=comprimentoDoTitulo)
    
    for linha in opcoes.items():
        print(f'{linha[0]} - {linha[1]}')
    
    separador(repeticoes=comprimentoDoTitulo)

    return opcoes


def validaMenu():

    opcoes = imprimeMenu()

    while True:
        try:
            acaoDoMenu = int(input('Escolha uma opção: ').strip())
        except ValueError:
            print('ERRO: Opção inválida. Escolha um item do Menu.')
            imprimeMenu()
            continue
        else:
            if str(acaoDoMenu) in opcoes.keys():
                print(f'Você escolheu {acaoDoMenu}')
                break
            else:
                print('ERRO: Opção fora do menu.')
                continue


validaMenu()