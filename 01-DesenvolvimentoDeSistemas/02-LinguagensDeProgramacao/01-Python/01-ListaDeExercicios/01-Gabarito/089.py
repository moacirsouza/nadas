print("""
089) Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em
uma lista composta. No final, mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente.
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
    ### O primeiro, i.e. "aluno[0]", é uma "string" vazia, onde o nome do aluno
    ### será armazenado.
    ### O segundo, i.e. "alunos[1]", é uma nova lista contendo três zeros.
    ### Estes zeros correspondem, respectivamente, às duas notas do aluno e à
    ### média aritmética delas
    alunos.append(['', [0, 0, 0]])

    ### TODO: Fazer uma validação para que as notas informadas não possam
    ### ser números negativos ou maiores que 10.
    nome = input(f'Aluno {indice+1:02d}: ').strip()
    nota01 = float(input('Nota 01: ').strip())
    nota02 = float(input('Nota 02: ').strip())
    media = (nota01+nota02)/2

    ### Cada indexação com a variável "indice" corresponde a um aluno.
    ### A partir daí, o primeiro índice zero ("[0]") corresponde ao nome
    ### do aluno
    alunos[indice][0] = nome
    ### Aqui o primeiro índice um ("[1]") acessa a lista que contém as notas
    ### e média de cada aluno. Estes últimos, por sua vez, são acessados,
    ### respectivamente, pelos últimos indices zero ("[0]"), um ("[1]") e
    ### dois ("[2]")
    alunos[indice][1][0] = nota01
    alunos[indice][1][1] = nota02
    alunos[indice][1][2] = media

    while True:
        continuar = input('Deseja continuar? (s/n) ').strip().lower()

        if continuar == 's' or continuar == 'n':
            break
        print('Digite S/s ou N/n para prosseguir ou suspender, respectivamente.')
    
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
print('{:<3} - {:<30} {}'.format('Número', 'Aluno', 'Média'))
print('-'*len(titulo))

for posicao, item in enumerate(alunos):
    ### Aqui a variável "posicao" guarda o índice de cada lista que contém
    ### o nome do aluno, as notas e a média. Essas listas, por sua vez,
    ### são referenciadas, a cada iteração, por "item". É importante lembar
    ### que estas informações estão armazenadas de forma posicional, a saber:
    ### item[0] é o nome, "item[1][0]" e "item[1][1]" as duas primeiras notas,
    ### respectivamente, e "item[1][2]", a média
    print(f'{posicao+1:06d} - {item[0]:.<30.25} {item[1][2]:>5,.2f}')

print('-'*len(titulo))

### Apresentação das notas de cada aluno, individualmente
while True:
    boletimParaApresentar = int(input('Ver boletim (999 para sair): ').strip())
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
