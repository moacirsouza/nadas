print("""
066) Crie um programa que leia vários números inteiros pelo teclado. O programa só
vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando
o flag).
""")

contador = soma = 0

while True:
    numero = int(input('Informe um número (999 para sair): ').strip())

    if numero == 999:
        break

    soma += numero
    contador += 1

print("""
{} números foram mostrados.
A soma deles é {},""".format(contador, soma))
