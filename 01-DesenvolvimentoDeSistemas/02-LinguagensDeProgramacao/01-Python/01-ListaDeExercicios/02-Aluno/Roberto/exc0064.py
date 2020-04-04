print("""
064) Crie um programa que leia vários números inteiros
pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição
de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles(desconsiderando o flag).
""")
numerosdigitados = 0
somadosnumeros = 0
numero = 0
# Poderia ser: numerosdigitados =  somadosnumeros = numero = 0
numero = int(input('Digite o número: '))

while numero != 999:
    numerosdigitados += 1
    somadosnumeros += numero
    

print('A quantidade de números digitados foi {}'.format(numerosdigitados))
print('A soma dos números digitados foi {}'.format(somadosnumeros))









