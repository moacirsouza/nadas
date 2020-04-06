print("""
065) Crie um programa que leia vários números inteiros pelo teclado. No final da execução
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa
deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
""")

maior = menor = soma = contador = 0
condicaoDeParada = 's'

while condicaoDeParada != 'n':
    numero = int(input('Informe um número inteiro: ').strip())
    soma += numero

    if contador == 0:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        else:
            menor = numero

    condicaoDeParada = str(input('Quer continuar? (s/n): ').strip())
    contador += 1

media = soma/contador

print("""
Média: {:.2f}
Maior: {}
Menor: {}""".format(media, maior, menor))
