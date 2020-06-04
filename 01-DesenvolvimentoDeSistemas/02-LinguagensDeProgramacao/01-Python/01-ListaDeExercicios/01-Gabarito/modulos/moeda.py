def aumentar(preco, taxa):
    retorno = preco*(1+taxa/100)
    return retorno


def diminuir(preco, taxa):
    retorno = preco*(1-taxa/100)
    return retorno


def dobro(preco):
    retorno = preco*2
    return retorno


def metade(preco):
    retorno = preco/2
    return retorno

