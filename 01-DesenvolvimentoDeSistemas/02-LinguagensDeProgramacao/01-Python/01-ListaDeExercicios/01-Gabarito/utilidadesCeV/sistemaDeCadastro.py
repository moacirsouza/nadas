diretorio = 'sistemaDeCadastro'
arquivo = 'cadastroDePessoas.txt'
arquivoDeCadastro = arquivo # '/'.join([diretorio, arquivo])

def iniciar(titulo='CADASTRO DE PESSOAS'):

    comprimentoDoSeparador = len(titulo)*2
    opcoes = imprimirMenu(titulo, comprimentoDoSeparador)

    while True:
        try:
            acaoDoMenu = int(input('Escolha uma opção: ').strip())
        except Exception as excecao:
            apresentarErro(excecao, 'iniciar')
            imprimirMenu(titulo, comprimentoDoSeparador)
            continue
        else:
            if str(acaoDoMenu) in opcoes.keys():
                if acaoDoMenu == 1:
                    verPessoas(titulo, comprimentoDoSeparador)
                elif acaoDoMenu == 2:
                    cadastrarPessoas(titulo, comprimentoDoSeparador)
                elif acaoDoMenu == 3:
                    sairDoSistema(titulo, comprimentoDoSeparador)
            else:
                print('ERRO: Opção fora do menu.')
                continue


def separador(caractere='-', repeticoes=30):
    print(caractere*repeticoes)


def imprimirMenu(titulo, comprimentoDoSeparador):

    opcoes = {
        '1':'Ver pessoas cadastradas',
        '2':'Cadastrar nova Pessoa',
        '3':'Sair do Sistema'
    }

    separador(repeticoes=comprimentoDoSeparador)
    print(f'{titulo:^{comprimentoDoSeparador}}')
    separador(repeticoes=comprimentoDoSeparador)
    
    for linha in opcoes.items():
        print(f'{linha[0]} - {linha[1]}')
    
    separador(repeticoes=comprimentoDoSeparador)

    return opcoes


def verPessoas(titulo, comprimentoDoSeparador):

    try:
        referenciaAoArquivo = open(arquivoDeCadastro, 'r')
    except Exception as excecao:
        apresentarErro(excecao, 'verPessoas')
    else:
        print('\n')
        separador(repeticoes=comprimentoDoSeparador)
        print(f'{"Listagem das pessoas":^{comprimentoDoSeparador}}')
        separador(repeticoes=comprimentoDoSeparador)
        print(referenciaAoArquivo.read())

        referenciaAoArquivo.close()
    finally:
        iniciar(titulo)


def cadastrarPessoas(titulo, comprimentoDoSeparador):

    try:
        referenciaAoArquivo = open(arquivoDeCadastro, 'r')
    except Exception as excecao:
        apresentarErro(excecao, 'cadastrarPessoas')
    
    try:
        referenciaAoArquivo = open(arquivoDeCadastro, 'a+')
    except Exception as excecao:
        apresentarErro(excecao, 'cadastrarPessoas')
    else:
        print('\n')
        separador(repeticoes=comprimentoDoSeparador)
        print('Informe os dados cadastrais: ')
        separador(repeticoes=comprimentoDoSeparador)

        nome = ' '.join(input('Nome: ').split())

        while True:
            try:
                idade = int(input('Idade: ').strip())
            except Exception as excecao:
                apresentarErro(excecao, 'cadastrarPessoas')
                continue
            else:
                if idade*(-1) > 0:
                    print('\nERRO: A idade não pode ser um número negativo.\n')
                    continue
                break
        
        referenciaAoArquivo.write(f'{nome},{idade}\n')
        referenciaAoArquivo.close()
    finally:
        iniciar(titulo)


def sairDoSistema(titulo, comprimentoDoSeparador):

    print('Saindo do sistema...')
    exit(0)

def apresentarErro(excecao, funcao):

    cabecalhoErro = 'ERRO: '
    cabecalhoAviso = 'AVISO: '

    if excecao.__class__ == FileNotFoundError:
        if funcao == 'verPessoas':
            mensagem = f"""
{cabecalhoErro}O arquivo "{arquivoDeCadastro}" não foi encontrado.
Tente cadastrar uma nova pessoa primeiro.
"""
        elif funcao == 'cadastrarPessoas':
            mensagem = f"""
{cabecalhoAviso}O arquivo {arquivoDeCadastro} não foi encontrado.
Tentarei criá-lo no caminho {arquivoDeCadastro}.
"""
    elif excecao.__class__ == PermissionError:
        if funcao == 'verPessoas':
            mensagem = f"""
{cabecalhoErro}O arquivo existe, mas está sem permissão de leitura.
Por favor, altere as permissões, ou remova o arquivo
existente para que eu possa recriar minha base de dados.
Caminho do arquivo atual: {arquivoDeCadastro}"""
        elif funcao == 'cadastrarPessoas':
            mensagem = f"""
{cabecalhoErro}Sinto muito, não tenho permissões suficientes para criar
minha base de dados. Certifique-se de ter permissões suficientes
no seguinte diretório: {arquivoDeCadastro}
"""
    elif excecao.__class__ == ValueError:
        if funcao == 'iniciar':
            mensagem = f"""
{cabecalhoErro}Opção inválida. Escolha um item do Menu."""
        elif funcao == 'cadastrarPessoas':
            mensagem = f"""
{cabecalhoAviso}Infome um valor inteiro para a idade.
"""

    print(mensagem)
