print("""
079) Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicioando. No final, serão exibidos todos os valores únicos digitados, em
ordem crescente.
""")

números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado ! Não adicionar ...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn' :
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os valores {números} ')
