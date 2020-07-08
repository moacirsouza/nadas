print("""
089) Crie um programa que leia nome e duas notas de vários alunos e guarde
tudo em uma lista composta. No final, mostre um boletim contendo a média de
cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.
""")

alunos = []
indice = 0
titulo = ' Sistema de Cadastro e Visualização de Notas '
print('-'*len(titulo))
print(f'{titulo}')
print('-'*len(titulo))

### Preenchimento da lista de alunos com nome, duas notas e a média ente elas
while True:
    ### A cada iteração uma lista com dois elementos é adicionada a "alunos".
    ### O primeiro, i.e. "aluno[0]", é uma "string" vazia, onde o nome do
    ### aluno será armazenado.
    ### O segundo, i.e. "alunos[1]", é uma nova lista contendo três zeros.
    ### Estes zeros correspondem, respectivamente, às duas notas do aluno
    ### e à média aritmética delas
    alunos.append(['', [0, 0, 0]])

    nome = input(f'Aluno {indice+1:02d}: ').strip()
    
    while True:
        nota01 = float(input('Nota 01: ').strip())

        if nota01 >= 0 and nota01 <= 10:
            break
        print('Informe uma nota válida. Valores entre 0 e 10.')

    while True:
        nota02 = float(input('Nota 02: ').strip())
        
        if nota02 >= 0 and nota02 <= 10:
            break
        print('Informe uma nota válida. Valores entre 0 e 10.')
    
    media = (nota01+nota02)/2

    ### Cada indexação com a variável "indice" corresponde a um aluno.
    ### A partir daí, o primeiro índice zero ("[0]") corresponde ao nome
    ### do aluno
    alunos[indice][0] = nome

    ### Aqui o primeiro índice um ("[1]") acessa a lista que contém as
    ### notas e média de cada aluno. Estes últimos, por sua vez, são
    ### acessados, respectivamente, pelos últimos indices zero ("[0]"),
    ### um ("[1]") e dois ("[2]")
    alunos[indice][1][0] = nota01
    alunos[indice][1][1] = nota02
    alunos[indice][1][2] = media

    while True:
        continuar = input('Deseja continuar? (s/n) ').strip().lower()

        if continuar == 's' or continuar == 'n':
            break
        print('Digite S/s ou N/n para prosseguir ou suspender, \
respectivamente.')
    
    if continuar == 'n':
        break

    ### O motivo de incrementar a variável "indice" apenas no final,
    ### logo após o teste de continuidade, é que ela só precisa ser
    ### alterada, se o laço não for interrompido
    indice += 1

### Apresentação do Boletim com um sequencial, nome e média de cada aluno
print('-'*len(titulo))
print('{:^{tamanho}}'.format('Boletins', tamanho=len(titulo)))
print('-'*len(titulo))
print('{:<3} |{:^30}| {}'.format('Número', 'Aluno', 'Média'))
print('-'*len(titulo))

for posicao, item in enumerate(alunos):
    ### Aqui a variável "posicao" guarda o índice de cada lista que
    ### contém o nome do aluno, as notas e a média. Essas listas, por
    ### sua vez, são referenciadas, a cada iteração, por "item". É
    ### importante lembar que estas informações estão armazenadas de
    ### forma posicional, a saber:
    ### - item[0]: ...... Nome
    ### - item[1][0]: ... Primeira nota
    ### - item[1][1]: ... Segunda nota
    ### - item[1][2]: ... Média
    print(f'{posicao+1:06d} |{item[0]:.<30.25}|{item[1][2]:>5,.2f}')

print('-'*len(titulo))

### Apresentação das notas de cada aluno, individualmente
while True:
    mensagemDeSaida = 'Ver boletim (999 para sair): '
    boletimParaApresentar = int(input(mensagemDeSaida).strip())
    
    if boletimParaApresentar == 999:
        print('Programa finalizado!')
        break
    else:
        ### É importante notar que, apesar de utilizar os mesmos
        ### identificadores do laço de criação da lista, não há
        ### problemas, uma vez que os escopos em que as variáveis
        ### existem são distintos e não conflitantes
        nome = alunos[boletimParaApresentar-1][0]
        nota01 = alunos[boletimParaApresentar-1][1][0]
        nota02 = alunos[boletimParaApresentar-1][1][1]

        print(f'As notas de "{nome}" foram {nota01} e {nota02}')
