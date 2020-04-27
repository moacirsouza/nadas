print("""
083) Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e
fechados na ordem correta.
""")

### TODO: Refazer. A lógica está muito confusa.
entrada = []
entrada += input('Digite uma expressão matemática: ').strip().lower()

for i in entrada:
    parentesesAbertos = entrada.count('(')
    parentesesFechados = entrada.count(')')
    if parentesesAbertos != parentesesFechados:
        print('Parenteses sem casamento')
        break
    else:
        if parentesesAbertos == 0 and parentesesFechados == 0:
            ### TODO: Validar o caso de parênteses vazios, e.g.,
            ### na expressão "()"
            if len(entrada) != 0:
                print('ok')
                break
            else:
                print('errado')
        else:
            posicaoDoParenteseAberto = entrada.index('(')
            posicaoDoParenteseFechado = entrada.index(')')
            print(entrada)
            if posicaoDoParenteseFechado > posicaoDoParenteseAberto:
                entrada.pop(posicaoDoParenteseAberto)
                entrada.pop(posicaoDoParenteseFechado-1)
                print(entrada)
            else:
                print(entrada)
                print('Parenteses fora de ordem')
                break
