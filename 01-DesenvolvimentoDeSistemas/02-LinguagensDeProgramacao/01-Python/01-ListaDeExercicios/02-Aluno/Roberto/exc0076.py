print("""
076) Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
preços, na sequência. No final, mostre uma listagem de preços organizando os dados em
forma tabular.
""")

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print('{:^40} '.format("LISTA DE PREÇOS"))
print('-' * 40)
for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print('{:.<30} '.format(listagem[posicao]), end='')
    else:
    #    print(f'R${listagem[posicao]:>7.2f}')
         print(' R${:>7.2f} '.format(listagem[posicao]))
print('-' * 40)










       
