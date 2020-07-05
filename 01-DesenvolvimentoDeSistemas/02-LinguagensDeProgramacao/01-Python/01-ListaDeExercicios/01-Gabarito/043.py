print("""
043) Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
""")

peso = float(input('Informe o peso do(a) paciente (Em quilos): ').strip())
altura = float(input('Informe a altura do(a) paciente (Em metros): ').strip())

### O Índice de Massa Corpórea, ou IMC, é calculado dividindo-se
### o peso pelo quadrado da altura, conforme orientação da
### Organização Mundial de Saúde
imc = peso/(altura**2)

if imc < 18.5:
    situacaoDoPaciente = 'abaixo do peso'
elif 18.5 <= imc < 25:
    situacaoDoPaciente = 'com peso ideal'
elif 25 <= imc < 30:
    situacaoDoPaciente = 'com sobrepeso'
elif 30 <= imc <= 40:
    situacaoDoPaciente = 'obeso(a)'
else:
    situacaoDoPaciente = 'com obesidade mórbida'

mensagemFinal = """
O IMC (Índice de Massa Corpórea), do(a)
paciente é {:.2f}. Nesta situação ele(a)
está {}.
""".format(imc, situacaoDoPaciente)

print(mensagemFinal)
