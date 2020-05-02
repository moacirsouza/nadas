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

while True:
    ### A cada iteração uma lista com dois elementos é adicionada a "alunos".
    ### O primeiro, i.e. "aluno[0]", é uma "string" vazia, onde o nome do aluno
    ### será armazenado.
    ### O segundo, i.e. "alunos[1]", é uma nova lista contendo três zeros.
    ### Estes zeros correspondem, respectivamente, às duas notas do aluno e à
    ### média aritmética delas
    alunos.append(['', [0, 0, 0]])

    nome = input(f'Aluno {indice+1:02d}: ').strip()
    nota01 = float(input('Nota 01: ').strip())
    nota02 = float(input('Nota 02: ').strip())
    media = (nota01+nota02)/2

    ### Cada indexação com a variável "indice" corresponde a um aluno.
    ### A partir daí, o primeiro índice zero corresponde ao nome do aluno
    alunos[indice][0] = nome
    ### Aqui o primeiro índice um acessa a lista que contém as notas e média
    ### de cada aluno. Estes últimos, por sua vez, são acessados,
    ### respectivamente pelos últimos indices zero, um e dois
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

print('-'*len(titulo))
print('{:^{tamanho}}'.format('Boletins', tamanho=len(titulo)))
print('-'*len(titulo))

for posicao, item in enumerate(alunos):
    print(f'{posicao+1} - {item[0]} {item[1][2]}')
print('-'*len(titulo))
