print("""
056) Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do 
programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos.
""")

somaDasIdades = 0
idadeDoHomemMaisVelho = 0
quantidadeDeMulheresComMenosDeVinteAnos = 0

for pessoa in range(1, 5):
    print('Pessoa {:02}'.format(pessoa))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: ').strip())
    sexo = input('Sexo (m/f): ').strip().lower()
    print('\n', end='')

    somaDasIdades += idade

    if sexo == 'm':
        if idade > idadeDoHomemMaisVelho:
            idadeDoHomemMaisVelho = idade
            nomeDoHomemMaisVelho = nome
    
    if sexo == 'f' and idade < 20:
        quantidadeDeMulheresComMenosDeVinteAnos += 1

mediaDasIdades = somaDasIdades/4

print("""
Média das idades: {}.
O nome do Homem mais velho é: {}.
Quantidade de mulheres com menos de 20 anos: {}""".format(mediaDasIdades,
                                                          nomeDoHomemMaisVelho,
                                                          quantidadeDeMulheresComMenosDeVinteAnos))
    