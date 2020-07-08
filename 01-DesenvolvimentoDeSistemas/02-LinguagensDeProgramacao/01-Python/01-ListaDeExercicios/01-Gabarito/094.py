print("""
094) Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários
em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
""")

titulo = ' Cadastro e estatísticas de Pessoas '
formatador = len(titulo)
pessoa = {}
cadastro = []
listaDasMulheres = []
idadesAcimaDaMedia = []
somaDasIdades = 0

print('-'*formatador)
print(titulo)
print('-'*formatador)
print(f'{"Preencha as informações abaixo":^{formatador}}')

while True:
    nome = input('Nome: ').strip()
    
    while True:
        sexo = input('Sexo (m/f): ').strip().lower()

        if sexo == 'm' or sexo == 'f':
            break
        print('O sexo só pode ser informado com M/m ou F/f.')
    
    idade = int(input(f'Idade de "{nome}": ').strip())
    somaDasIdades += idade
    
    while True:
        continuar = input('Deseja continuar? (s/n) ').strip().lower()

        if continuar == 's' or continuar == 'n':
            break
        print('Digite S/s ou N/n para prosseguir ou suspender, \
respectivamente.')

    pessoa = dict(Nome=nome, Sexo=sexo, Idade=idade)
    cadastro.append(pessoa.copy())
    pessoa.clear()

    if continuar == 'n':
        break

quantidadePessoas = len(cadastro)
mediaDasIdades = somaDasIdades/quantidadePessoas

for cadastrado in cadastro:
    sexo = cadastrado['Sexo']
    idade = cadastrado['Idade']
    nome = cadastrado['Nome']
    
    if sexo == 'f':
        listaDasMulheres.append(nome)
    
    if idade > mediaDasIdades:
        idadesAcimaDaMedia.append(f'{nome} ({idade})')

if not listaDasMulheres:
    listaDasMulheres.append('Nenhuma mulher cadastrada')

if not idadesAcimaDaMedia:
    idadesAcimaDaMedia.append('Não há ninguém com idade acima da média')

print('-'*formatador)
print(f'{"Resultado":^{formatador}}')
print('-'*formatador)

print(f'A) Quantidade de pessoas cadastradas: {quantidadePessoas}.')
print(f'B) Lista das mulheres: {", ".join(listaDasMulheres)}.')
print(f'C) A média de idade do(s) cadastrado(s) é {mediaDasIdades:.2f}.')
print(f'D) Pessoas com idade acima da média: {", ".join(idadesAcimaDaMedia)}.')
