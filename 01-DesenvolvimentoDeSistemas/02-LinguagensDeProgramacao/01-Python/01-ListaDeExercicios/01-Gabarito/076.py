("""
076) Crie um programa que tenha uma tupla única com nomes de produtos e
seus respectivos preços, na sequência. No final, mostre uma listagem de
preços organizando os dados em forma tabular.
""")

listaDeProdutos = ('Ovo (Bandeja com 30)', 6.2, 'Maçã (Kg)', 8.5,
                   'Detergente de Pratos', 0.99, 'Sabonete', 0.85,
                   'Água Sanitária', 1.1, 'Sabão em Pó', 6.5,
                   'Biscoito Bono', 1.85, 'Batata Ruffles', 1.8,
                   'Fubá', 1.15, 'Café', 2.5,
                   'Pão', 23.9, 'Manteiga', 2.5)

# TODO: Verificar a relação entre o offset e os comprimentos do
# preço, nome do produto e do símbolo de moeda
titulo = 'Lista de Preços'
offset = 5
contador = 0

### É preciso saber, de antemão, o espaço ocupado pelo preço após a
### formatação, que nesse caso, é a exigência de duas casas decimais
### após a vírgula. É por isso que o método "len" foi utilizado após
### a extração do valor máximo, mas apenas depois de utilizarmos uma
### f-string para forçar a formatação que será utilizada em seguida.
comprimentoDoMaiorPreco = len(f'{max(listaDeProdutos[1::2]):.2f}')
comprimentoDoMaiorProduto = max(map(len, listaDeProdutos[0::2]))

comprimentoDaTabela = comprimentoDoMaiorProduto \
                      + comprimentoDoMaiorPreco \
                      + offset

print('-'*comprimentoDaTabela)
print(f'{titulo:^{comprimentoDaTabela}}')
print('-'*comprimentoDaTabela)

for contador in range(0, len(listaDeProdutos), 2):
    produto = listaDeProdutos[contador]
    preco = listaDeProdutos[contador+1]

### TODO: Colocar o 'R$ ' como variável da "string" de apresentação
    quantidadeDePontos = comprimentoDaTabela - (comprimentoDoMaiorPreco+3)
    
    print(f'{produto:.<{quantidadeDePontos}}R$ \
{preco:>{comprimentoDoMaiorPreco}.2f}')

print('-'*comprimentoDaTabela)
