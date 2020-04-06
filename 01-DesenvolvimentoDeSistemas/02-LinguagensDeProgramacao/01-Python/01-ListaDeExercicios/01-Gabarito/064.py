print("""
064) Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre
quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
""")

condicaoDeParada = 0
soma = 0
contador = 0

while condicaoDeParada != 999:
    condicaoDeParada = int(input('Informe um número inteiro: ').strip())
    soma += condicaoDeParada
    contador += 1
print(soma-999, contador-1)
