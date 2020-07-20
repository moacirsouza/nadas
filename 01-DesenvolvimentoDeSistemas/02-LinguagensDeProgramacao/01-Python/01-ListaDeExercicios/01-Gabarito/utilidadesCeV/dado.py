def leiaDinheiro(mensagem='Informe um valor monetário: '):

    erro = f'ERRO: O valor informado não pode ser \
formatado como moeda. Tente novamente.'

    while True:
        entrada = input(mensagem).replace(',', '.').strip()
        
        if entrada.isalpha() or entrada is '':
            print(erro)
        else:
            retorno = float(entrada)
            break

    return retorno
