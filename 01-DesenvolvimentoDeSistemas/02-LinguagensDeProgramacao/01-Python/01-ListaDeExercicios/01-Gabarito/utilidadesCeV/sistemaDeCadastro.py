diretorio = 'sistemaDeCadastro'
arquivo = 'cadastroDePessoas.txt'
arquivoDeCadastro = arquivo # '/'.join([diretorio, arquivo])

def apresentaErro(excecao, funcao):

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
                if acaoDoMenu == 1:
                    verPessoas()
                elif acaoDoMenu == 2:
                    cadastrarPessoas()
                elif acaoDoMenu == 3:
                    sairDoSistema()
                else:
                    break
            else:
                print('ERRO: Opção fora do menu.')
                continue


def verPessoas():

    try:
        referenciaAoArquivo = open(arquivoDeCadastro, 'r')
    except Exception as excecao:
        apresentaErro(excecao, 'verPessoas')
    else:
        print(referenciaAoArquivo.read())
        referenciaAoArquivo.close()
    finally:
        validaMenu()



def cadastrarPessoas():

    try:
        referenciaAoArquivo = open(arquivoDeCadastro,'r')
    except Exception as excecao:
        apresentaErro(excecao, 'cadastrarPessoas')
    else:
        try:
            referenciaAoArquivo = open(arquivoDeCadastro, 'a+')
        except Exception as excecao:
            apresentaErro(excecao, 'cadastrarPessoas')
        else:
            separador(repeticoes=40)
            print('Iniciando o cadastro: ')
            separador(repeticoes=40)

            nome = input('Nome: ').strip()

            while True:
                try:
                    idade = int(input('Idade: ').strip())
                except ValueError as excecao:
                    apresentaErro(excecao, 'cadastrarPessoas')
                    continue
                else:
                    break
            
            referenciaAoArquivo.write(f'{nome},{idade}\n')
            referenciaAoArquivo.close()
    finally:
        validaMenu()


def sairDoSistema():
    print('Saindo do sistema...')
    exit(0)


validaMenu()
