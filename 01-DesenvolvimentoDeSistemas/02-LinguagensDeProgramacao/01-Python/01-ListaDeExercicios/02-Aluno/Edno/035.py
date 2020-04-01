# (01-Gabarito/035.py)) Desenvolva um programa que leia o comprimento de três retas e diga ao
# usuário se elas podem ou não formar um triângulo.

hipotenusa = float(input('Digite o valor do que será a hipotenusa\t: '))
cateto_a = float(input('Digite o valor do que será o cateto adjacente\t: '))
cateto_o = float(input('Digite o valor do que será o cateto oposto\t: '))

if pow(hipotenusa,2) == (pow(cateto_a,2)+pow(cateto_o,2)):
    print('Dá pra ser triângulo.')
else:
    print('Não dá pra ser triângulo.')
