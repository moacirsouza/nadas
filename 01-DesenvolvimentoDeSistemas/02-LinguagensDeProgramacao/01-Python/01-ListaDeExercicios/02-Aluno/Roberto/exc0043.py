print("""
043) Desenvolva uma lógia que leia o peso e a altura de uma pessoa, 
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
""")

peso = float(input('Qual o seu peso? (kg) ' ))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura**2)
print('O seu IMC será {:.1f}'.format(imc))
if imc < 18.5:
  print('Você está abaixo do peso')
elif 18.5 <= imc < 25: 
  print('Parabéns, você está no peso IDEAL')
elif 25 <= imc < 30:
  print('Você está com Sobrepeso')
elif 30 <= imc <= 40:
  print('Você está com Obesidade')
elif imc > 40:
  print('Você está com Obesidade Mórbida')


