print("""
078) Faça um programa que leia 5 valores numéricos de guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.
""")
maior = 0
menor = 0
listanum = []
for n in range(0, 5):
    listanum.append(int(input(f'Entre com o valor para a posição {n}: ')))
    if n == 0:
        maior = menor = listanum[n]
    else:
        if listanum[n] > maior:
            maior = listanum[n]
        if listanum[n] < menor:
            menor = listanum[n]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor é {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()        
print(f'O menor valor é {menor} nas posições ', end='' )
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()