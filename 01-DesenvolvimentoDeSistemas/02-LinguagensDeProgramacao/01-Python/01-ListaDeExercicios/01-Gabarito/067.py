print("""
067) Faça um programa que mostre a tabuada de vários números, um de cada vez, para
cada valor digitado pelo usuário. O programa será interrompido quando o número
solicitado for negativo.
""")

while True:
    numero = int(input("""
Quer ver a tabuada de qual número?
Digite um número negativo para sair: """).strip())

    if numero < 0:
        break

    ### Extração ipsis litteris do Exercício 049,
    ### que já imprime a tabuada de qualquer
    ### número
    titulo = 'Tabuada do ' + str(numero)

    print('\n+{:-^16}+'.format(titulo))
    for fatorMultiplicador in range(1, 11):
        print('| {:>2} x {:>2} = {:>4} |'.format(numero,
                                                 fatorMultiplicador,
                                                 numero*fatorMultiplicador))
    print('+'+('-'*16)+'+')

print('Fim')
