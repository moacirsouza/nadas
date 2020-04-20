("""
076) Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
preços, na sequência. No final, mostre uma listagem de preços organizando os dados em
forma tabular.
""")

listaDeProdutos = ('Pão', 0.99, 'Manteiga', 2.5, 'Ovo (Bandeja com 30)', 6.2,
                   'Maçã (Kg)', 8.5, 'Detergente de Pratos', 1.1, 'Sabonete', 0.85,
                   'Água Sanitária', 2321123.9, 'Sabão em Pó', 6.5, 'Biscoito Bono', 1.85,
                   'Batata Ruffles', 1.8, 'Fubá', 1.15, 'Café', 2.5)

titulo = 'Lista de Preços'
# comprimentoDaTabela = 40
contador = 0

comprimentoDoMaiorPreco = len(str(max(listaDeProdutos[1::2])))
comprimentoDoMaiorProduto = len(max(listaDeProdutos[0::2]))
comprimentoDaTabela = comprimentoDoMaiorProduto + comprimentoDoMaiorPreco + 20
print(comprimentoDaTabela)


print('-'*comprimentoDaTabela)
print(f'{titulo:^{comprimentoDaTabela}}')
print('-'*comprimentoDaTabela)

for contador in range(0, len(listaDeProdutos), 2):
    produto = listaDeProdutos[contador]
    preco = listaDeProdutos[contador+1]
    
    # TODO: Melhorar o cálculo do tamanho da tabela para adequar-se a qualquer
    # valor informado na tupla.
    quantidadeDePontos=comprimentoDaTabela-(comprimentoDoMaiorPreco+5)
    
    print(f'{produto:.<{quantidadeDePontos}}R$ {preco:>{comprimentoDoMaiorPreco+2}.2f}')

print('-'*comprimentoDaTabela)
