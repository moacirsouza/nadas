print("""
036) Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele
vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou
então o empréstimo será negado.
""")

### Entrada do programa: Recebe o valor da casa e o salário do comprador como número real
### ("float") e o tempo de pagamento como inteiro ("int").
valorDoImovel = float(input('Informe o valor do imóvel: R$ ').strip())
salarioDoComprador = float(input('Informe o salário do(a) comprador(a): R$ ').strip())
tempoDePagamento = int(input('Informe o tempo de pagamento (Em anos): ').strip())

percentualDoSalario = 0.3
limiteSuperior = salarioDoComprador*percentualDoSalario
parcelaMensal = valorDoImovel/(tempoDePagamento*12)
mensagemDeAprovacao = '\nParabéns! Seu financiamento foi aprovado!'
situacaoDoFinanciamento = 'APROVADO'

if parcelaMensal > limiteSuperior:
    mensagemDeAprovacao = '\nSinto muito. Seu financiamento foi negado.'
    situacaoDoFinanciamento = 'NEGADO'

mensagemDeAprovacao += '\nVeja os detalhes financeiros a seguir.'

print(mensagemDeAprovacao.format(parcelaMensal))
print("""
Resumo financeiro:
- Valor do Imóvel: R$ {:.2f}
- Salário do Comprador: R$ {:.2f}
- Tempo de pagamento: {} anos
- Valor da Parcela: R$ {:.2f}
- Limite Superior (30% do Salário): R$ {:.2f}
- Situação do Financiamento: {}
""".format(
    valorDoImovel,
    salarioDoComprador,
    tempoDePagamento,
    parcelaMensal,
    limiteSuperior,
    situacaoDoFinanciamento
    )
)
