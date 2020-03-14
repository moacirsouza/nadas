print("""
036) Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele
vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou
então o empréstimo será negado.
""")
valordacasa = float(input('Qual o valor da casa? '))
salariodocomprador = float(input('Qual o salário do comprador? '))
tempoparapagar = float(input('Em quantos anos irá pagar?'))
valordaprestacaomensal = valordacasa/(tempoparapagar*12)
if valordaprestacaomensal > 0.3*salariodocomprador:
    print('Empréstimo Negado')
else:
    print('Seu empréstimo foi APROVADO e sua mensalidade será de {}'.format(valordaprestacaomensal))
