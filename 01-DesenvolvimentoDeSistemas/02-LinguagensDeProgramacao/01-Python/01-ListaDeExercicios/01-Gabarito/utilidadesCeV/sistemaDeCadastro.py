### TODO: Criar uma função para tratamento e apresentação de erros.
diretorio = 'sistemaDeCadastro'
arquivo = 'cadastroDePessoas.txt'
arquivoDeCadastro = arquivo # '/'.join([diretorio, arquivo])

def apresentaErro(erro, funcao):

    cabecalhoErro = 'ERRO: '
    cabecalhoAviso = 'AVISO: '

    if erro.__class__ == FileNotFoundError:

        if funcao == 'verPessoas':
            mensagem = f"""
{cabecalhoAviso}O arquivo "{arquivoDeCadastro}" não foi encontrado.
Tente cadastrar uma nova pessoa primeiro.
"""
        elif funcao == 'cadastrarPessoas':
            mensagem = f"""
{cabecalhoErro}O arquivo {arquivoDeCadastro} não foi encontrado.
Tentarei criá-lo a seguir.
"""
    elif erro.__class__ == PermissionError:
        mensagem = f"""
{cabecalhoErro}Sinto muito, não tenho permissões suficientes para criar
minha base de dados. Ela ficaria localizada em: {arquivoDeCadastro}
"""
    elif erro.__class__ == ValueError:
        mensagem = f"""
{cabecalhoAviso}Infome um valor inteiro para a idade.
"""

    print(mensagem)

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
                # print(f'Você escolheu {acaoDoMenu}')

                if acaoDoMenu == 1:
                    verPessoas()
                elif acaoDoMenu == 2:
                    cadastrarPessoas()
                break
            else:
                print('ERRO: Opção fora do menu.')
                continue


def verPessoas():
    try:
        referenciaAoArquivo = open(arquivoDeCadastro, 'r')
    except FileNotFoundError as erro:
        apresentaErro(erro, 'verPessoas')
        validaMenu()
    else:
        print(referenciaAoArquivo.read())
        referenciaAoArquivo.close()


def cadastrarPessoas():
    try:
        referenciaAoArquivo = open(arquivoDeCadastro,'r')
    except FileNotFoundError as erro:
        apresentaErro(erro, 'cadastrarPessoas')
        try:
            referenciaAoArquivo = open(arquivoDeCadastro, 'w+')
        except PermissionError as erro:
            apresentaErro(erro, 'cadastrarPessoas')
    else:
        referenciaAoArquivo = open(arquivoDeCadastro, 'a+')
        while True:
            nome = input('Nome: ').strip()

            while True:
                try:
                    idade = int(input('Idade: ').strip())
                    break
                except ValueError as erro:
                    apresentaErro(erro, 'cadastrarPessoas')
                    continue
            
            referenciaAoArquivo.write(f'{nome},{idade}\n')

            while True:
                continuar = input('Deseja cadastrar mais pessoas? (s/n)')
                continuar = continuar.lower().strip()

                if continuar == 'n' or continuar == 's':
                    break
                # apresentaErro(IOError as erro, 'cadastrarPessoas')
                print('ERRO: As escolhas limtam-se às letras "S", "s", "N" ou "n".')
            
            if continuar == 'n':
                break
            referenciaAoArquivo.close()


validaMenu()
