print("""
049) refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
""")

print('-' * 18)

n = int(input('Digite um número: '))
print('Tabuada do {}'.format(n))
for valor in range(1, 11):
    print('{} x {} = {}' .format(n, valor, n*valor ))

print('-' * 18)


