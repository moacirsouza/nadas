def leiaDinheiro(mensagem='Informe um valor monetário: '):

    while True:
        entrada = input(mensagem).strip().replace(',', '.')
        
        if entrada.isalpha():
            print(f'ERRO: O valor informado não pode ser \
formatado como moeda. Tente novamente.')
        else:
            retorno = float(entrada)
            break

    return retorno
