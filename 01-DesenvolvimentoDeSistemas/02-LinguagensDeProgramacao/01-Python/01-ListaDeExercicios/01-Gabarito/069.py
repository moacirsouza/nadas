print("""
069) Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No
final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
""")

totalDeHomensCadastrados = 0
totalDePessoasComMaisDeDezoitoAnos = 0
totalDeMulheresComMenosDeVinteAnos = 0
erroIdadeInvalida = 'O valor informado não pode ser usado como idade.'
erroSexoInvalido = 'Use "M/m" ou "F/f" para informar o sexo.'

while True:
    idade = input('Informe a idade: ')

    ### Valida se a idade é um tipo numérico. Se não puder,
    ### o programa repete o pedido até receber um valor
    ### válido. O método "isnumeric()" só aceita números
    ### positivos, naturais.
    if not idade.isnumeric():
        print(erroIdadeInvalida)
        continue

    idade = int(idade)

    ### Valida se o sexo foi informado com as letras
    ### "M", "m", "F" ou "f". Se não, avisa ao usuário
    ### e continua a solicitação até receber um valor
    ### válido.
    while True:
        sexo = input('Informe o sexo (m/f): ').strip().lower()

        if sexo == 'm' or sexo == 'f':
            break
        print(erroSexoInvalido)

    parada = input('Deseja continuar? (s/n) ').strip().lower()

    ### Validação da idade (18+)
    if idade >= 18:
        totalDePessoasComMaisDeDezoitoAnos += 1

    ### Validação do sexo (Masculino)
    if sexo == 'm':
        totalDeHomensCadastrados += 1

    ### Validação da mulher com menos de 20 anos
    if sexo == 'f' and idade < 20:
        totalDeMulheresComMenosDeVinteAnos += 1

    if parada == 'n':
        break

print("""
Pessoas com 18+: {}.
Homens: {}.
Mulheres com 20-: {}.
""".format(totalDePessoasComMaisDeDezoitoAnos,
           totalDeHomensCadastrados,
           totalDeMulheresComMenosDeVinteAnos)
)