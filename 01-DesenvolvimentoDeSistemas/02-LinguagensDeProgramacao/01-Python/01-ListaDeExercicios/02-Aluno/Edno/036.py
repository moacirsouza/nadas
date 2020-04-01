# (01-Gabarito/036.py)) Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('*'*100)
print('* Sistema Unico de Administração - Mudança, Avaliação e Empréstimo (SUA MAE)' + ' '*23 + '*')
print('*'*100)
print('')
valor_casa = float(input('* Diga o valor da casa\t\t\t\t\t: '))
salario = float(input('* Diga o salário do comprador\t\t\t\t: '))
anos = int(input('* Diga em quantos anos o pagamento será realizado\t: '))

mensalidade = round(valor_casa/(anos*12),6)
limite = salario * 0.30

print('')
print('')
if mensalidade > limite:
    print('A simulação negou o risco, pois o valor da mensalidade, que é de R$ ' + str(round(mensalidade,2)) + ' é maior do que R$ ' + str(round(limite,2)) + ', que é o máximo que você pode usar.')
else:
    print('A simulação aprovou o risco. O valor da parcela é de R$ ' +str(round(mensalidade,2)) + '.')


