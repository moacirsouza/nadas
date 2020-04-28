print("""
084) Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma
lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
""")

listaDePessoasEPesos = []
maiorPeso = menorPeso = 0
pessoasMaisPesadas = ''
pessoasMaisLeves = ''

while True:
    nome = input('Informe o nome da pessoa: ').strip()
    peso = float(input(f'Informe o peso de {nome}: ').strip())

    ### Verificação do maior e menor pesos
    if len(listaDePessoasEPesos) == 0:
        maiorPeso = menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        elif peso < menorPeso:
            menorPeso = peso

    ### Esta atribuição garante que o nome e o peso serão inseridos,
    ### sempre, como uma lista aninhada na lista principal.
    ### É boa prática, no entanto, preferir o uso do método "append()".
    listaDePessoasEPesos += [[nome, peso]]

    ### Verificação tradicional de continuidade do programa
    while True:
        continuar = input('Deseja continuar? (s/n) ').strip().lower()

        if continuar == 's' or continuar == 'n':
            break
        print('Digite S/s ou N/n para prosseguir ou suspender, respectivamente.')
    
    if continuar == 'n':
        break

for item in listaDePessoasEPesos:
    if item[1] == maiorPeso:
        pessoasMaisPesadas += item[0] + ', '
    elif item[1] == menorPeso:
        pessoasMaisLeves += item[0] + ', '

print(f'{len(listaDePessoasEPesos)} pessoas foram cadastradas.')
print(f'O maior peso encontrado foi {maiorPeso}Kg. As pessoas deste grupo são: {pessoasMaisPesadas[:-2]}.')
print(f'O menor peso encontrado foi {menorPeso}Kg. As pessoas deste grupo são: {pessoasMaisLeves[:-2]}.')
