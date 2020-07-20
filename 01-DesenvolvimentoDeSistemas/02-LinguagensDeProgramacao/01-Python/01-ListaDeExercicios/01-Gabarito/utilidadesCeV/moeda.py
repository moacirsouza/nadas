def aumentar(preco=0, taxa=0, valorMonetario=False):
    retorno = preco*(1+taxa/100)

    if valorMonetario:
        retorno = moeda(retorno)

    return retorno


def diminuir(preco=0, taxa=0, valorMonetario=False):
    retorno = preco*(1-taxa/100)

    if valorMonetario:
        retorno = moeda(retorno)

    return retorno


def dobro(preco=0, valorMonetario=False):
    retorno = preco*2

    if valorMonetario:
        retorno = moeda(retorno)

    return retorno


def metade(preco=0, valorMonetario=False):
    retorno = preco/2

    if valorMonetario:
        retorno = moeda(retorno)

    return retorno


def moeda(preco=0, formatadorDeMoeda='R'):
    retorno = f'{formatadorDeMoeda}$ {preco:.2f}'
    
    return retorno


def resumo(preco=0, taxaDeAumento=0, taxaDeReducao=0):
    precoFormatado = moeda(preco)
    precoDobrado = dobro(preco, True)
    precoPelaMetade = metade(preco, True)
    precoIncrementado = aumentar(preco, taxaDeAumento, True)
    precoReduzido = diminuir(preco, taxaDeReducao, True)

### TODO: Melhorar a formatação da saída, levando em conta
### coisas como o possível tamanho variável da tabela, de
### acordo com o comprimento do preço informado etc.
    retorno = f"""
    -------------------------------
            RESUMO DO VALOR
    -------------------------------
    Preço analisado: {precoFormatado}
    Dobro do preço: {precoDobrado}
    Metade do preço: {precoPelaMetade}
    {taxaDeAumento}% de aumento: {precoIncrementado}
    {taxaDeReducao}% de redução: {precoReduzido}
    -------------------------------
    """

    print(retorno)
