print("""
059) Crie um programa que leia dois valores e mostre um menu com o o ao lado na tela:
Seu programa deverá realizar a operação solicitada em cada caso.
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
""")

mensagemDeBoasVindas = ' Seja bem vindo à Roleta das Operações! '
print('[{:-^80}]'.format(mensagemDeBoasVindas))
numero01 = float(input('Digite o primeiro número: ').strip())
numero02 = float(input('Digite o segundo número: ').strip())

### Como o conhecimento adquirido até agora pode-se fazer um menu mais
### dinâmico, usando uma tupla. Também seria possível usar uma lista,
### mas os valores da estrutura não devem mudar, a não ser que a regra
### de negócios também mude, portanto, a tupla é mais adequada para esse
### caso.
listaDeOpcoes = ('somar',
                 'multiplicar',
                 'maior',
                 'novos números',
                 'sair do programa')

menu = """
Que operação deseja realizar?"""

### É possível usar "for" ou "while" para iterar no conteúdo da tupla.
### A decisão pelo "for" foi arbitrária, apenas para trazer mais
### diversidade ao programa.
for opcao in range(len(listaDeOpcoes)):
    menu += """
[{}] {}""".format(opcao+1, listaDeOpcoes[opcao])

menu += """
Escolha: """

escolhaDoUsuario = 0
saida = False

while escolhaDoUsuario != len(listaDeOpcoes):
    escolhaDoUsuario = int(input(menu))

    # if escolhaDoUsuario > len(listaDeOpcoes) or escolhaDoUsuario <= 0:
    #     print('Opção inválida. Tente novamente')
    #     continue
    
    if listaDeOpcoes[escolhaDoUsuario-1] == 'somar':
        resultado = numero01 + numero02
    
    if listaDeOpcoes[escolhaDoUsuario-1] == 'multiplicar':
      resultado = numero01 * numero02
    
    if listaDeOpcoes[escolhaDoUsuario-1] == 'maior':
        maior = numero01
        if numero02 > numero01:
            maior = numero02
        resultado = maior

    if listaDeOpcoes[escolhaDoUsuario-1] == 'novos números':
        numero01 = float(input('Digite o primeiro número: ').strip())
        numero02 = float(input('Digite o segundo número: ').strip())
        resultado = 'Os novo números são: {} e {}.'.format(numero01, numero02)

    if listaDeOpcoes[escolhaDoUsuario-1] == 'sair do programa':
        mensagemFinal = 'Obrigado por jogar. Volte sempre.'
        saida = True
    
    if not saida:
        mensagemFinal = """
Seus números são {} e {} e operação escolhida foi: {}.
O resultado é: {}""".format(numero01,
                            numero02,
                            listaDeOpcoes[escolhaDoUsuario-1],
                            resultado)

    print(mensagemFinal)
