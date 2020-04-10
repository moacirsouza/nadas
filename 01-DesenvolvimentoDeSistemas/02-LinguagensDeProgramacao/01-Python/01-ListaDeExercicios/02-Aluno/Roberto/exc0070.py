print("""
070) Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato.
""")

totalgasto = 0
totalacimade1000 = 0
menorpreco = 0
contador = 0
produtomaisbarato = ''

while True:
    nomedoproduto = str(input('Qual o nome do produto? ')).strip().upper()
    precodoproduto = float(input('Qual o preço do produto R$? '))
    contador += 1
    totalgasto += precodoproduto
    if precodoproduto > 1000:
        totalacimade1000 += 1     
    if contador == 1:
        menorpreco = precodoproduto
        produtomaisbarato = nomedoproduto
    else:
        if precodoproduto < menorpreco:
            menorpreco = precodoproduto
            produtomaisbarato = nomedoproduto


    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break

print('O total gasto na compra foi: R${:.2f}'.format(totalgasto))
print('A quantidade de produtos que custam mais de R$1000 é: {}'.format(totalacimade1000))
print('O produto mais barato custa R${:.2f}'.format(menorpreco))
print('O nome do produto mais barato foi: {}'.format(produtomaisbarato))

