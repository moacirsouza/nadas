print("""
070) Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto da compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.
""")

totalGastoNaCompra = 0
quantidadeDeProdutosMaisCarosQue1000 = 0
precoDoProdutoMaisBarato = 0
contador = 0

while True:
    nomeDoProduto = input('Informe o nome do produto: ')
    precoDoProduto = float(input('Informe o preço do produto: R$ '))
    
    while True:
        condicaoDeParada = input('Deseja continuar? (s/n) ').strip().lower()

        if condicaoDeParada == 's' or condicaoDeParada == 'n':
            break
        print('Use "S/s" ou "N/n", respectivamente, para \
contiunar ou sair do programa.')

    ### Avaliação do produto mais barato
    if contador == 0:
        nomeDoProdutoMaisBarato = nomeDoProduto
        precoDoProdutoMaisBarato = precoDoProduto
    else:
        if precoDoProdutoMaisBarato > precoDoProduto:
            precoDoProdutoMaisBarato = precoDoProduto
            nomeDoProdutoMaisBarato = nomeDoProduto

    ### Totalizador de Gastos
    totalGastoNaCompra += precoDoProduto

    if precoDoProduto > 1000:
        quantidadeDeProdutosMaisCarosQue1000 += 1
        nomeDoProdutoMaisCaroQue1000 = nomeDoProduto

    if condicaoDeParada == 'n':
        break

    contador += 1

print("""
O produto mais barato foi: {} (R$ {:2.f}).
O total gasto foi de R$ {:.2f}.
Há {} produto(s) mais caro(s) \
que R$ 1000.00 ({}).""".format(nomeDoProdutoMaisBarato,
                               precoDoProdutoMaisBarato,
                               totalGastoNaCompra,
                               quantidadeDeProdutosMaisCarosQue1000,
                               nomeDoProdutoMaisCaroQue1000)
)
