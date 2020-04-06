print("""
064) Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre
quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
""")

condicaoDeParada = 0
soma = 0
contador = 0
flag = 999

while condicaoDeParada != flag:
    condicaoDeParada = int(input('Informe um número inteiro (999 para sair): ').strip())
    soma += condicaoDeParada
    contador += 1

print("""
Você informou {} número(s).
O somatório dele(s) é: {}
""".format(contador-1, soma-flag))
