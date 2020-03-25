print("""
049) refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
""")

numero = int(input('Digite um número inteiro: '))
titulo = 'Tabuada do ' + str(numero)

print('+{:-^16}+'.format(titulo))
for fatorMultiplicador in range(1, 11):
    print('| {:>2} x {:>2} = {:>4} |'.format(numero,
                                             fatorMultiplicador,
                                             numero*fatorMultiplicador))
print('+'+('-'*16)+'+')
