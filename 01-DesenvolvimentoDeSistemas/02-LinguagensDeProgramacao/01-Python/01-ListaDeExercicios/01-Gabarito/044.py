print("""
044) Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros
""")

print("""
[{:-^80}]
""".format(' Lojinha da Esquina '))

precoDoProduto = float(input('Informe o preço do produto: R$ ').strip())

formaDePagamento01 = 'À vista, no dinheiro ou cheque: 10% de desconto.'
formaDePagamento02 = 'À vista, no cartão: 5% de desconto.'
formaDePagamento03 = 'Em até 2 vezes, no cartão: Preço regular.'
formaDePagamento04 = 'Em 3 vezes ou mais, no cartão: 20% de juros.'

menuFormasDePagamento = """
Opções de pagamento:
[1] {}
[2] {}
[3] {}
[4] {}

Escolha uma forma de pagamento: """.format(formaDePagamento01,
                                           formaDePagamento02,
                                           formaDePagamento03,
                                           formaDePagamento04)

formaDePagamento = int(input(menuFormasDePagamento).strip())

mensagemFinal = """
[{:-^80}]

Preço do produto: R$ {:.2f}
Forma de pagamento: """.format(' Resumo financeiro ', precoDoProduto)

opcaoInvalida = False

if formaDePagamento == 1:

    precoDoProduto -= precoDoProduto*0.1
    mensagemFinal += """{}
""".format(formaDePagamento01)

elif formaDePagamento == 2:

    precoDoProduto -= precoDoProduto*0.05
    mensagemFinal += """{}
""".format(formaDePagamento02)

elif formaDePagamento == 3:

    mensagemFinal += """{}
Sua compra será dividida em 2 parcelas de R$ {:.2f}, sem juros.
""".format(formaDePagamento03, (precoDoProduto/2))

elif formaDePagamento == 4:

    precoDoProduto += precoDoProduto*0.2
    parcelas = int(input('Divir a compra em quantas parcelas? ').strip())

    if parcelas < 3:
        opcaoInvalida = True
        mensagemFinal = """
Nesta opção só é possível dividir o pagamento em 3 vezes ou mais.
Reinicie o processo de compra.
"""
    else:
        mensagemFinal += """{}
Sua compra será dividida em {} parcelas de R$ {:.2f},
com acréscimo de 20% de juros.
""".format(formaDePagamento04, parcelas, (precoDoProduto/parcelas))

else:
    opcaoInvalida = True
    mensagemFinal = """
Opção inexistente no menu.
Por favor, tente novamente.
"""

if not opcaoInvalida:
    mensagemFinal += """
Preço final: R$ {:.2f}
""".format(precoDoProduto)

print(mensagemFinal)
