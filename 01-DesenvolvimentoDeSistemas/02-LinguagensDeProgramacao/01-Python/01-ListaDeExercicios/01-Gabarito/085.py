print("""
085) Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre
os valores pares e ímpares em ordem crescente.
""")

paresEImpares = [[], []]

for contador in range(7):
    numero = int(input(f'Informe o {contador+1}º número inteiro: ').strip())

    if numero%2 == 0:
        # paresEImpares[0] += [numero]
        paresEImpares[0].append(numero)
    else:
        # paresEImpares[1] += [numero]
        paresEImpares[1].append(numero)

paresEImpares[0].sort()
paresEImpares[1].sort()
print(f'A lista de pares é: {paresEImpares[0]}.')
print(f'A de ímpares é: {paresEImpares[1]}')
