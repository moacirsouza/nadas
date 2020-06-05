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


def moeda(preco, formatadorDeMoeda='R'):
    retorno = f'{formatadorDeMoeda}$ {preco:.2f}'
    
    return retorno
