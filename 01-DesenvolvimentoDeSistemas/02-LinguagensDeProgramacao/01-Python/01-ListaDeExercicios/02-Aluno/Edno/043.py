# (01-Gabarito/043.py)) Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#       - Abaixo de 18.5: Abaixo do Peso
#       - Entre 18.5 e 25: Peso ideal
#       - 25 até 30: Sobrepeso
#       - 30 até 40: Obesidade
#       - Acima de 40: Obesidade mórbida

peso = float(input('Digite seu peso em Kg\t: '))
altura = float(input('Digite seu peso em M\t: '))

imc = round((peso / (altura * altura)),2)
print('')
if imc < 18.5:
    print('Seu IMC é {}. Você está abaixo do peso! Vai cuidar, homem!!!'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {}. Você está no peso ideal! Parabéns!!!'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é {}. Você está com sobrebeso. Se oriente!!!'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é {}. Você está obeso. Cuide não que vc morre!!!'.format(imc))
else:
    print('Seu IMC é {}. Você está com obesidade mórbida. Você já morreu. Tá faltando só ser enterrado!!!'.format(imc))





